# To access Steganography library.
from steganography.steganography import Steganography
# All basic class and list is imported from spy_info file.
from spy_info import spy, Spy, ChatMessage, friends
# randint function has been imported from random library
from random import randint
import time
import datetime
# For attractive console
print ''
print ''
print ''
print 'Taking u all to the era of 70s'
print '|*****************************|'
print '*'
print '*'
print '*'
print '*'
print '*'
print 'Moon Techs'
print 'Welcomes you to the Future!'
print '*'
print '*'
print '*'
print '*'
print '*'
print '*'
print '|*****************************|'
print ''
print 'Featuring the most advanced A.I spy of our time!'
print 'Heyy'
dili = []
secretmsg = []
chat = []
# Simple conversation with user
gender = raw_input('Male or Female:')
if gender.upper() == 'MALE' or gender.upper() == 'M':
    name = raw_input("Enter your name:")
    if name.isalpha():
        print ''
        time.sleep(0.5)
        print 'I am a Spy'
        print 'Just for folks!!!'
        print ''
        print 'Welcome'
        marital = raw_input('Married or not? \n')
        print 'Okay!'
        print ''
        if marital.upper() == 'YES' or marital.upper() == 'MARRIED':
            salutation = 'Mr.'
            marital = 'Married'
            print salutation + name
        elif marital.upper() == 'NO' or marital.upper() == 'NOT MARRIED' or marital.upper() == 'NOT':
            marital = 'Not Married'
            salutation = 'Mr.'
            print salutation + name
        else:
            print 'Wrong Input!'
            print 'Enter only one input among these two:'
            marital = raw_input('Married or Not Married? \n')
            if marital.upper() == 'MARRIED':
                salutation = 'Mr.'
                marital = 'Married'
                print salutation + name
            elif marital.upper() == 'NOT MARRIED':
                salutation = 'Mr.'
                marital = 'Not Married'
                print salutation + name

        print 'Alright,I would like to know a little more about you...'
        age = 0
        try:
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old
        except ValueError:
            print 'Enter a numeric value.'
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old

    else:
        print 'Enter alphabetic characters'
        name = raw_input("Enter your name:")
        print ''
        time.sleep(0.5)
        print 'I am a Spy'
        print 'Just for folks!!!'
        print ''
        print 'Welcome'
        marital = raw_input('Married or not? \n')
        print 'Okay!'
        print ''
        if marital.upper() == 'YES' or marital.upper() == 'MARRIED':
            salutation = 'Mr.'
            marital = 'Married'
            print salutation + name
        elif marital.upper() == 'NO' or marital.upper() == 'NOT MARRIED' or marital.upper() == 'NOT':
            marital = 'Not Married'
            salutation = 'Mr.'
            print salutation + name
        else:
            print 'Wrong Input!'
            print 'Enter only one input among these two:'
            marital = raw_input('Married or Not Married? \n')
            if marital.upper() == 'MARRIED':
                salutation = 'Mr.'
                marital = 'Married'
                print salutation + name
            elif marital.upper() == 'NOT MARRIED':
                salutation = 'Mr.'
                marital = 'Not Married'
                print salutation + name

        print 'Alright,I would like to know a little more about you...'
        age = 0
        try:
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old
        except ValueError:
            print 'Enter a numeric value.'
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old

