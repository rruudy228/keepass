from pykeepass import PyKeePass, create_database

kp = create_database ('newDb.kdbx', password='s3cr3t', keyfile=None, transformed_key=None)

group = kp.add_group(kp.root_group, 'email')

entry = kp.add_entry(group, 'gmail', 'myusername', 'myPassw0rdXX')
print(entry)  

kp.save()
