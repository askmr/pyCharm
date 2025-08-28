class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return x, y

P1=Point(2,4)
P2=Point(4,2)

print(P1+P2)
print(P1-P2)
