import random
dict_players = {}
letters = 'qwertyuiopasdfghjklzxcvbnm'
for i in range(50):
    dict_players[random.randrange(100000, 1000000)] = str(random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters))
print(dict_players)    