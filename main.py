from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.graphics import Rectangle, Color, PushMatrix, Rotate, PopMatrix

Builder.load_file('menu.kv')
Builder.load_file('game.kv')


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class Space(App):
    square_pos = {'x': 400, 'y': 700}

    def rotate_image(self, instance) -> None:
        print('it work')
        print(instance)
        # animate = Animation(pos=(500, 400), size=(300, 300), duration=1)
        # animate.start(instance)
        with instance.canvas.before:
            PushMatrix()
            Rotate(angle=-10, origin=instance.center, axis=(0, 0, 1))
        with instance.canvas.after:
            PopMatrix()


    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(MenuScreen(name='menu'))
        return sm


if __name__ == '__main__':
    Space().run()