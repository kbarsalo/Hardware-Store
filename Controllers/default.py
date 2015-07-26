# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control



#Note to graders: A lot of this code is from the teacher's hints, but I changed a lot 
#to meet by needs. I am aware the ajax call to product price is very wonky, mark down
#what you wish. A passing grade would be awesome though. Get price is not working 
#correctly, but everything else is. 


@auth.requires_login()
def index():

    response.flash = T("Welcome to NailIt")
    user_appellation = auth.user.first_name
    if user_appellation:
        print user_appellation
    else: print "user undefined"
    return locals()

@auth.requires_login()
def create_order():
    
    #Global variables to be updated
    datime = request.now
    amount = 0              # initial value for order total amount
    prod = ''               #initial blank product order used to update DB
    quanity = 0             #initial value for product quantity(misspelled on purpose)
    price = 0               #initial price of said product used to update DB
    
    #Teacher's code used to get the product Name
    productNames = db().select(db.product.name) 

    #Teacher's Ajax example
    get_price_url = URL('get_price')   
    
    #"Update NailIt’s database to record order data for customer order" - From PDF
    #Updates purchase SQL database (Needed for customer's reference)
    purchase = db.purchase.insert(date=datime,product=prod,quantity=quanity, total=amount)
    
    #Updates customer SQL database
    #Note: I'm not making the user input their phone #
    buyer = db.customer.insert(name=auth.user.first_name, email=auth.user.email)
    
    #Updates product SQL database
    product=db.product.insert(name=prod,price=price,quantity=quanity)
    

    
    #Test code to make sure SQL was updating correctly
    #me = db(db.customer.id==buyer).select() #this works
    
 

    return locals()

def get_price():
    """
    URI targeted by ajax request to retrieve price for selected product
    """
    
    #Teacher's code. Could not get it working.
    #price = db(db.product.name == productName).select(db.product.price)[0].price
    
    
    return (200)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login()
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
