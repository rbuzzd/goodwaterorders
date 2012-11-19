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
    Time = db.StringProperty()#db.DateTimeProperty()
    OrderedProduct = db.ReferenceProperty(Product)
    Amount = db.IntegerProperty()
    IsPaid = db.BooleanProperty()
    IsDone = db.BooleanProperty()
    Comment = db.TextProperty()
#endregion


class MainPage(webapp2.RequestHandler):
  def get(self):    
      jinja_environment = jinja2.Environment(autoescape=True,
          loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
      template = jinja_environment.get_template('index.html')
      template_values = {
          'footerText': footerText
          }
      self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),
                                ('/main', MainPage)],
                                debug=True)