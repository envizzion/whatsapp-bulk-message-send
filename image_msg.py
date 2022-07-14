from alright import WhatsApp
from codecs import open
from os import path
from time import sleep
msg =""
numbers =[]


if not path.exists('image.png'):
    raise Exception('No image with name image.png found')

if not path.exists('message.txt'):
    raise Exception('No message.txt file found')

if not path.exists('numbers.txt'):
    raise Exception('No numbers.txt file found')


with open('message.txt', encoding='utf-8') as f:
    msg = f.read()
    print("Found message")

if msg == None or msg == '':
    raise Exception("message is empty")

    

with open('numbers.txt') as f:
    for line in f.readlines():
        num = line.strip()
        if not num.isnumeric():
            raise Exception("non numeric number "+str(num))
        if len(num) != 11:
            raise Exception("invalid no length "+ str(len(num))+" for number "+str(num))
        if num in numbers:
            raise Exception("duplicate number "+str(num))
        numbers.append(num)        
total_nos =  len(numbers)

if total_nos == 0:
    raise Exception('No numbers found in numbers.txt')
print('--------------------------------------------------')
print('Found image.png')   
print('Found '+ str(total_nos) +' numbers for sending messages')
print('Message to be sent: '+msg)
print('---------------------------------------------------')
print()
txt = input('enter y to send first message to first number : '+str(numbers[0])+'  >')

messenger = WhatsApp()
messenger.find_user(numbers[0])
messenger.send_picture('image.png',msg)

txt = input('enter y to send message to rest of the numbers  >')
failed_numbers = []
for i,number in enumerate(numbers):
    if i == 0 :
        continue
    try:
        messenger.find_user(number)
        messenger.send_picture('image.png',msg)
        print('send message to '+ str(i)+'/'+str(total_nos) +' success')
    except Exception as e:
        print('failed sending message to: '+str(number)+' > '+str(e))
        failed_numbers.append(number)
    sleep(3)
print('----------------------------------')
print('sending messages completed')
print('Failed to send messages for '+str(len(failed_numbers))+' numbers')
print(failed_numbers)
        
# with open('message.txt') as f:
#     msg = f.read()
#     print(msg)