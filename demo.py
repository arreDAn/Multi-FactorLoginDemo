####################################################
#  The purpose of this program is to explore       # 
# different ways to to login while protectin the   # 
#  integrity of the system, using a password       #
#  and using a login code method.                  #
#                                                  #
#   IMPORTANT: Scince this program requieres       #
#   personal information...                        #
#   I will not provide my email or email password. #
#   To run the program one must do the fallowing   #
#   modifications to sendEmail function:           #
#    1) provide email for sender                   #
#    2) provide password for sender email.(warning #
#        this is not the password you use to login #
#        into your email. you must request an app  #
#        password under privacy setting in your    #
#        email app.)                               #
#     3. provide resiver password                  #
####################################################


import string
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#This fuction ask the user to enter an option 
def menu():
    #Display menu
    print("Select from the fallowing")
    print("1. Generate password")
    print("2. Text message loging")
    print("press any other key to exit")
    x = input("Enter option: ")
    while(x=='1' or x=='2'):
        if x == '1':
            print("You selected generate password...")
            generated_password = generatePassword()
            print("Generated Password:", generated_password)
            loginAt(generated_password)
            x = '0';
            menu()

        elif x == '2':
            print("You selected verification code login...")
            send_email()
            x = '0'
            menu()
        else:
            print("Adios")
            
    

#This funntion generates a password
def generatePassword(length=12, uppercase=True, digits=True, special_characters=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))


    return password
#This funtion generate a 5 integer string
def generate_random_integers_as_string(count=5, lower_limit = 1, upper_limit = 9 ):
    random_integers = [random.randint(lower_limit, upper_limit) for _ in range(count)]
    random_integers_string = ''.join(map(str, random_integers))
    return random_integers_string

# This funtion sends an email with the verefication code
def send_email():
    # Create the MIME object
    subject = " This is your verification code"
    body = generate_random_integers_as_string()
    yahoo_email = # replace example email with real email, must be a string "example.emal"
    app_password = # replace examplePassword with app password must be a string "examplePassword"
    # Recipient email address
    recipient_email = #replace with second email, must be aa string "examle.email"
    message = MIMEMultipart()
    message["From"] = yahoo_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Add the email body
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
        server.starttls()
        # Login with your Yahoo email and app password
        server.login(yahoo_email, app_password)
        # Send the email
        server.sendmail(yahoo_email, recipient_email, message.as_string())
    loginAt(body)

#This is an example of login 
def loginAt(Pword):
    print("Enter anything for user")
    username = input("Enter username: ") #any input will be accepted
    userPword = input("Enter password: ")
    #checks if password or verification code is correct
    if Pword == userPword:
        print("Access granted for "+username+"...")
    else:
        print("The password you enter is incorrect")


menu()
