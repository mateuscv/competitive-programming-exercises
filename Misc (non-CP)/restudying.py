import re

# The very basics -- american phone number example

myRegexString = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = myRegexString.search('My number: 123-456-7890, not 123-456-7884. No end eight. Call me later.') # will find only the first occurrence, RETURNS None OTHERWISE
print(matchObject.group())

matchesList = myRegexString.findall('My number: 123-456-7890, not 123-456-7884. No end eight. Call me later.') # finds all occurrences
print(matchesList)

# Groups:
print()

brNumberRegexGrouped = re.compile(r'(\(\d\d\)) (\d\d\d\d\d-\d\d\d\d)')
matchObject = brNumberRegexGrouped.search('Meu número é (55) 99999-9999')
print(matchObject.group()) # the whole number
print(matchObject.group(1)) # only group 1 --> the number prefix
print(matchObject.group(2)) # only group 2 --> the actual phone number

# The | character (pipe):
print()

myRegexString = re.compile(r'Bat(man|mobile|cave)') # group the possible variations separated by pipes
mo = myRegexString.search('Batmobile is a nice car in a nice Batcave, belonging to Batman.')
print(mo.group())
print(mo.group(1))
ml = myRegexString.findall('Batmobile is a nice car in a nice Batcave, belonging to Batman.')
print(ml)

# The ? character: -- optional groups
print()

myRegexString = re.compile(r'Bat(wo)?man')
mo = myRegexString.search('Batwoman.')
print(mo.group())
mo = myRegexString.search('Batman.')
print(mo.group())

myRegexString = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # area code optional
mo = myRegexString.search("My number is 458-458-8484")
print(mo.group())
mo = myRegexString.search("My number is 458-8484")
print(mo.group())

# The * character: -- groups can appear zero or more times
print()

myRegexString = re.compile(r'Bat(wo)*man')
mo = myRegexString.search('Batwoman.')
print(mo.group())
mo = myRegexString.search('Batman.')
print(mo.group())
mo = myRegexString.search('Batwowowowoman.')
print(mo.group())

# The + character: -- groups can appear one or more times
print()

myRegexString = re.compile(r'Bat(wo)+man')
mo = myRegexString.search('Batwowoman.')
print(mo.group())
mo = myRegexString.search('Batman.')
print(mo) # No match -- "wo" must appear at least once!

# Specific number of appearances:
print()

myRegexString = re.compile(r'(Ha){3}')
mo = myRegexString.search('HaHaHa')
print(mo.group())

myRegexString = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
mo = myRegexString.search("My numbers are 451-431-5304, 657-8975, 123-456-7890.")
print(mo)
print(mo.group())

myRegexString = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3,5}') # leave 2nd number blank for infinity as max
mo = myRegexString.search("My numbers are 451-431-5304, 657-8975, 123-456-7890, 456-897-5656.")
print(mo.group())