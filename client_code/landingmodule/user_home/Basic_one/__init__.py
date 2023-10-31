from ._anvil_designer import Basic_oneTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Basic_one(Basic_oneTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  # this one is for taking back to user form
  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home')
    """This method is called when the button is clicked"""
    

  # this for second storage 
  def button_2_click(self, **event_args):
    name = self.text_box_1.text
    city = self.text_box_2.text
    gender = self.drop_down_1.selected_value
    if not name or not city or not gender:
      Notification("plz enter all required fields ").show()
    else:
      anvil.server.call('add_lendor_first_form',name,city,gender)
      Notification("step form fill up submited sucessfull")
      open_form('landingmodule.user_home.Basic_two',name=name)
   

  


  

    

  

