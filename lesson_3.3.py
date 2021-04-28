from random import choice, randrange

nouns = ["собака", "картина" , "капуста" , "русский" , "чайник"  , "тостер"]
adverbs = ["когда-то" , "где-то" , "никогда" , "что - то" , "везде" , "повсюду"]
abjectives = ["зимний" , "красивый" , "самый" , "правдивый" , "печёный" , "поющий"] 

def some_jokes(n, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), abjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverds)} {choice(adjectives)}")
        n -= 1
    return list_of_j

print(some_jokes(10, True))