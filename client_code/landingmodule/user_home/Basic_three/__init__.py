from ._anvil_designer import Basic_threeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Basic_three(Basic_threeTemplate):
  def __init__(self, name,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name =name
    print(name)

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_two')

  def button_2_click(self, **event_args):
    hear = self.drop_down_1.selected_value
    if not hear:
      Notification("fill the details ").show()
    else:
      name =self.name
      row = app_tables.lendor.search(name=name)
      if len(row) > 0:
        row[0]['hear']=hear
        open_form('landingmodule.user_home.Basic_four',name=name)
    
    

  

