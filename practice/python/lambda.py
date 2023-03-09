people = [{'name': "A", 'house': "abc"}, {'name': "C", 'house': "ghi"}, {'name': "B", 'house': "def"}]

# takes input parameter of person and returns name of the person
people.sort(key = lambda person: person["name"])

print(people)   