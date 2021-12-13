# Collections 2 boodschappenlijst

def boodschappenlijstje():
    lijstje = {}
    for x in range(9999999999999999999999999999):
        item = input("Wat wil je hebben? ")
        if item in lijstje:
            lijstje[item] += 1
        else:
            lijstje.update({item : 1})
        print(lijstje)
        wil = input("wil je nog meer toevoegen?")
        if wil == "nee":
            print(lijstje)
            quit()

boodschappenlijstje()