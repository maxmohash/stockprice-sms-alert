import urllib, time
from bs4 import BeautifulSoup
from twilio.rest import Client


# Make sure the stock symbol entered is correct below
your_stock_symbol = "isrg"
your_stock_market = "NASDAQ"
google_finance_request_url = "https://www.google.com/finance?q={}%3A{}".format(your_stock_market, your_stock_symbol)
# Enter the price hike (i.e. in USD) you expect and wish to be notified
# if the actual stock price equals or rises above it
expected_hike = 8

# You can get your personal account-sid and auth_token by registering at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
your_cell_number = "+15555555556"
# The below given Twilio number has to be taken for trial or bought from Twilio
# here https://www.twilio.com/console/phone-numbers/incoming
from_twilio_number = "+15555555555"


def stock_sms_alert_on_price_hike():
    try:
        open_url = urllib.urlopen(google_finance_request_url)
        get_text = open_url.read()
        parsed_text = BeautifulSoup(get_text, 'html.parser')
        price_change_field = parsed_text.find('span', attrs={'class' : 'chg'})
        price_change = price_change_field.text.strip()
        if price_change is not None:
            split_price_value = list(str(price_change))
            if split_price_value[0] == '+':
                if price_change >= expected_hike:
                    client = Client(account_sid, auth_token)
                    client.api.account.messages.create(
                        to=your_cell_number,
                        from_=from_twilio_number,
                        body="Price hike of {} seen which is above your expected price of {} for your stock {}".format(
                            price_change, expected_hike, your_stock_symbol))
        else:
            print("Price change not found for " + your_stock_symbol)
    except Exception, e:
        print str(e)
        print 'Error occurred in getting price change. Please ensure the stock symbol entered is correct'


while True:
    stock_sms_alert_on_price_hike()
    # This condition checks the price change every 30 minutes as of now i.e. 30*60=1800seconds
    time.sleep(1800)

