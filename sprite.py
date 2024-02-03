from kivy.clock import Clock
from kivy.graphics import PushMatrix, Rotate, PopMatrix
from kivy.uix.image import Image


class Sprite(Image):
    angle = 0
    event = None

    def rotate(self, num):
        with self.canvas.before:
            PushMatrix()
            self.angle += num
            print(self.angle)
            Rotate(angle=num, origin=self.center, axis=(0, 0, 1))
        with self.canvas.after:
            PopMatrix()

    def start_rotation(self, num):
        self.event = Clock.schedule_interval(lambda dt: self.update_rotation(num), 1 / 60)

    def update_rotation(self, num):
        self.rotate(num)
        if self.angle >= 90:
            Clock.unschedule(self.event)
