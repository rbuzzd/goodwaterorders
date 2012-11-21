# -*- coding: utf-8 -*-
import webapp2
import random
import jinja2
import os
from google.appengine.ext import db
import json

#region Models
class Product(db.Model):
    Name = db.StringProperty()
    Price = db.FloatProperty()
    Comment = db.TextProperty()


class Customer(db.Model):
    Name = db.StringProperty()
    Phone = db.StringProperty()
    Street = db.StringProperty()
    HouseNumber = db.StringProperty()
    FlatNumber = db.StringProperty()
    Comment = db.TextProperty()
    Balance = db.FloatProperty()


class Order(db.Model):
    Client = db.ReferenceProperty(Customer)
    Time = db.StringProperty()
    OrderedProduct = db.ReferenceProperty(Product)
    Amount = db.IntegerProperty()
    IsPaid = db.BooleanProperty()
    IsDone = db.BooleanProperty()
    Comment = db.TextProperty()

#endregion

class GetCustomers(webapp2.RequestHandler):
    def get(self):
        customers = Customer.all().fetch(1000)# db.GqlQuery("SELECT * FROM Customer").run()
        prepJson = []
        for customer in customers:
            tempCustomer = dict()
            tempCustomer["ID"] = customer.key().id()
            tempCustomer["Key"] = str(customer.key())
            tempCustomer["Name"] = customer.Name
            tempCustomer["Phone"] = customer.Phone
            tempCustomer["Street"] = customer.Street
            tempCustomer["HouseNumber"] = customer.HouseNumber
            tempCustomer["FlatNumber"] = customer.FlatNumber
            tempCustomer["Balance"] = customer.Balance
            tempCustomer["Comment"] = customer.Comment
            prepJson.append(tempCustomer)
        self.response.write(json.dumps(prepJson))


class GetProducts(webapp2.RequestHandler):
    def get(self):
        products = Product.all().fetch(1000)# db.GqlQuery("SELECT * FROM Customer").run()
        prepJson = []
        for product in products:
            temp_product = dict()
            temp_product["ID"] = product.key().id()
            temp_product["Key"] = str(product.key())
            temp_product["Name"] = product.Name
            temp_product["Price"] = product.Price
            temp_product["Comment"] = product.Comment
            prepJson.append(temp_product)
        self.response.write(json.dumps(prepJson))



class MainPage(webapp2.RequestHandler):
    def get(self):
        jinja_environment = jinja2.Environment(autoescape=True,
            loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
        template = jinja_environment.get_template('index.html')
        template_values = {}
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),
    ('/main', MainPage),
    ('/getCustomers', GetCustomers),
    ('/getProducts', GetProducts)],
    debug=True)