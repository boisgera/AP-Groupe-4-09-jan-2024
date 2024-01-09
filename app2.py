import pyxel


def main():
    i = 0

    def update():
        nonlocal i
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_UP):
            i = i + 1

    def draw():
        if i % 3 == 0:
            pyxel.cls(1)
        elif i % 3 == 1:
            pyxel.cls(7)
        else:
            pyxel.cls(8)

    pyxel.init(160, 120)
    pyxel.run(update, draw)


main()
