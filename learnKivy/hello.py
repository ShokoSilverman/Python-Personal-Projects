import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # init infinite keywords
    def __init__(self, **kwargs):
        # call grid layout ctor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1

        # create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # Add input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # add widgets
        self.top_grid.add_widget(Label(text="Favorite Color: "))
        # Add input box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # add new top_grid to app
        self.add_widget(self.top_grid)

        # create a submit button
        self.submit = Button(text="Submit", font_size="32")
        # Bind button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name: str = self.name.text
        pizza: str = self.pizza.text
        color: str = self.color.text
        # print(name, pizza, color)
        self.add_widget(
            Label(
                text=f"Hello {name}, you like {pizza} pizza, your favorite color is {color}"
            )
        )

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
