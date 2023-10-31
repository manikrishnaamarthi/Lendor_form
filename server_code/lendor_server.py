import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def add_lendor_first_form(name_,city_,gender_):
  app_tables.lendor.add_row(name=name_,city=city_,gender=gender_)

# @anvil.server.callable
# def add_lendor_second_form(name, invest_amount, mobile_no, email_id, profile_img):
#   lendor_row =app_tables.lendor.search(name=name)
#   if len()