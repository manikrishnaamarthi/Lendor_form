from ._anvil_designer import user_homeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import main_form_module

class user_home(user_homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_of_user.text = "Welcome " + main_form_module.name
    # Any code you write here will run before the form opens.

  

  

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass


  def logout_user_home_button_click(self, **event_args):
    open_form('landingmodule.logout_home')

  def home_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home')

  def about_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home.about_user_home')
   

  def services_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home.services_user_home')
   
  def product_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home.products_user_home')

  def borrower_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home.borrower_user_home_registertion_form')

  def lendor_user_home_button_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_one')
    """This method is called when the button is clicked"""
    


  


  
    

 




   





    

   

 
   

   


 
    




    

    










