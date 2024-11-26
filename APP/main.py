from kivy.uix.filechooser import Screen
from kivy.uix.screenmanager import SlideTransition
import kivy
from kivy.app import App
from kivy.lang import Builder 
from kivy.core.text import LabelBase
# from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from utils.colors import new_rgb_color
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


kivy.require('2.3.0')


# Add custom fonts
LabelBase.register(
    name='Montserrat', 
    fn_regular='assets/fonts/Montserrat-Bold.ttf'
)


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    
    def switch(self):
        app.screen_manager.transition = SlideTransition(direction='down')
        app.screen_manager.current = 'Res'

    def change_color(self):
        self.main_title.color = new_rgb_color()

class Reserva(BoxLayout):
    def __init__(self):
        super(Reserva, self).__init__()
    
    def change_color(self):
        self.main_title.color = new_rgb_color()
      



class Universe(App):

    # .kv files path
    kv_directory = "templates"

    def build(self):
        # return Label(text="Hello World!")
        # return MyRoot()
        self.screen_manager = ScreenManager()

        self.myroot = MyRoot()
        screen = Screen(name='Root')
        screen.add_widget(self.myroot)
        self.screen_manager.add_widget(screen)

        self.reserva = Reserva()
        screen = Screen(name='Res')
        screen.add_widget(self.reserva)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


    
if __name__ == "__main__":
    app = Universe()
    app.run() 
