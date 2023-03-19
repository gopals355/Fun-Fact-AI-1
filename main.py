import random

fun_facts = {
    1: "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    2: "Honey never spoils.",
    3: "Cats have over 20 muscles in each ear.",
    4: "A snail can sleep for three years.",
    5: "Dolphins sleep with one eye open.",
    6: "Cows have best friends.",
    7: "A single strand of spaghetti is called a spaghetto.",
    8: "A baby octopus is about the size of a flea when it is born.",
    9: "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    10: "Greenland sharks can live for more than 400 years, making them the longest-living shark species.",
    11: "The oldest known sample of the smallpox virus has been found on the teeth of a 17th-century child buried in Lithuania.",
    12: "The world's smallest reptile is the Brookesia nana, a chameleon species discovered in Madagascar.",
    13: "The tallest tree ever recorded was an Australian eucalyptus with a height of 132.6 meters (435 feet).",
    14: "The tongue is the only muscle in the human body that is only attached at one end.",
    15: "Cleopatra lived closer in time to the building of the first Pizza Hut than to the building of the pyramids.",
    16: "Polar bears have black skin under their fur.",
    17: "Alaska is the state with the highest percentage of people who walk to work.",
    18: "The total weight of all the ants on Earth is greater than the total weight of all humans.",
    19: "The average person will spend six months of their life waiting for red lights to turn green.",
    20: "The highest wave ever surfed reached a height of 80 feet (24.4 meters).",
    21: "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    22: "There are more stars in the universe than grains of sand on all the beaches on Earth.",
    23: "The largest snowflake ever recorded measured 15 inches (38 cm) across.",
    24: "It's impossible to hum while holding your nose.",
    25: "A jiffy is a unit of time equivalent to one one-hundredth of a second.",
    26: "A group of jellyfish is called a smack.",
    27: "The first recorded game of baseball was played in 1846 in Hoboken, New Jersey.",
    28: "The first VCR was the size of a piano.",
    29: "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo'.",
    30: "The world's smallest mammal is the bumblebee bat.",
    31: "The word 'emoji' comes from the Japanese words 'e' (picture) and 'moji' (character).",
    32: "The world's largest desert is Antarctica, not the Sahara.",
    33: "The dot over the letter 'i' and 'j' is called a tittle.",
    34: "An ostrich's eye is bigger than its brain.",
    35: "The shortest war in history was between Britain and Zanzibar in 1896, lasting only 38 minutes.",
    36: "There are more than 200 different flavors of Kit Kats in Japan.",
    37: "A single cloud can weigh more than 1 million pounds.",
    38: "The Earth's core is as hot as the surface of the sun.",
    39: "The average person walks the equivalent of five times around the world during their lifetime.",
    40: "The word 'karaoke' means 'empty orchestra' in Japanese.",
    41: "A giraffe's tongue can be up to 45 cm (18 inches) long.",
    42: "The smell of freshly cut grass is a distress signal from the plant.",
    43: "Blue whales eat half a million calories in one mouthful.",
    44: "It rains diamonds on Saturn and Jupiter.",
    45: "There are more possible ways to shuffle a deck of cards than there are atoms on Earth.",
    46: "The world's oldest known living tree is over 9,500 years old.",
    47: "Peanuts are not nuts; they're actually legumes.",
    48: "The first recorded use of the word 'hello' was by Thomas Edison.",
    49: "The average person produces enough saliva in their lifetime to fill two swimming pools.",
    50: "Bananas are berries, while strawberries are not."
}

def get_fun_fact():
    fact_key = random.choice(list(fun_facts.keys()))
    return fun_facts[fact_key]

if __name__ == "__main__":
    while True:
        prompt = input("Enter a prompt for a fun fact or type 'exit' to quit: ")
        
        if prompt.lower() == "exit":
            break
        
        print(get_fun_fact())

