import random

actions = ["the world was destroyed", 
			"nazis have taken power",
			"pollution makes you gay",
			"I'm married to a lizard person",
			"whip my hair won a grammy",
			"we get to play games",
			"your bones were shattered",
			"we have to fight to survive"]

nouns = ["Drumpf",
			"evangicals",
			"feminists",
			"muppets",
			"THEE dalai lama",
			"Rick Sanchez",
			"skynet"]

random_action = random.choice(actions)
random_noun = random.choice(nouns)

print(f"I can't believe {random_action} thanks to {random_noun}")

