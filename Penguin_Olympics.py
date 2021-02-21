snapshot = """
|--~~---~~~------~------p--------------------------------------------------------------------------|
|-~~------------~------------------------p---------------------------------------------------------|
|~~--~------------~-------~-------~--p-----~-------~-------~-------~-------~-------~-------~-------|
|--------~------------------------p----------------------------------------------------------------|
|--------~-----~~~-----------p---------------------------------------------------------------------|
"""
penguins = ['Adam', 'Brian', 'Flipper', 'Franko', 'Darwin']

def calculate_winners(snapshot, penguins):

	lanes = []
	speeds = []


	for i in snapshot.lower().strip().strip(' ').split('\n'):
		lanes.append((0, i))

	penguins_speed = dict(zip(penguins, lanes))


	for speed, lane in penguins_speed.values():
		length = 0
		for i in lane[lane.index('p'):]:
			if i == '-':
				length += 1
			if i == '~':
				length += 2

		speeds.append(length)


	sorted_res = sorted([*zip(speeds, penguins)], key=lambda x: x[0])
	return "GOLD: {}, SILVER: {}, BRONZE: {}".format(sorted_res[0][1], sorted_res[1][1], sorted_res[2][1])



print(calculate_winners(snapshot, penguins))

# result GOLD: Brian, SILVER: Franko, BRONZE: Flipper

