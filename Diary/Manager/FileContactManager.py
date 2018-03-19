import json

class FileContactManager:

	FILE_NAME='contact.txt'


	def add(self, contact):

		contacts = []
		if not self.is_empty_file():
			contacts = self.read_all()

		file = open(self.FILE_NAME, 'a+')
		contacts.append(json.dumps(contact))
		file.write(json.dumps(contacts))
		file.close()


	def read_all(self):
		file = open(self.FILE_NAME, 'r+')
		print file
		contacts = json.loads(file.read())
		print contacts
		file.close()
		return contacts


	def read(self, contact_id):
		file = open(self.FILE_NAME, 'r+')
		file.close()


	def delete(self, contact_id):
		file = open(self.FILE_NAME, 'w+')
		file.close()


	def is_empty_file(self):
		import os
		return os.stat(self.FILE_NAME).st_size == 0
