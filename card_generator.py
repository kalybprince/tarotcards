import json
from random import randint

with open('jsondata.json') as f:
	data = json.load(f)

rand_num = randint(0, 76)

print()
print(data['card'][rand_num]['name'])
print()
print(data['card'][rand_num]['keywords'])