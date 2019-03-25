# works with both python 2 and 3
from __future__ import print_function
from datetime import datetime
import africastalking

class SMS:
    def __init__(self):
        self.username = "gs1kenya"
        self.api_key = "0902d36a02514da9fa33a11586683f8d76e5207ea544363e7d41149e6c9a6718"
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS
    def send(self, phone, message):
        try:
            response = self.sms.send(str(message), ["+254"+str(phone)])
        except Exception as e:
            message = """
                        Dear, Omambia Mogaka.
                        Ref: Message Notification
                        ------------------------
                        There was an error in sending message to your other employee.
                        The Error is: {}
                        Thank You,
                            Humble Developer, Most adored,
                        GS1 Kenya
                        Date: {} .
                      """
            print (message.format(str(e), datetime.now))
