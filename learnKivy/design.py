import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name: str = self.name.text
        pizza: str = self.pizza.text
        color: str = self.color.text
        # print(name, pizza, color)
        # self.add_widget(
        #     Label(
        #         text=f"Hello {name}, you like {pizza} pizza, your favorite color is {color}"
        #     )
        # )
        print(f"Hello {name}, you like {pizza} pizza, your favorite color is {color}")

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


# kv file needs to be this.kv unless app is in it, then remove app (my.kv)
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
