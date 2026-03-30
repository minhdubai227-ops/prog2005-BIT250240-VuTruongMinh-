class Flower:
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
hoa = Flower("xanh")
print(hoa.get_color())
hoa.set_color("den")
print(hoa.get_color())