import csv
import sys

csvFile = open('export.csv', 'w')
csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_MINIMAL)
csvWriter.writerow(['title', 'username', 'password', 'notes'])

importSocket = open(sys.argv[1], 'r')
importFile = importSocket.readlines()
importSocket.close()

# Concatenate strings
myList = []
temp = ''

for line in importFile:
    if line != '\n':
        temp = temp + line
    elif temp != '':
        myList.append(temp)
        temp = ''
if temp != '':
    myList.append(temp)

# Create entry
def constructLine(splittedItem):
    entry = []
    notes = ''
    withoutUsername = True
    withoutPassword = True
    usernameAsEmail = False

    # Try to find `Username`
    for line in splittedItem:
        if line.startswith('Username'):
            withoutUsername = False
            entry.append(line.replace('Username ', ''))
    # If there is no `Username` field — try to find `E-Mail` and use it as `Username`
    if withoutUsername:
        for line in splittedItem:
            if (line.startswith('E-Mail') or line.startswith('Email') or line.startswith('E-mail')):
                withoutUsername = False
                usernameAsEmail = True
                entry.append(line.replace('E-Mail ', '').replace('Email ', '').replace('E-mail', ''))
    # If there is no `E-Mail` — field is filled with `none`
    if withoutUsername:
        entry.append('none')
    # Try to find `Password`
    for line in splittedItem:
        if line.startswith('Password'):
            withoutPassword = False
            entry.append(line.replace('Password ', ''))
    # If there is no `Password` — field is filled with `none`
    if withoutPassword:
        entry.append('none')
    # Everything else goes to `notes` section
    for line in splittedItem:
        if (not line.startswith('Password') and not line.startswith('Username')) and not ((line.startswith('E-Mail') or line.startswith('Email') or line.startswith('E-mail')) and usernameAsEmail):
            notes += line.replace('Url ', '').replace('E-Mail ', '').replace('Email ', '').replace('E-mail', '')
    entry.append(notes)
    return entry

# Iterate array, close file
for item in myList:
    splittedItem = item.split('\n')
    # First entry always a name
    name = splittedItem.pop(0)
    csvWriter.writerow([name] + constructLine(splittedItem))

csvFile.close()
