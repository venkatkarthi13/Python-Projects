    
from random import choice

city="Chennai"
Train="Metro, Localtrain"
Airport="Meenambakkam"
Central="Vyasarpadi"

def randomFunfacts():
    funFacts = [
           "The shortest war in history lasted only 38 minutes. It was between Britain and Zanzibar on August 27, 1896.",
           "A group of flamingos is called a flamboyance.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "The surface area of Russia is larger than the surface area of Pluto.",
            "Bananas are berries, but strawberries aren't.",
            "Octopuses have three hearts.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the iron.",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
            "The unicorn is the national animal of Scotland.",
            "There are more possible iterations of a game of chess than there are atoms in the known universe."]
    
    index=choice("012345")

    print(funFacts[int(index)])
randomFunfacts()
        