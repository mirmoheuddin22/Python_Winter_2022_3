import re
email1 = 'mir.moheuddin$student.sgh.waw.pl'
email2 = 'mir.moheuddin@'
email3 = 'mm120110@student.sgh.waw.pl'
email4 = '@student.sgh.waw.pl'
email5 = 'mir.moheuddin@.pl'
email6 = 'mir@moheuddin@.pl'

def check_email(email):
    path = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(path,email):
        return True
    else:
        return False

for em in [email1, email2, email3, email4, email5, email6]:
    print('{}: {}'.format(em, check_email(em)))

#for i in range(len(email4)):
    #print(email4[i])
#import re
#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#def check_email(email):
    #if (re.fullmatch(regex, email)):
        #print("Valid Email")

    #else:
        #print("Invalid Email")
#if __name__ == '__main__':
#email1 = 'mm120110@student.sgh.waw.pl'
#check_email(email1)
#email2 = 'mir.moheuddin$student.sgh.waw.pl'
#check_email(email2)
    #email3 = 'mir.moheuddin@'
    #check_email(email3)
    #email4 = '@student.sgh.waw.pl'
    #check_email(email4)
    #email5 = 'mir.moheuddin@.pl'
    #check_email(email5)
    #email6 = 'mir@moheuddin@.pl'
    #check_email(email6)
