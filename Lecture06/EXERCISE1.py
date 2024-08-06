heroes = ['Ironman','Thor','Hulk','Spiderman']
def Disply():
    print(f"The list of Heroes: {heroes}")
def add():
    global heroes
    heroes_add = input("Please input heroes name :")
    heroes.append(heroes_add)
