from dice import Dice
from horse import Horse

dice = Dice()

h2 = Horse(2, 3)
h3 = Horse(3, 6)
h4 = Horse(4, 8)
h5 = Horse(5, 11)
h6 = Horse(6, 14)
h7 = Horse(7, 17)
h8 = Horse(8, 14)
h9 = Horse(9, 11)
h10 = Horse(10, 8)
h11 = Horse(11, 6)
h12 = Horse(12, 3)
horses = [h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12]

gameOver = False
rolls = []

while gameOver == False:
    roll = dice.roll()
    rolls.append(roll)
    for horse in horses:
        if roll == horse.lane:
            horse.position += 1
        if horse.position == horse.rolls_to_win:
            gameOver = True
            winningHorse = horse

print(f"Game over! Horse {winningHorse.lane} won! It took ", len(rolls), " rolls to win.")
print(rolls)