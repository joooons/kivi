import kivy
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

kivy.require("2.2.1")

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

Builder.load_file('menu.kv')
Builder.load_file('tick.kv')


class MenuScreen(Screen):
    pass


class TickScreen(Screen):
    pass


class Space(App):
    square_pos = {'x': 400, 'y': 700}

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(TickScreen(name='tick'))
        sm.add_widget(MenuScreen(name='menu'))
        return sm


if __name__ == '__main__':
    Space().run()
