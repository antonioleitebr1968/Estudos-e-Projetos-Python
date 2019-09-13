from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

class Principal(BoxLayout):

    texto_principal = StringProperty('Eu sou uma label')
    tamanho_texto_princinpal = NumericProperty(20)

    def teste(self):
        self.texto_principal = 'Fui clicado'
        self.tamanho_texto_princinpal += 5


class Secundario(Widget):
    pass

class Teste(App):
    def build(self):
        return Principal()

Teste().run()
