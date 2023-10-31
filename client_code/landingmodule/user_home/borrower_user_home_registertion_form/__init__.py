from ._anvil_designer import borrower_user_home_registertion_formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import main_form_module


class borrower_user_home_registertion_form(borrower_user_home_registertion_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

 

  def submit_borrower_user_home_registertion_button_click(self, **event_args):
    open_form('landingmodule.user_home.borrower_user_home_registertion_form.borrower_user_home_registertion_form_step_2')

  def clear_click(self, **event_args):
    print("this button need to done")

  def back_borrower_user_home_registertion_button_click(self, **event_args):
    open_form('landingmodule.user_home')
   

    

    

    





