email1 = 'mm120110@sgh.studuent.waw.pl'
email2 = 'mm120110.mir$sgh.student.waw.pl'
email3 = 'mir.moheuddin@'
email4 = '@sgh.student.waw.pl'
email5 = 'mir.moheuddin@.pl'
email6 = 'mir@moheuddin@.pl'

def check_email(email):
    if email == email1:
        return True
    elif not email2:
        return False
    elif not email3:
        return False
    elif not email4:
        return False
    elif not email5:
        return False
    else:
        return False

for em in [email1, email2, email3, email4, email5, email6]:
    print('{}: {}'.format(em, check_email(em)))

