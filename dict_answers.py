aditi = {
  'name': 'Aditi',
  'email': 'aditi@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#part1
# print "Emails are: ", aditi['email']


#part2
# print "First interest is: ", aditi['interests'][0]


#part3
# print "Jasmine's email is: ", aditi["friends"][0]["email"]

#part4
# print "Jasmine's second interest is ", aditi["friends"][0]["interests"][1]




#Exercise 2 What's expected
filename = raw_input("Type out the filename: ")

#read contents of file
file = open(filename)
contents= file.read()
file.close

contents = contents.replace(',', '').replace('.', '').replace('!', '')

words = contents.split()
tally = {}

# for word in words:
#     if word in tally:
#         count = tally[word]
#         count = count +1
#         tally[word] = count
#     else:
#         tally[word] = 1
#
# print tally

#Alternative
for word in words:
    if word in tally:
        count = tally.get(word, 0)
        count = count +1
        tally[word] = count
    else:
        tally[word] = 1

print tally



#Exercise 2: My own way
# from collections import Counter
# from sys import argv
# script = argv
# import re
#
# cnt = Counter()
# words = re.findall(r'\w+', open('repeated.txt').read().lower())
# Counter(words).most_common(10)
#
# print Counter(words)
