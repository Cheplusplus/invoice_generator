from jinja2 import Template
import pdfkit
from participant import Sender, Client
from item import Item
from currencies import Currency
from datetime import date
import random
import string
from img_to_base64 import img_to_base64


class Invoice():

    _used_invoice_numbers = {''}

    def __init__(self, html: str,css: str) -> None:
        self.html: str = html
        self.css: str = css
        self._sender: object = Sender()
        self._client: object = Client()
        self._items: list = []
        self._currency: Currency = Currency.DOLLAR
        self._invoice_number: int = self._invoice_number_generator()
        self._date: date = date.today()
        self._profile_photo: str = ""
        self._total: float = 0.00

    def render(self) -> None:
        # Renders the template
        template = open(self.html, "r").read()
        jt = Template(template)
        data = self._get_data()
        self._rendered = jt.render(data)
        
    def output_pdf(self,filename, options: dict={'encoding':'UTF-8'}) -> None:
        # Outputs render to PDF
        self.render()
        try:
            pdfkit.from_string(self._rendered, f"{filename}.pdf", css=self.css, options=options)
        except:
            pass

    def output_html(self, filename):
        self.render()
        with open(f"{filename}.html", 'w+') as file:
            file.write(self._rendered)

    def _get_data(self) -> dict:
        # Gets data for the template
        data = {
            "sender":{ k.replace('_', ''): v for k, v in self._set_from_class(self._sender) },
            "client":{ k.replace('_', ''): v for k, v in self._set_from_class(self._client) },
            "items": [vars(item) for item in self._items],
            "currency": self.currency,
            "invoice_number": self._invoice_number,
            "date": self._date,
            "profile_photo": self._profile_photo,
            "total": self._get_total_cost(),
        }
        return data
    
    def new_item(self, description: str, cost: float, quantity: float) -> str:
        # Add a new item to the invoice
        self._items.append(Item(description, cost, quantity))
        return f"Item created: description:{description}, cost:{cost}, quantity:{quantity}"
    
    def remove_item(self, index: int) -> bool:
        # Remove an item from the invoice
        try:
            del self._items[index]
            return True
        except:
            return False
        
    def edit_item(self,index: int, description: str='', cost: float='', quantity: float='') -> Item:
        try:
            this_item = self._items[index]
            if description != '':
                this_item.description = str(description)
            if cost != '':
                if type(cost) == float:
                    this_item.cost = cost
                else:
                    return None
            if quantity != '':
                if type(quantity) == float:
                    this_item.quantity = quantity
            return vars(self._items[index])
        except:
            return None

    @property
    def sender(self) -> Sender:
        # Return the sender of the invoice
        return self._sender
    
    @sender.setter
    def sender(self, sender: Sender) -> None:
        # Set the sender to new Sender object
        self._sender = sender

    @property
    def client(self) -> Client:
        # Return the client of the invoice
        return self._client
    
    @client.setter
    def client(self, client: Client) -> None:
        # Set the client to new Sender object
        self._client = client

    @property
    def currency(self) -> str:
        return self._currency._value_
     
    @currency.setter
    def currency(self, currency: Currency) -> None:
        if type(currency) != Currency:
            raise Exception("Must be of type 'Currency'")
        self._currency = currency

    @property
    def invoice_number(self) -> Client:
        return self._invoice_number
    
    def _invoice_number_generator(self) -> str:
        invoice_number = ''
        while invoice_number in self._used_invoice_numbers:
            invoice_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self._used_invoice_numbers.add(invoice_number)
        return invoice_number

    @property
    def date(self) -> date:
        return self._date
    
    @date.setter
    def date(self, new_date) -> None:
        self._date = date.fromisoformat(new_date)
    
    def update_profile_photo(self, photo_url: str) -> None:
        self._profile_photo = img_to_base64(photo_url)

    def __del__(self) -> None:
        self._used_invoice_numbers.remove(self._invoice_number)

    def _get_total_cost(self) -> float:
        total = 0.0
        for item in self._items:
            total += item.cost * item.quantity
        return total

    @staticmethod
    def _set_from_class(cls) -> set:
        return set((key, value)for (key, value) in cls.__dict__.items())