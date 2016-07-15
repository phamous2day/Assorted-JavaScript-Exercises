# Did this exercise in 3 parts: first to encrypt the common-words into md5 passwords, second to loop through all the user passwords in acccounts.json, then third to match up the encrypted commong words with the passwords in accounts.json
import md5
import json


#chunk 1: encrypt all common words using md5 hexdigest
words = open("common_words.txt")
content_file = words.read()
content_file = content_file.split('\n')
encrypted_common_words = {}
for word in content_file:
    m = md5.new()
    m.update(word)
    encrypted_password = m.hexdigest()
    encrypted_common_words[encrypted_password] = word


#chunk 2: loop through all the passwords. Eventually, match them up with the encrypted commonn words, if they match up then print it out
leaked_passwords = open('accounts.json', 'r')
whole_file = json.loads(leaked_passwords.read())
count = 0


for individual_object in whole_file:
    password = individual_object.get('password')
    username = individual_object.get('username')
    if password in encrypted_common_words:
        count = count + 1
        print username +  ": " + encrypted_common_words[password]

print "Passwords Decrypted", count
