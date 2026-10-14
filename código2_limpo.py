def calc_points(a, b, c):
    total = a + b + c
    return total


def sort_students():
    harry = 20
    hermione = 25
    ron = 18
    draco = 30
    gryffindor = calc_points(harry, hermione, ron)
    slytherin = calc_points(draco, 0, 0)
    print("Pontos da Grifinória: ", gryffindor)
    print("Pontos da Sonserina: ", slytherin)


sort_students()
