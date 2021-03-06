def movement_vector_to_energy(vector):
    return movement_to_energy(vector.get_x(), vector.get_y())


def movement_to_energy(delta_x, delta_y):
    return {
        0: {0: 1, 1: 2, 2: 5},
        1: {0: 2, 1: 3, 2: 6},
        2: {0: 5, 1: 6, 2: 7},
    }[abs(delta_x)][abs(delta_y)]


def code_to_movement(code):
    mx = (code % 5) - 2
    my = int(code / 5) - 2
    return (mx, my)
