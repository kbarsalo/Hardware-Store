# -*- coding: utf-8 -*-

db = DAL("sqlite://storage.sqlite")


#The following defines a database pertaining to the product being bought

#quantity_in_store is an integer (rating system arbitary) of the product bought in the store
#price is an integer (to avoid mess) cost of the product being bought
#quantity is a integer (rating system arbitary) of the the product bought outside of the store
#supplies this should reference the table supplier whoever that may be. I realize it doesn't work so I'm changing it to string so theres no errors.
#Could be say Amazon, Ebay, etc. Supplier would have that information.
db.define_table('product',
   Field('name', 'string'),
   Field('price', 'integer'), #changed to int to avoid wonky #s
   Field('quantity', 'integer'),
   Field('suppliers', 'list:reference supplier'),
   format = '%(name)s',
   singular = 'product',
   plural = 'products')

#Defines a table relating to the name of said supplier, adrress, and contact information of more than one person. 

#name is a string of the actual name of supplier, i.e Amazon.
#address is a string of the physical address of the supplier.
#contacts is a reference to contact databse.
db.define_table('supplier',
   Field('name', 'string'),
   Field('address', 'string'),
   Field('contacts', 'list:reference contact'), 
   format = '%(name)s',
   singular = 'supplier',
   plural = 'suppliers')

#Defines the standard contact information required for sending, name, email, phone, extra info about contact

#name is a string of the given name of the contact like Alice Webber
#email is a string of the online address of the contact, i.e AliceW@amazon.com
#phone is a integer the contact's phone number used to reach them. 
#note is a text (or note style on web2py) used to put on additional notes about the contact such as position in company or title. 
db.define_table('contact',
   Field('name', 'string'),
   Field('phone', 'integer'),
   Field('email', 'string'),
   Field('description', 'text'),
   format = '%(name)s',
   singular = 'contact',
   plural = 'contacts')


#Table pertaining to the customer's name, phone number, email, and bought purchases

#name is a string name of the customer buying said product.
#phone is a integer phone number of the customer to reach them.
#email is a string online address would to reach them.
#purchases is a reference to purchase database containing the string names of the purchases bought
db.define_table('customer',
   Field('name', 'string'),
   Field('phone', 'integer'),
   Field('email', 'string'),
   Field('purchases', 'list:reference purchase'), 
   format = '%(name)s',
   singular = 'customer',
   plural = 'customers')

#Table refers to the purchase bought by a customer with information on date bought, what was bough, the price, quantity, and total

#date is the datetime of bough item. Will be in the form of the date and time bought.
#product is the string of the name of the bought product
#quantity is an integer that refers to how much of the product is being bought
#total is a integer of the total price of bought
db.define_table('purchase',
   Field('date', 'datetime'),
   Field('product', 'string'),
   Field('quantity', 'integer'),
   Field('total', 'integer'),
   singular = 'purchase',
   plural = 'purchases')
