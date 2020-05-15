#! /usr/bin/env python3

# This python script checks a SHA256 hash against the HASH known for the application.
# If the Hash is not known, the opportunity is given to add the hash and the application to the dictionary.





from Hash_JSON_Data import Application_Hash_Dictionary

while True:
    print('')
    print('All hashes entered should be SHA256')
    print('')
    print('Enter hash value (press q to quit): ')
    name = input()
    if name == 'q':
        break

    if name in Application_Hash_Dictionary:
        print('This SHA256 value has been reported to represent: ' + Application_Hash_Dictionary[name])
    else:
        print('There is no application linked to ' + name)
        print('What is the name of the application linked to this SHA256 hash?')
        hash = input()
        Application_Hash_Dictionary[name] = hash
        print('SHA256 Hash database updated.')
        import json
        with open('Hash_JSON_Data.py', 'w') as f:
            f.write('Application_Hash_Dictionary = '+ json.dumps(Application_Hash_Dictionary))
