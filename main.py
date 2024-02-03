from kivy.app import App
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.graphics import Rectangle, Color

Builder.load_file('menu.kv')
Builder.load_file('game.kv')


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class Space(App):
    square_pos = {'x': 0, 'y': 400}
    angle = -45
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(MenuScreen(name='menu'))
        return sm


if __name__ == '__main__':
    Space().run()