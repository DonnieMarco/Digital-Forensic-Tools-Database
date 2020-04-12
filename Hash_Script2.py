#! /usr/bin/env python3

#This python script checks a SHA256 hash against the HASH known for the application.
#IF the Hash is not known, the opportunity is given to add the hash and the application to the dictionary.



#Application_Hash_Dictionary  = {'51ea006fac7c7cf88dda19133fd2e701d53a774d0f9a6f094178db40424e2bd1': 'Notepad++ 7.8.1', 'd713c41ed85b4fcad4a810ba46e9a7753b0e6e49ec88cf81138d03f89d2b5814': 'Kali Linux 2019.1', '6789cdd2054bccb1d623d0ff32e4246d4d4c49c21cec85a7d1ea5922b5075a55': 'HandBrake-1.3.0.dmg'}

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
