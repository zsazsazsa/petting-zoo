from Slithering import Copperhead, RatSnake, Salamander, Bullfrog, Newt
from Swimming import Mallard, Goldfish, Catfish, Koi, Swan
from Walking import Llama, Donkey, Sheep, Alpaca, Cow

miss_fuzz = Llama("Miss Fuzz", "Llama", "Morning")

hector = Donkey("Hector", "Donkey", "Midday")

ilana = Sheep("Ilana", "Sheep", "Midday")

percy = Alpaca("Percy", "Alpaca", "Afternoon")

betty = Cow("Betty", "Cow", "Afternoon")

dirk = Mallard("Dirk", "Mallard")

joyce = Goldfish("Joyce", "Goldfish")

spencer = Catfish("Spencer", "Catfish")

yvonne = Swan("Yvonne", "Swan")

joy = Koi("Joy", "Koi")

colin = Copperhead("Colin", "Copperhead")

rachel = RatSnake("Rachel", "Rat Snake")

sally = Salamander("Sally", "Salamander")

buford = Bullfrog("Buford", "Bullfrog")

nell = Newt("Nell", "Newt")

print(f'{hector.name} the {hector.species} is available to pet during the {hector.shift} shift.')
