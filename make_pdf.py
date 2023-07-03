from invoice import Invoice, Currency

x = Invoice('templates/invoice_template.html', 'templates/style2.css' )
x.sender.edit(    
                    name='che',
                    surname='overmeyer',
                    company='Journey On',
                    address='Some address',
                    phone='2223334402'
            ) 

x.client.edit(

                    name='john',
                    surname='smith',
                    company='Grottos',
                    address='55 adfdfda asdfasdf',
                    phone='25566326'
            ) 
x.new_item("Chips", 12.3, 4)
x.new_item("Coke", 9.5, 2)
x.new_item("Chocolate", 20.50, 1)


x.currency = Currency.RAND
x.update_profile_photo('media/logo.png')
x.output_pdf('test2')
x.output_html('test')