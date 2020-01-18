#! /usr/bin/env python3
#Phone and Email finder- Extracts phone numbers and emails from the clipboard

import pyperclip , re

# finds phone numbers

phoneregex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #finds the area code 
(\s|-|\.)? #Seporator
(\d{3}) #first three main digits
(\s|-|\.) #seporator 
(\d{4}) # last four digits 
(\s*(ext|x|ext.)\s*(\d{2,5}))? # Extensions 
)''' , re.VERBOSE)

# finds emails

emailregex = re.compile(r'''(
[a-zA-Z0-9._%\-+]+
@
[a-zA-Z0-9.\-]
(\.[a-zA-z]{2,5})
)''', re.VERBOSE)

# takes emails and phone numbers from the clipboard,
# makes them into a single standard format and puts them into a list

text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

# Copies results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clip board')
else:
    print("No phone numbers or emails were found")


