# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioPricingClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = TwilioPricingClient(account_sid, auth_token)

country = client.phone_numbers.countries.get("US") 

for p in country.phone_number_prices:
    print("{} {}".format(p['number_type'], p['current_price']))