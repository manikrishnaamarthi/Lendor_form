import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
email_addr = anvil.google.auth.get_user_email()

@anvil.server.callable
def add_user(name, mobile, mail, pincode, userid, passcode):
  app_tables.users.add_row(name=name,Date_of_signup=datetime.now(),mobile_no=mobile,mail_id=mail,pincode=pincode, user_id=userid, passward=passcode)



# This is for form_1
