from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.names = ['Anna', 'Bob', 'Carl', 'Dave', 'Edna']

    def build(self):

        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()

        return self.root

    def create_widgets(self):

        for name in self.names:

            temp_label = Label(text=name)
            temp_label.font_size = 36
            temp_label.color = (0, 0, 1, 1)

            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
