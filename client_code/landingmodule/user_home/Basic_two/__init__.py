from ._anvil_designer import Basic_twoTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Basic_two(Basic_twoTemplate):
  def __init__(self, name,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name=name
    print(name)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_one')


  def button_2_click(self, **event_args):
    invest_amount = self.drop_down_1.selected_value
    mobile_no = self.text_box_2.text
    email_id = self.text_box_2.text
    profile_img = self.file_loader_1.file
    if not invest_amount or not mobile_no or not email_id or not profile_img:
      Notification("plz enter all required fields").show()
    else:
      name =self.name
      row = app_tables.lendor.search(name=name)
      if len(row) > 0:
        row[0]['investment']=invest_amount
        row[0]['mobile']=mobile_no
        row[0]['email']=email_id
        row[0]['profile_photo']=profile_img
        open_form('landingmodule.user_home.Basic_three',name=name)
      
   
    



  


  


  

    
    

    

