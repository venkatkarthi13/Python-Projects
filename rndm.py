    
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
            "There are more possible iterations of a game of chess than there are atoms in the known universe.",
            "Cows have best friends and can become stressed when they are separated.",
            "Wombat poop is cube-shaped.",
            "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
            "The inventor of the Pringles can is now buried in one.",
            "A small child could swim through the veins of a blue whale.",
            "An octopus has three hearts.",
            "A bolt of lightning is five times hotter than the surface of the sun.",
            "The longest hiccuping spree lasted 68 years.",
            "The world's smallest reptile was discovered in 2021 in Madagascar, and it fits on the tip of a finger.",
            "A snail can sleep for three years at a time.",
            "You can hear a blue whale's heartbeat from more than 2 miles away.",
            "Sloths can hold their breath longer than dolphins can.",
            "The longest time between two twins being born is 87 days.",
            "The inventor of the Frisbee was turned into a Frisbee after he died.",
            "A jiffy is an actual unit of time: 1/100th of a second.",
            "Cows can walk up stairs, but not down them.",
            "The dot over the lowercase letters 'i' and 'j' is called a tittle.",
            "The human nose can detect over 1 trillion different scents.",
            "There are more stars in the universe than grains of sand on all the Earth's beaches.",
            "A single strand of spaghetti is called a 'spaghetto.' "
            ]
    
    index=choice("012345")

    print(funFacts[int(index)])
randomFunfacts()
        