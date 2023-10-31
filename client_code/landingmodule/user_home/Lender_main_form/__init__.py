from ._anvil_designer import Lender_main_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_main_form(Lender_main_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  
      
    """This method is called when the button is clicked"""

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def button_1_click(self, **event_args):
    if self.radio_button_1.selected:
      open_form('landingmodule.user_home.Lender_main_form.Individual_step_one')
    elif self.radio_button_2:
      open_form('landingmodule.user_home.Lender_main_form.Institutional_step_one')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_seven')
    """This method is called when the button is clicked"""

  

    

    




  

  

  

    
    

  
  

  

    

    


