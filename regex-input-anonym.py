import re
user_input=input('write your text: \n')
def anonym_mail():
    global substitute
    email_pattern="[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{,3}"
    substitute=re.sub(email_pattern,'*email*',user_input)
    
def anonym_phone():
    global substitute
    phone_pattern="\+?\d{10,15}"
    substitute=re.sub(phone_pattern,'*phone*',substitute)
    
with open('anonym.txt','a') as file:
    anonym_mail()
    anonym_phone()
    print(f'the anonymized version of your text: \n {substitute}')
    file_write=input("would you like to save this (y/n): \n")
    if file_write=='y':
        file.write(substitute+'\n')
    else:
        pass
