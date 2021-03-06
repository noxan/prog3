from shared.geometry import WorldPoint
from shared.utils import movement_to_energy, code_to_movement


class Nibble(object):
    def __init__(self, name, world, position=None, energy=30):
        self._name = name
        self._world = world
        if position:
            self._position = position
        else:
            self._position = WorldPoint(world, 0, 0)
        self._energy = energy
        self._world.set(self.get_position(), self)

    def move_code(self, code):
        code = int(code)
        movement = code_to_movement(code)
        return self.move(movement[0], movement[1])

    def move(self, dx, dy):
        denergy = movement_to_energy(dx, dy)
        self._energy -= denergy
        self._world.move(self.get_position(), dx, dy)
        self._position.move(dx, dy)

    def get_name(self):
        return self._name

    def is_alive(self):
        return self._energy > 0

    def get_position(self):
        return self._position

    def get_position_x(self):
        return self._position._x

    def get_position_y(self):
        return self._position._y

    def get_energy(self):
        return self._energy

    def compare_energy(self, other):
        if self.get_energy() > other.get_energy():
            return 1
        elif self.get_energy() < other.get_energy():
            return -1
        else:
            return 0

    def eat(self, other):
        if isinstance(other, Nibble):
            compare = self.compare_energy(other)
            if compare < 0:
                self._energy += other.get_energy()
                other._energy = 0
            else:
                other._energy += self.get_energy()
                self._energy = 0
        else:
            self._energy += 5

    def __str__(self):
        return "%s (%s)" % (self.get_name(), self.get_position())
