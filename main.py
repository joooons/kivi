from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.label import Label


class MyGridLayout(Widget):
    def press(self, instance):
        name = self.name.text
        color = self.color.text
        pizza = self.pizza.text
        self.add_widget(Label(text=f'{name} {color} {pizza}'))
        self.name.text = ''
        self.color.text = ''
        self.pizza.text = ''


class Space(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Space().run()
