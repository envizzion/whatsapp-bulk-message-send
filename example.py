# If you DO NOT have the WhatsApp Desktop app installed
from alright import WhatsApp
from codecs import open 

messenger = WhatsApp()
# messenger.find_user('2556929069077')
messenger.find_by_username('Mydiaog')
# time.sleep(5)
# messenger.send_message('test22')
# messenger.send_message1('94789629878',"hey I'm done its tuesday ")
with open('message.txt', encoding='utf-8') as f:
    msg = f.read()
    # print(msg)
    
messenger.send_picture('image.png',msg)
input()

# If you DO have the WhatsApp Desktop app installed
# from alright import WhatsApp

# msg = "hey I'm done its tuesday"
# messenger = WhatsApp()
# messenger.send_message1('Mydiaog', msg)
