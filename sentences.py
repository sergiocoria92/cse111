import random

def main():
    """Genera y muestra 6 oraciones con diferentes cantidades, tiempos verbales, frases preposicionales y adverbios."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Construye y devuelve una oración con un determinante, un sustantivo, un verbo y dos frases preposicionales."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    adverb = get_adverb()

    sentence = f"{determiner} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2} {adverb}."
    return sentence.capitalize()



def get_determiner(quantity):
    """Devuelve un determinante aleatorio."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Devuelve un sustantivo aleatorio."""
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Devuelve un verbo aleatorio basado en el tiempo y cantidad."""
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:  # future
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(verbs)

def get_preposition():
    """Devuelve una preposición aleatoria."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", 
                    "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Construye y devuelve una frase preposicional compuesta por una preposición, un determinante y un sustantivo."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_adverb():
    """Devuelve un adverbio aleatorio."""
    adverbs = ["quickly", "slowly", "happily", "sadly", "easily", "loudly", "gracefully", "frequently", "quietly", "carefully"]
    return random.choice(adverbs)

if __name__ == "__main__":
    main()
