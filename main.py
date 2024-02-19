import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget

kivy.require("2.2.1")

Builder.load_file('pong.kv')
Builder.load_file('menu.kv')
# Builder.load_file('game.kv')
Builder.load_file('tick.kv')


class MenuScreen(Screen):
    pass


class TickScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class PongBall(Widget):
    pass


class PongGame(Widget):
    pass


class Space(App):
    square_pos = {'x': 400, 'y': 700}

    def build(self):
        return PongGame()
        # sm = ScreenManager(transition=NoTransition())
        # sm.add_widget(MenuScreen(name='menu'))
        # sm.add_widget(TickScreen(name='tick'))
        # # sm.add_widget(GameScreen(name='game'))
        # return sm


if __name__ == '__main__':
    Space().run()
