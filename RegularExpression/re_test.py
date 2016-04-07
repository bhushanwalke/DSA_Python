import re

phoneregex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

res = phoneregex.search('My number is 415-555-4242 415-555-4243.')

areacode, mainNum, lastNum = res.groups()
print areacode, mainNum, lastNum



phoneregex1 = re.compile(r'(\(\d{3}\)) (\d{3})-(\d{4})')

res1 = phoneregex1.search('My number is (415) 555-4242 415-555-4243.')

areacode, mainNum, lastNum = res1.groups()
print areacode, mainNum, lastNum



heroregex = re.compile(r'Batman|Superman')

hero = heroregex.search("Superman VS Batman")
print hero.group()

# hero1 = heroregex.search("Superman VS Batman")
# print hero1.group()


phoneregex = re.compile(r'(\d{3}) (\d{3})-(\d{4})')
res = phoneregex.findall('My number is (415) 555-4242 415 555-4243')
print res[0]

phoneregex = re.compile(r'\(?\d{3}\)? \d{3}-\d{4}')
res = phoneregex.findall('My number is (415) 555-4242 415 555-4243')
print res

roboregex = re.compile(r'[^aeiou ]')
robo = roboregex.findall('Robocop eats baby food.')
print robo

xmsregex = re.compile(r'[\d]+\s\w+')
xms = xmsregex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print xms

beginregex = re.compile('^Hello')
begin = beginregex.search(r'Hello World')
print begin

endregex = re.compile(r'\d+$')
end = endregex.findall('Hello 007')
print end