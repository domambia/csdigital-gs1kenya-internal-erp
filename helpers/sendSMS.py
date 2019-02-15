# works with both python 2 and 3
from __future__ import print_function
from datetime import datetime
import africastalking

class SMS:
    def __init__(self):
        self.username = "omambia"
        self.api_key = "4eb8662a2ecef1c54c1650179e397a3d18a591df35e00269fd48fadc3e837c1b"
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS
    def send(self, phone, message):
        print(message)
        try:
            response = self.sms.send(str(message), ["+254"+phone])
            print (response)
        except Exception as e:
            message = """
                        Dear Omambia Mogaka,
                        Re: Message Notification
                        ------------------------
                        There was an error in sending message to your other employee.
                        The Error is: {}
                        Thank You,
                            Humble Developer, Most adored,
                        GS1 Kenya
                        Date: {} .
                      
                      """
            print (message.format(str(e), datetime.now))