# Stock Price SMS Alert

## Python way to get SMS Alert based on Stock Price hike/fall

Best practice to use the virtualenv by following the below steps:

```
sudo easy_install pip
pip install virtualenv
pip install -Ur requirements.txt
virtualenv venv
source venv/bin/activate
```
#### Enter the details required in the lines of code starting from below to make this functional for your personal use:

`https://github.com/maxmohash/stockprice-sms-alert/blob/master/stocksmsalert.py#L6`

#### Now to get the Stock Alert via SMS just type in terminal:

`python stocksmsalert.py`

#### You can also Use Makefile commands to install everything:

`make clean freshstart`

#### Screenshots of Alert:

https://github.com/maxmohash/stockprice-sms-alert/blob/master/IMG-8388.PNG

https://github.com/maxmohash/stockprice-sms-alert/blob/master/IMG-8387.PNG

##### Read https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest#send-sms-via-library to know about Twilio API

## Now set the alert and enjoy!