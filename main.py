# import kivy
# kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='hello there')

if __name__ == '__main__':
    MyApp().run()