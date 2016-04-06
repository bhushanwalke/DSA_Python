import re

phoneregex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

res = phoneregex.search('My number is 415-555-4242 415-555-4243.')

areacode, mainNum, lastNum = res.groups()
print areacode, mainNum, lastNum



phoneregex1 = re.compile(r'(\(\d{3}\)) (\d{3})-(\d{4})')

res1 = phoneregex1.search('My number is (415) 555-4242 415-555-4243.')

areacode, mainNum, lastNum = res1.groups()
print areacode, mainNum, lastNum



heroregex = re.compile(r'Batman | Superman')

hero = heroregex.search("Superman VS Batman")
print hero.group()

# hero1 = heroregex.search("Superman VS Batman")
# print hero1.group()
