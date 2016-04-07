import re

phoneregex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

res = phoneregex.search('My number is 415-555-4242 415-555-4243.')

areacode, mainNum, lastNum = res.groups()
print areacode, mainNum, lastNum



phoneregex1 = re.compile(r'(\(\d{3}\)) (\d{3})-(\d{4})')

res1 = phoneregex1.search('My number is (415) 555-4242 (415) 555-4243.')

areacode, mainNum, lastNum = res1.groups()
print areacode, mainNum, lastNum



heroregex = re.compile(r'Batman|Superman')
<<<<<<< HEAD
=======
hero = heroregex.search('Superman VS Batman')
print(hero.group())
>>>>>>> 71b8dc35df562592620ab0c7e4b33b87d739eedf

hero1 = heroregex.search("Batman VS Superman")
print hero1.group()

<<<<<<< HEAD
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
=======

batregex = re.compile(r'Bat(man|mobile|bat)')
bat = batregex.search('Batmobile Batbat lost a wheel')
print bat.groups()


batregex = re.compile(r'Bat(wo)?man')
bat = batregex.search('The Adventures of Batman')
print bat.group()
bat = batregex.search('The Adventures of Batwoman')
print bat.group()


phoneregex = re.compile(r'\(?\d{3}\)?-\d{3}-\d{4}')
phone = phoneregex.search('My number is 415-555-4242')
print(phone.group())

batregex = re.compile(r'Bat(wo)*man')
bat = batregex.search('The Adventures of Batman')
print bat.group()
bat = batregex.search('The Adventures of Batwowowoman')
print bat.group()

batregex = re.compile(r'Bat(wo)+man')
bat = batregex.search('Batwoman')
print(bat.group())
bat = batregex.search('Batman')
print(bat == None)
>>>>>>> 71b8dc35df562592620ab0c7e4b33b87d739eedf
