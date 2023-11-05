contacts = [
    {
        "name": "Jamil",
        "surname": "Xametov",
        "number": "+994559992233"
    },
    {
        "name": "Murad",
        "surname": "Agazada",
        "number": "+9945590002233"
    },
    {
        "name": "Camal",
        "surname": "Damarov",
        "number": "+9945587952233"
    },
    {
        "name": "Famal",
        "surname": "Geras",
        "number": "+994557653768354733"
    },
    {
        "name": "Famil",
        "surname": "Ramanov",
        "number": "+9945590078353"
    },
    {
        "name": "Cavad",
        "surname": "Ramaman",
        "number": "+9945583958233"
    },
]

def add_contact(name, surname, number):
    name=name.title();surname=surname.title()
    contacts.append({'name': name, 'surname': surname, 'number': number})
    return f'Contact {name} {surname} added.'

def all_contact():
    print('')
    for i in contacts:
        print(i["name"],i["surname"],i["number"])

def contact_by_number(number):
    hello=0;number=number
    for person in contacts:
        if person['number']==number:
            hello=1
            return f'Contacts with number {number}:\n{person["name"]} {person["surname"]}, {person["number"]}'
    if hello==0: return f'No contacts with number {number} found'

def delete_contact(name):
    name=name.title()
    da=0
    for i in contacts:
        if i['name']==name:
            da=1
            contacts.remove(i)
            return "delete"
    if da==0: return f'No contacts with name {name} found'

def edit_contact(name, new_name, new_surname, new_number):
    name=name.title();div=0
    for person in contacts:
        if person['name']==name:
            div=1
            contacts[contacts.index(person)]={'name':new_name,'surname':new_surname,'number':new_number}
            return 'edited'
    if div!=1: return f'Error 404: Contact not found. Error 911: You are Invalid'

def call_contact(name):
    name=name.title();div=0
    for person in contacts:
        if person['name']==name:
            div=1
            return f"Calling {person['name']},{person['surname']},{person['number']}"
    if div!=1: return f'Error 404: Contact not found. Error 911: You are Invalid'

while True:
    all_contact()
    operation=input('What do you want to do? (add, delete, call, find, edit, quit)\n')
    if operation=='quit': print('Byebye');break
    elif operation=='add': print(add_contact(input('Enter name: '), input('Enter surname: '), input('Enter number: ')))
    elif operation=='delete': print(delete_contact(input('Which contact do you want do delete? (enter name)\n')))
    elif operation=='find': print(contact_by_number(input('Enter contact number: ')))
    elif operation=='edit': print(edit_contact(input('Which contact do you want to edit?\n'),input('Enter new contact name: '), input('Enter new contact surname'), input('Enter new contact number: ')))
    elif operation=='call': print(call_contact(input("Enter name: ")))