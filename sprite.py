from kivy.graphics import PushMatrix, Rotate, PopMatrix
from kivy.uix.image import Image


class Sprite(Image):
    def rotate_thing(self, num):
        print('it work')
        print(self)
        with self.canvas.before:
            PushMatrix()
            Rotate(angle=num, origin=self.center, axis=(0, 0, 1))
        with self.canvas.after:
            PopMatrix()
