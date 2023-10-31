from ._anvil_designer import Basic_fourTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Basic_four(Basic_fourTemplate):
  def __init__(self,name, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name=name

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Basic_three')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    user_qualification = self.drop_down_1.selected_value
    pan_number = self.text_box_1.text
    pan_img = self.file_loader_1.file
    if not user_qualification or not pan_number or not pan_img:
      Notification("plz fill all the details ").show()
    else:
      name =self.name
      row = app_tables.lendor.search(name=name)
      if len(row) > 0:
        row[0]['qualification_degree'] = user_qualification
        row[0]['pan_card_number']=pan_number
        row[0]['pan_img']=pan_img
        open_form('landingmodule.user_home.Basic_five',name=name)
    

    

