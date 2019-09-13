from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        bt1 = Button(text="Botão")
        bt1.size_hint_x = .50
        bt1.size_hint_y = .15

        lb = Label(text='clique no botão abaixo')
        box.add_widget(lb)
        box.add_widget(bt1)

        return help(bt1.center)



if __name__ == '__main__':
    Test.title = 'Olá, mundo!'

    Test().run()
