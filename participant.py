class Participant():
    def __init__(self) -> None:
        self._name = ""
        self._surname = ""
        self._company = ""
        self._address = ""
        self._phone = ""
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = str(name)

    @property
    def surname(self) -> str:
        return self._surname
    
    @surname.setter
    def surname(self, surname):
        self._surname = str(surname)

    @property
    def company(self) -> str:
        return self._company
    
    @company.setter
    def company(self, company):
        self._company = str(company)

    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = str(address)

    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = str(phone)

    def edit(self, name: str='', surname: str='', company: str='', address: str='', phone: str='') -> dict:
        try:
            if name != '':
                self.name = str(name)
            if surname != '':
                self.surname = str(surname)
            if company != '':
                self.company = str(company)
            if address != '':
                self.address = str(address)
            if phone != '':
                self.phone = str(phone)
            return vars(self)
        except:
            return False


class Sender(Participant):
    pass


class Client(Participant):
    pass