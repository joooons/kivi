from kivy.app import App

from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

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
        return MyGridLayout()


if __name__ == '__main__':
    Space().run()
