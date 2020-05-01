import math

print([value for value in ["Hans,", "Birgitte", "Henriette", "Arnold", "Hedvig"] if value.startswith("H")])

print ([value ** 3 for value in range (1, 101)])

print([(len(a), a) for a in ["Hans,", "Birgitte", "Henriette", "Arnold", "Hedvig"]])

print ([value for value in "khjbg324lhkbj234ljhvb43lkhj" if value.isdigit()])

print (set([(a, b) for a in range(1, 7) for b in range(1, 7)]))

print ({a: len(a) for a in ["Hans,", "Birgitte", "Henriette", "Arnold", "Hedvig"]})

print ({a: math.sqrt(a) for a in range(1, 10)})

def dice():
    dice_rolls = [a + b for a in range(1, 7) for b in range(1, 7)]
    print(dice_rolls)
    probability = {a: "{0:.0%}".format(dice_rolls.count(a)/len(dice_rolls)) for a in dice_rolls}
    print(probability)

dice()