elif gender.upper() == 'FEMALE' or gender.upper() == 'F':
    name = raw_input("Enter your name:")
    if name.isalpha():
        print ''
        time.sleep(0.5)
        print 'I am a Spy'
        print 'Just for folks!!!'
        print ''
        print 'Welcome'
        marital = raw_input('Married or not ? \n')
        print 'Okay!'
        print ''
        if marital.upper() == 'YES' or marital.upper() == 'MARRIED':
            salutation = 'Mrs.'
            marital = 'Married'
            print salutation + name
        elif marital.upper() == 'NO' or marital.upper() == 'NOT MARRIED' or marital.upper() == 'NOT':
            salutation = 'Miss.'
            marital = 'Not Married'
            print salutation + name
        else:
            print 'Invalid Input!'
            print 'Enter only one input among these two:'
            marital = raw_input('Married or Not Married? \n')
            if marital.upper() == 'MARRIED':
                salutation = 'Mr.'
                marital = 'Married'
                print salutation + name
            elif marital.upper() == 'NOT MARRIED':
                salutation = 'Mr.'
                marital = 'Not Married'
                print salutation + name

        print 'Alright,I would like to know a little more about you...'
        age = 0
        try:
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old
        except ValueError:
            print 'Enter a numeric value.'
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old

    else:
        print 'Enter alphabetic characters'
        name = raw_input("Enter your name:")
        print ''
        time.sleep(0.5)
        print 'I am a Spy'
        print 'Just for folks!!!'
        print ''
        print 'Welcome'
        marital = raw_input('Married or not ? \n')
        print 'Okay!'
        print ''
        if marital.upper() == 'YES' or marital.upper() == 'MARRIED':
            salutation = 'Mrs.'
            marital = 'Married'
            print salutation + name
        elif marital.upper() == 'NO' or marital.upper() == 'NOT MARRIED' or marital.upper() == 'NOT':
            salutation = 'Miss.'
            marital = 'Not Married'
            print salutation + name
        else:
            print 'Invalid Input!'
            print 'Enter only one input among these two:'
            marital = raw_input('Married or Not Married? \n')
            if marital.upper() == 'MARRIED':
                salutation = 'Mr.'
                marital = 'Married'
                print salutation + name
            elif marital.upper() == 'NOT MARRIED':
                salutation = 'Mr.'
                marital = 'Not Married'
                print salutation + name

        print 'Alright,I would like to know a little more about you...'
        age = 0
        try:
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old
        except ValueError:
            print 'Enter a numeric value.'
            age = raw_input('Enter you age:')
            age *= 1
            year = datetime.date.today().year - int(age)
            print 'So lemme guess...'
            time.sleep(1)
            print 'You were born in:', year
            age = int(age)
            if age < 100:
                old = 100 + int(year)
                print 'You will be 100 years old in:', old
            else:
                old = 100 + int(year)
                print 'You were 100 years older in:', old

else:
    print 'Sorry! I can\'t help you out...'
    salutation = ''
    name = ''
    age = ''
    marital = ''

time.sleep(1)
status = 'Not updated yet!'


# A function to add new friend.
def add_frnd():
    new_friend = Spy('', '', 0, 0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = int(raw_input("Age?"))
    new_friend.rating = float(raw_input("Spy rating?"))
    print 'Adding Friend...'
    time.sleep(1)
    print 'Name:', new_friend.name
    print 'Age:', new_friend.age
    print 'Rating:', new_friend.rating
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! We can\'t add you because you are not eligible.'
    return len(friends)


# A function to select among online friends.
def select_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number+1, friend.salutation, friend.name, friend.age, friend.rating)
        item_number = item_number + 1
    try:
        friend_choice = int(raw_input("Choose from your friends:"))
        friend_choice_position = friend_choice - 1
        return friend_choice_position
    except ValueError:
        print 'Wrong Input'
        print 'Enter the position in numerals'


# Function to encrypt message inside an image file.
def send_message():
    frnd = select_friend()
    original_image = raw_input('Name of image:')
    output_image = raw_input('Name of output image:')
    text = raw_input('Enter your message:')
    # Encryption of image:
    Steganography.encode(original_image, output_image, text)
    new_chat = ChatMessage(text, True)
    friends[frnd].chats.append(new_chat)
    print "Your secret message image is ready!"


# Function to read encrypted message encoded inside an image file.
def read_message():
    frnd = select_friend()
    output_path = raw_input('Name of image which contains secret message:')
    # Decryption of encrypted image
    secret_text = Steganography.decode(output_path)
    print 'This is your message:'
    print secret_text
    new_chat = ChatMessage(secret_text, False)
    friends[frnd].chats.append(new_chat)
    print "Your secret message has been saved!"


# Function to read chat messages from the users.
def read_chat():
    read_for = select_friend()
    try:
        for chat in friends[read_for].chats:
            if chat.sent_by_me:
                print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
            else:
                print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)
    except AttributeError:
        print 'No previous messages.'


