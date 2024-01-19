from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Username', font_size=72))
        self.username = TextInput(text='Dude',
                                  multiline=False,
                                  padding_x=[100,100],
                                  padding_y=[200,0],
                                  font_size=72,
                                  background_color=[0.8, 1, 0.8, 1])
        self.add_widget(self.username)
        self.add_widget(Label(text='password', font_size=72))
        self.password = TextInput(password=True,
                                  multiline=False,
                                  padding=[10, 10, 10, 10],
                                  font_size=72
                                  )
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
