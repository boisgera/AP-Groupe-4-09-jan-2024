import pyxel

class App:
    def __init__(self):
        self.i = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_UP):
            self.i = self.i + 1

    def draw(self):
        if self.i % 3 == 0:
            pyxel.cls(1)
        elif self.i % 3 == 1:
            pyxel.cls(7)
        else:
            pyxel.cls(8)


pyxel.init(160, 120)

app = App()
pyxel.run(app.update, app.draw)
