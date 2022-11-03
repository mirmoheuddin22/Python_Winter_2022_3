email1 = 'mm120110@student.sgh.waw.pl'
email2 = 'mir.moheuddin$student.sgh.waw.pl'
email3 = 'mir.moheuddin@'
email4 = '@student.sgh.waw.pl'
email5 = 'mir.moheuddin@.pl'
email6 = 'mir@moheuddin@.pl'


def check_email(email):
    #TODO implement all checks here
    if email:
        return True
    else:
        return False


for em in [email1, email2, email3, email4, email5, email6]:
    print('{}: {}'.format(em, check_email(em)))

for i in range(len(email4)):
    print(email4[i])