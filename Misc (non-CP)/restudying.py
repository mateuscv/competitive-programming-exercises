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

# Shorthand character classes:
# \d -- digits, \w -- letters, digits or underscores, \s -- spaces, tabs, newlines
# every one of those has a capital letter counterpart (e.g. \D) that denotes its opposite.
print()

lyrics = "12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree"
lyrRegex = re.compile('\d+\s\w+')
lyrList = lyrRegex.findall(lyrics)
print(lyrList)

# Custom character classes:
print()

vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u|A|E|I|O|U)'

# OR

vowelRegex = re.compile(r'[aeiou]', re.I) # re.I --> IGNORECASE
print(vowelRegex.findall('Oloco bixo! Quem sabe faz ao vivo!'))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Oloco bixo! Quem sabe faz ao vivo!'))

# Negative:
nonVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(nonVowelRegex.findall('Oloco bixo! Quem sabe faz ao vivo!'))

# ^ on non-custom -- only matches strings which begin with regex pattern.
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said hello there!'))

# $ at the end -- only matches strings which end with the regex pattern.
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search("Hello world!"))
print(endsWithWorldRegex.search("Hello world!assd"))

print()

# using both -- the entire string must match the pattern

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('45542155546'))
print(allDigitsRegex.search('4554a2155546'))

# The dot -- any single character except newline
print()

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat')) #notice the spaces in output

# Dot-star:
print()

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall("First Name: Al Last Name: Sweigart"))

# greedily and non:
serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

# With newline:
print()

prime = 'Serve.\nProtect.\nUpload.'
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())