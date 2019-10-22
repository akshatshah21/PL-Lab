import datetime
contacts = {}

def addContact():
	global contacts
	new_name = input("Name:")
	new_pNo = int(input("Primary Number:"))
	s_opt = input("Add Secondary Number?(y/n)")
	new_sNo = None
	if s_opt == 'y':
		new_sNo = int(input("Secondary Number:"))
	new_contact = dict()
	new_contact['name'] = new_name
	new_contact['pNo'] = new_pNo
	new_contact['sNo'] = new_sNo
	contacts[new_name] = new_contact

def search():
	global contacts
	key = input("Search:")
	item = dict()
	for name in contacts.keys():
		if key in name:
			item = contacts[name]
			break
	return item

def printContact(contact):
	print("Name", contact['name'])
	print("Primary Number:", contact['pNo'])
	print("Secondary Number:", contact['sNo'])

while True:
	opt = int(input("1. Add Contact\t2. Search\t3. Edit Contact\n4. Delete Contact\t5. View all\t6. Exit\n"))
	if opt == 1:		# Add new contact
		print("Add contact:")
		addContact()
		print("Contact added\n")

	elif opt == 2:	# Search for a contact. Currently returns first result when searching key as prefix of name
		item = search()
		if item == dict():
			print("No such contact found")
		else:
			print("Contact found:")
			printContact(item)
			print()

	elif opt == 3:	# Edit a contact, after searching for it
		item = search()
		if item == dict():
			print("No such contact found")
		else:
			print("Contact found:")
			printContact(item)
			del contacts[item['name']]
			addContact()
			print("Contact updated\n")

	elif opt == 4:	# Delete a contact after searching for it
		item = search()
		if item == dict():
			print("No such contact found")
		else:
			print("Contact found:")
			printContact(item)
			opt3 = input("Delete?(y/n)")
			if opt3 == 'y':
				del contacts[item['name']]
				print("Contact deleted\n")

	elif opt == 5:	# Display all contacts
		print("Total contacts:", len(contacts))
		j = 1
		for contactKey in contacts.keys():
			print("Contact", j, ":")
			printContact(contacts[contactKey])
			print("----------")
			j += 1
		print()

	elif opt == 6:	# End application
		print("Contact application terminated")
		break