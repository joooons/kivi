from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        grid_layout = GridLayout(cols=3,
                                 row_force_default=True,
                                 row_default_height=200,
                                 col_force_default=True,
                                 col_default_width=200)
        for i in range(1,7):
            grid_layout.add_widget(Button(text=f'{i}'))

        self.title = Label(text='Title', font_size=72, size_hint_x = None, width=600)
        self.paragraph = Label(text='Message', font_size=72, size_hint_x = None, width=600)
        self.next_button = Button(text='CLICK ME',
                                  font_size=72,
                                  size_hint_y =None,
                                  height=100,size_hint_x = None, width=600)
        self.add_widget(Label(text=''))
        self.add_widget(grid_layout)
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(self.title)
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(self.paragraph)
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(self.next_button)
        self.add_widget(Label(text=''))



class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