# Function to start Menu which will call other functions required to perform their respective tasks.
def start_chat():
    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + 'It is good to see you.'
    try:
        show_menu = True
        while show_menu:
            print '\n'
            print 'Select any of the following:'
            choices = '1.Add a status update \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read Chats from user \n6.Show your profile \n7.Terminate \n\n'
            ch = int(raw_input(choices))
            if ch == 1:
                print 'Time to update the status!'
                print 'Wanna update from your previous updates'
                u = raw_input('Yes or No:')
                if u.upper() == 'NO':
                    dic = dict()
                    dic.update({'Status': '', 'Time': ''})
                    dic['Status'] = raw_input('Enter your status:')
                    dic['Time'] = time.strftime("%H:%M:%S")
                    if len(dic['Status']) > 0:
                        dili.append(dic)
                        print 'Updating...'
                        time.sleep(0.8)
                        print 'Status updated!'
                    else:
                        print 'You haven\'t entered anything.'
                elif u.upper() == 'YES':
                    if len(dili) < 0:
                        print 'No previous updates found'
                    else:
                        print dili
                        t = int(raw_input('Enter its position'))
                        t += 1
                print 'Showing status updates:'
                print dili

            elif ch == 2:
                frnd_num = add_frnd()
                print 'You have %d friends' % frnd_num
                add_frnd()

            elif ch == 3:
                print 'Wanna send some secret messages...!'
                time.sleep(0.8)
                send_message()

                # Another way:
                # def select_friend():
                #     item_number = 0
                #     secmsg = {
                #         'pos': '',
                #         'nam': '',
                #         'msg': ''
                #     }
                #     for friend in friends:
                #         print '%s aged %d with rating %.2f is online' % (friend['name'], friend['age'], friend['rating'])
                #         print '%d.%s' % ((item_number + 1), friend['name'])
                #         item_number = item_number + 1
                #     friend_choice = int(raw_input("Choose from your friends:"))
                #     secmsg['pos'] = friend_choice
                #
                #     if friend_choice == 1:
                #         secmsg['nam'] = friends[0]['name']
                #     elif friend_choice == 2:
                #         secmsg['nam'] = friends[1]['name']
                #     elif friend_choice == 3:
                #         secmsg['nam'] = friends[2]['name']
                #     elif friend_choice == 4:
                #         secmsg['nam'] = friends[3]['name']
                #     elif friend_choice == 5:
                #         secmsg['nam'] = friends[4]['name']
                #     elif friend_choice == 6:
                #         print 'Invalid Choice!'
                #     msg = raw_input('Enter your message:')
                #     secmsg['msg'] = msg
                #     print 'Your secret message is being sent...'
                #     time.sleep(0.8)
                #     secretmsg.append(secmsg)
                #
                # select_friend()


            elif ch == 4:
                print 'To proceed further you have to prove yourself:'
                a = randint(1, 11)
                b = randint(1, 11)
                r = 0
                print '%s+%s' % (str(a), str(b))
                c = a+b
                try:
                    r = int(raw_input('What will be the sum?\n'))
                except ValueError:
                    print 'Wrong Input!'
                    print 'Enter the sum only.'

                if c == r:
                    print 'Access Granted!'
                    read_message()
                else:
                    print 'Access Denied!'
                    print 'Program Terminating!!!'
                    show_menu = False

            elif ch == 5:
                read_chat()

                # Another way:
                # cho = raw_input('Send or Read:')
                # msg_dict = {
                #     'To': '',
                #     'Message': ''
                # }
                #
                # def send():
                #     msg_dict['To'] = raw_input('Receiver\'s Name:')
                #     msg_dict['Message'] = raw_input('Enter your message:')
                #     if len(msg_dict['Message']) > 0 and len(msg_dict['To']) > 0:
                #         chat.append(msg_dict)
                #         print chat
                #     else:
                #         print 'Your message is discarded.'
                #
                # def read():
                #     if not chat:
                #         print 'No messages in your Inbox.'
                #     else:
                #         print chat
                #
                # if cho.upper() == 'SEND':
                #     send()
                # elif cho.upper() == 'READ':
                #     read()

            elif ch == 6:
                if len(name) > 0:
                    print ''
                    print 'Your Profile:'
                    print 'Name:', salutation + name
                    print 'Age:', age
                    print 'Marital Status:', marital
                else:
                    print 'No credentials entered.'

            elif ch == 7:
                show_menu = False
                print 'Terminating...'
                time.sleep(0.8)

    except ValueError:
        print 'Invalid Choice!'
        print 'Enter your choice as shown.'
        start_chat()


start_chat()
# End of the code.