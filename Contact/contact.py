from datetime import datetime
contacts = {}
log = []
def addContact():
	global contacts
	global log
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
	log += [[datetime.now().isoformat(), "Added contact: Name:{}|Primary Number:{}|Secondary Number:{}".format(new_contact['name'], new_contact['pNo'], new_contact['sNo'])]]
	return contacts[new_name]

def search(): # Improve searching
	global contacts, log
	key = input("Search:")
	log += [[datetime.now().isoformat(), "Query key:{}".format(key)]]
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
			log += [[datetime.now().isoformat(), "Query result: Not found"]]
		else:
			log += [[datetime.now().isoformat(), "Query result: Name:{}|Primary Number:{}|Secondary Number:{}".format(item['name'], item['pNo'], item['sNo'])]]
			print("Contact found:")
			printContact(item)
			print()

	elif opt == 3:	# Edit a contact, after searching for it
		item = search()
		if item == dict():
			print("No such contact found")
			log += [[datetime.now().isoformat(), "Query result: Not found"]]
		else:
			log += [[datetime.now().isoformat(), "Query result: Name:{}|Primary Number:{}|Secondary Number:{}".format(item['name'], item['pNo'], item['sNo'])]]
			print("Contact found:")
			printContact(item)
			del contacts[item['name']]
			log += [[datetime.now().isoformat(), "Deleted contact: Name:{}|Primary Number:{}|Secondary Number:{}".format(item['name'], item['pNo'], item['sNo'])]]
			addContact()
			print("Contact updated\n")

	elif opt == 4:	# Delete a contact after searching for it
		item = search()
		if item == dict():
			log += [[datetime.now().isoformat(), "Query result (deletion): Not found"]]
			print("No such contact found")
		else:
			print("Contact found:")
			printContact(item)
			opt3 = input("Delete?(y/n)")
			if opt3 == 'y':
				del contacts[item['name']]
				print("Contact deleted\n")
				log += [[datetime.now().isoformat(), "Deleted contact: Name:{}|Primary Number:{}|Secondary Number:{}".format(item['name'], item['pNo'], item['sNo'])]]

	elif opt == 5:	# Display all contacts
		print("Total contacts:", len(contacts))
		j = 1
		for contactKey in contacts.keys():
			print("Contact", j, ":")
			printContact(contacts[contactKey])
			print("----------")
			j += 1
		log += [[datetime.now().isoformat(), "Printed all contacts"]]
		print()

	elif opt == 6:	# End application
		print("Contact application terminated")
		for i in log:
			print("{:30}{}".format(i[0], i[1]))	
		break	
