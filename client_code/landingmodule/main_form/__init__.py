from ._anvil_designer import main_formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import main_form_module


class main_form(main_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def sign_up_main_form_button_click(self, **event_args):
    # the data is fetch from the main_form
    
    first_name = self.first_name_main_form_text.text
    last_name = self.last_name_main_form_text.text
    email_id = self.email_main_form_text.text
    mobile = self.mobile_main_form_text.text
    pincode = self.pincode_main_form_text.text
    date_of_birth =self.date_of_birth_main_form.date
    gender =self.gender_value_main_form.selected_value

    # this is the default passcode given to db later user can edit
    password=self.pincode_main_form_text.text+self.mobile_main_form_text.text

    #this code have to be change
    user_id = self.mobile_main_form_text.text+self.pincode_main_form_text.text
    
    # Check if any of the fields are empty
    if not first_name or not last_name or not email_id or not mobile or not pincode or not date_of_birth or not gender:
        Notification('Please fill in all fields').show()
    else:
      name = first_name + last_name
      anvil.server.call('add_user', name, email_id, mobile, pincode, user_id, password)
      Notification('Your details were submitted ' + name).show()
      main_form_module.email_id=email_id
      main_form_module.name=name
      main_form_module.password=password
      main_form_module.user_id=user_id
      open_form('landingmodule.user_home')
      
      

  def login_main_form_butoon_click(self, **event_args):
   
    open_form('landingmodule.login_main')

  # this button is use to clear the form
  def clear_main_form_button_click(self, **event_args):
    
    self.first_name_main_form_text.text = None
    self.last_name_main_form_text.text = None
    self.email_main_form_text.text = None
    self.mobile_main_form_text.text = None
    self.pincode_main_form_text.text = None
    self.date_of_birth_main_form.date = None
    self.gender_value_main_form.selected_value = None

  
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


  
  #this is google button for first signup
  def google_sighnup_mainform_button_click(self, **event_args):
    email_addr = anvil.google.auth.login()

  def gender_value_main_form_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  

   

   



   

    

   


    
    

  

    
    

    





