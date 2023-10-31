from ._anvil_designer import logout_homeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import main_form_module


class logout_home(logout_homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  #-------------no need to change-----

  def home_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form')

  def about_us_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form.about_main_form')

  def faqs_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form.faqs_main_form')

  def careers_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form.careers_main_form')

  def location_main_form_link_click(self, **event_args):
    open_form('landingmodule.main_form.locations_main_form')

  #---------no nead to change-------

  def login_main_form_butoon_click(self, **event_args):
    open_form('landingmodule.login_main')



