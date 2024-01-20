from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGridLayout(Widget):


    def press(self, instance):
        name = self.name.text
        color = self.color.text
        pizza = self.pizza.text
        self.add_widget(Label(text=f'{name} {color} {pizza}'))
        self.name.text = ''
        self.color.text = ''
        self.pizza.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
