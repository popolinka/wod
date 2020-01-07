import random


""" Assuming the text files are relatively small"""

filenames = ['CS34_wods.txt', 'crossfitCom_wods.txt']

# with open('/Users/orkunkadioglu/PycharmProjects/buSeferCiddi/venv/wods.txt', 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             outfile.write(infile.read())


def generateRandomWod():
    workouts = open('wods.txt').read().splitlines()
    randomWorkout = random.choice(workouts)
    return randomWorkout

for i in range(1,5):
    print(generateRandomWod())
