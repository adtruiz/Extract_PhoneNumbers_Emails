#! python3
# https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-5050, 555-0000, (515)555-0505, 415 512-9568, etx. 123, x 126
(
((\d\d\d) | (\d\d\d))?   # area code (optional)
(\s|-)    # first separator
\d\d\d    # first digits
(\s|-)    # seperator
\d\d\d\d    # last 4 digits
(((etx(\.)?\s) | x) (\d{2,5})?    # extension word-part(optional)
(\d{2,5}))?    # extension number-part(optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# something@something.com

[a-zA-Z0-9_.+]+    # name part
@   # @ symbol
[a-zA-Z0-9_.+]+    # domain part


''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)