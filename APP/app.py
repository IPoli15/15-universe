from kivy.app import App 
from kivy.lang import Builder 

class MyApp(App):
    def build(self):
        return Builder.load_file("app.kv")
if __name__ == "__main__":
    MyApp().run()