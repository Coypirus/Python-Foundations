#Dictionaries are made up of key:value pairs.
#Dictionaries don't repeat, just like sets.
    #Therefore, both use curly brackets.

d = {'navin':'samsung', 'rahul':'iPhone', 'kiran':'OnePlus'}

print(d.keys())
print(d.values())
print(d['rahul'])
print(d.get('kiran', 'Not Found'))