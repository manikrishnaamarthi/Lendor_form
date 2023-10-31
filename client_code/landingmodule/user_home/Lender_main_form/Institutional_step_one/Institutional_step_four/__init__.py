from ._anvil_designer import Institutional_step_fourTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Institutional_step_four(Institutional_step_fourTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('landingmodule.user_home.Lender_main_form.Institutional_step_one.Institutional_step_three')
    """This method is called when the link is clicked"""

  def button_1_click(self, **event_args):
    open_form('landingmodule.user_home.Lender_main_form.Institutional_step_one.Institutional_step_five')
    """This method is called when the button is clicked"""
    

    

