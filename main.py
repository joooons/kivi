from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('unrelated.kv')


class MyLayout(Widget):

    name = ObjectProperty(None)
    color = ObjectProperty(None)
    pizza = ObjectProperty(None)
    def press(self):
        name = self.name.text
        color = self.color.text
        pizza = self.pizza.text

        print(f'{name} {color} {pizza}')
        # self.add_widget(Label(text=f'{name} {color} {pizza}'))
        self.name.text = ''
        self.color.text = ''
        self.pizza.text = ''


class Space(App):
    def build(self):
        Window.clearcolor = (0.7,0.9,0.7,1)
        return MyLayout()


if __name__ == '__main__':
    Space().run()
