from Spy_Alpha import spy
import time ;
import datetime ;
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
print ''
print 'Featuring the most advanced A.I spy of our time!'
print 'Heyy'
global friends
friends=[]
gender=raw_input('Male or Female:')
if ((gender.upper()=='MALE') or (gender.upper()=='M')):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.5)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    marital=raw_input('Married or not? \n')
    if marital=='Married':
        salutation='Mr.'
        print salutation+name
    else:
        marital = 'Not Married'
        salutation='Mr.'
        print salutation+name
    print '\n Alright,I would like to know a little more about you...'
    age=raw_input('Enter you age:')

    while(age.isalpha()):
        print 'Enter a numeric value'
        age=(raw_input('Enter your age:'))

    year = datetime.date.today().year-int(age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:',year
    age=int(age)
    if age<100:
        old=100+int(year)
        print 'You will be 100 years old in:',old
    else:
        old=100+int(year)
        print 'You were 100 years older in:',old

elif ((gender.upper()=='FEMALE') or (gender.upper()=='F')):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.5)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    marital=raw_input('Married or not ? \n')
    if ((marital.upper()=='YES') or (marital.upper()=='MARRIED')):
        salutation='Mrs.'
        print salutation+name
    else:
        salutation='Miss.'
        marital='Not Married'
        print salutation + name
    print '\n Alright,I would like to know a little more about you...'
    age = raw_input('Enter you age:')

    while (age.isalpha()):
        print 'Enter a numeric value'
        age = (raw_input('Enter your age:'))

    year = datetime.date.today().year - int(age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:', year
    age=int(age)
    if age < 100:
        old = 100 + int(year)
        print 'You will be 100 years old in:', old
    else:
        old = 100 + int(year)
        print 'You were 100 years older in:', old

else:
    print 'Sorry! I can\'t help you out...'

time.sleep(1)
status='Not updated yet!'
def start_chat():
    global status
    show_menu=True
    while show_menu:
        print '\n'
        print 'Select any of the following:'
        choices='1.Add a status update \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read Chats from user \n6.Show your profile \n7.Terminate \n\n'
        ch=int(raw_input(choices))
        if ch==1:
            print 'Time to update the status!'
            pos=1
            status=raw_input('Enter your status:')
            pos+=pos
            list=[]
            for i in list:
                list.append(status)
            print 'Updated Status:',status
            print 'Showing previous status updates'
            for j in range(len(list)):
                print list[j]
        elif ch==2:
            def add_frnd():
                new_friend={
                    'name':'',
                    'salutation':'',
                    'age':0,
                    'rating':0.0
                }
                new_friend['name'] = raw_input("Please add your friend's name: ")
                new_friend['salutation'] = raw_input("Mr. or Ms.?: ").capitalize()
                new_friend['name'] = new_friend['salutation']  + new_friend['name']
                new_friend['age'] = int(raw_input("Age:"))
                new_friend['rating'] = float(raw_input("Spy rating:"))
                print 'Adding Friend...'
                time.sleep(1)
                print 'Name:',new_friend['name']
                print 'Age:', new_friend['age']
                print 'Rating:',new_friend['rating']
                if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['spy_rating']:
                    friends.append(new_friend)
                    print friends
                else:
                    print 'Sorry! We can\'t add you because you are not eligible.'
                return len(friends)
            add_frnd()

        elif ch==3:
            print 'Wanna send some secret messages...!'
            time.sleep(0.8)

            def select_friend():
                global item_number
                item_number=0
                for friend in friends:
                    print '%s aged %d with rating %.2f is online' % (friend['name'], friend['age'], friend['rating'])
                    print '%d.%s' % ((item_number + 1), friend['name'])
                    item_number = item_number + 1
                friend_choice = raw_input("Choose from your friends")
                friend_choice_position = int(friend_choice) - 1
                return friend_choice_position
            select_friend()

        elif ch==4:
            print 'Under Development'
        elif ch==5:
            print 'Under Development'
        elif ch==6:
            print ''
            print 'Your Profile:'
            print 'Name:',salutation+name
            print 'Age:',age
            print 'Marital Status:',marital
            print 'Status: \n',status
        elif ch==7:
            show_menu =False
            print 'Terminating...'
            time.sleep(0.7)
            print 'Eventually Terminated'

start_chat()