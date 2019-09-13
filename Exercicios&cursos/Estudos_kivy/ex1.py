import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class Testando(Widget):
    pass

class MyApp(App):

    def build(self):
        return Testando()


if __name__ == '__main__':
    MyApp().run()
