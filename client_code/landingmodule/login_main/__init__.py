from ._anvil_designer import login_mainTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class login_main(login_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_login_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form')

  def google_login_main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def signup_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form')



  


    
 
    


  
