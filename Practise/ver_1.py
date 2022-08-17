beef = 0
pork = 0
lamb = 0

menu = {
    'beef': beef,
    'pork': pork,
    'lamb': lamb
}


def menu_update(i):
    global beef, pork, lamb
    if i == menu['beef']+1:
        beef += 1
        print(beef)


menu_update(menu['beef']+1)
