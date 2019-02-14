# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        self.username = "omambia"
        self.api_key = "4eb8662a2ecef1c54c1650179e397a3d18a591df35e00269fd48fadc3e837c1b"
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS
    def send(self, phone, message):
        try:
            response = self.sms.send(message, [phone])
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))