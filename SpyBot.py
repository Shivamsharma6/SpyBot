from Spy_Alpha import spy
import time
import datetime
import random

print ''
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
friends = []
secretmsg = []
chat = []
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


def start_chat():
    try:
        show_menu = True
        while show_menu:
            print '\n'
            print 'Select any of the following:'
            choices = '1.Add a status update \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read Chats from user \n6.Show your profile \n7.Terminate \n\n'
            ch = int(raw_input(choices))
            if ch == 1:
                print 'Time to update the status!'
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
                print 'Showing status updates:'
                print dili

            elif ch == 2:
                def add_frnd():
                    new_friend = dict()
                    new_friend.update({'name': raw_input('Please add your friend\'s name: '),
                                       'salutation': raw_input("Mr. or Ms.?: ").capitalize(), 'age': 0, 'rating': 0.0})
                    new_friend['name'] = new_friend['salutation'] + new_friend['name']
                    new_friend['age'] = int(raw_input("Age:"))
                    new_friend['rating'] = float(raw_input("Spy rating:"))
                    print 'Adding Friend...'
                    time.sleep(1)
                    print 'Name:', new_friend['name']
                    print 'Age:', new_friend['age']
                    print 'Rating:', new_friend['rating']
                    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['spy_rating']:
                        friends.append(new_friend)
                    else:
                        print 'Sorry! We can\'t add you because you are not eligible.'
                    return len(friends)

                add_frnd()

            elif ch == 3:
                print 'Wanna send some secret messages...!'
                time.sleep(0.8)

                def select_friend():
                    item_number = 0
                    secmsg = {
                        'pos': '',
                        'nam': '',
                        'msg': ''
                    }
                    for friend in friends:
                        print '%s aged %d with rating %.2f is online' % (friend['name'], friend['age'], friend['rating'])
                        print '%d.%s' % ((item_number + 1), friend['name'])
                        item_number = item_number + 1
                    friend_choice = int(raw_input("Choose from your friends:"))
                    secmsg['pos'] = friend_choice

                    if friend_choice == 1:
                        secmsg['nam'] = friends[0]['name']
                    elif friend_choice == 2:
                        secmsg['nam'] = friends[1]['name']
                    elif friend_choice == 3:
                        secmsg['nam'] = friends[2]['name']
                    elif friend_choice == 4:
                        secmsg['nam'] = friends[3]['name']
                    elif friend_choice == 5:
                        secmsg['nam'] = friends[4]['name']
                    elif friend_choice == 6:
                        print 'Invalid Choice!'
                    msg = raw_input('Enter your message:')
                    secmsg['msg'] = msg
                    print 'Your secret message is being sent...'
                    time.sleep(0.8)
                    secretmsg.append(secmsg)

                select_friend()

            elif ch == 4:
                def read_secmsg():
                    print 'Checking for secret messages...'
                    time.sleep(0.8)
                    for message in secretmsg:
                        print '%d secret messages has been received from ...' % (message['pos'])

                    print 'To know the names you have to verify yourself'
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = a + b
                    print 'Here\'s your 1st Number:', a
                    print 'Here\'s your 2nd Number:', b
                    summ = int(raw_input('What will be the sum?:'))
                    if summ == c:
                        print 'Successfully Authenticated!'
                        for message in secretmsg:
                            print 'A secret message has been received from %d: %s is %s' % (
                                message['pos'], message['nam'], message['msg'])
                    else:
                        print 'Access Denied'

                read_secmsg()

            elif ch == 5:
                cho = raw_input('Send or Read:')
                msg_dict = {
                    'To': '',
                    'Message': ''
                }

                def send():
                    msg_dict['To'] = raw_input('Receiver\'s Name:')
                    msg_dict['Message'] = raw_input('Enter your message:')
                    if len(msg_dict['Message']) > 0 and len(msg_dict['To']) > 0:
                        chat.append(msg_dict)
                        print chat
                    else:
                        print 'Your message is discarded.'

                def read():
                    if not chat:
                        print 'No messages in your Inbox.'
                    else:
                        print chat

                if cho.upper() == 'SEND':
                    send()
                elif cho.upper() == 'READ':
                    read()

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
