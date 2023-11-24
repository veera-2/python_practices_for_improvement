# SLICING = create a substring by extracting elements fom another string
# to slice a string we can use the indexing[] or slice()
# there are three argument in slicing a string  [start:stop:step]

name = "khadija hamisu"

first_name = name[0:7]
last_name = name[8:]
nick_name = name[0:14:3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(nick_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)
#website[slice]

print(website1[slice])
print(website2[slice])