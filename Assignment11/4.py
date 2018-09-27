def get_emails():
    email_list = []
    user_input = ""
    while user_input != "q":
        user_input = input("Email address: ")
        if user_input != "q":
            email_list.append(user_input)
    return email_list

def get_names_and_domains(email_list):
    templist = []
    temptuple = ()
    for i in email_list:
        temptuple = tuple(i.split('@'))
        templist.append(temptuple)
    return templist
# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)