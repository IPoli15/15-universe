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
import requests
from kivy.uix.popup import Popup
from kivy.uix.label import Label


kivy.require('2.3.0')


# Add custom fonts
LabelBase.register(
    name='Montserrat', 
    fn_regular='assets/fonts/Montserrat-Bold.ttf'
)


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    
    def switch_res(self):
        app.screen_manager.transition = SlideTransition(direction='down')
        app.screen_manager.current = 'Res'

    def switch_log(self):
        app.screen_manager.transition = SlideTransition(direction='down')
        app.screen_manager.current = 'Log'

    def change_color(self):
        self.main_title.color = new_rgb_color()

class Reserva(BoxLayout):
    def __init__(self):
        super(Reserva, self).__init__()

    def switch_root(self):
        app.screen_manager.transition = SlideTransition(direction='down')
        app.screen_manager.current = 'Root'
    
    def change_color(self):
        self.main_title.color = new_rgb_color()

class Login(BoxLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.backend_url = 'http://localhost:5001/usuarios-password' 

    def send_login(self, username, password):
        """
        Enviar las credenciales al backend.
        """
        try:
            response = requests.post(
                self.backend_url,
                json={"nombre": username, "password": password}
            )
            
            if response.status_code == 200:
                self.show_popup("Login Exitoso", "Bienvenido, " + username)
                self.switch_root()
            else:

                self.show_popup("Error", "Credenciales incorrectas o problema con el servidor")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))
    
    def switch_root(self):
        app.screen_manager.transition = SlideTransition(direction='down')
        app.screen_manager.current = 'Root'
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3),
        )
        popup.open()


      



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

        self.login = Login()
        screen = Screen(name='Log')
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)


        return self.screen_manager


    
if __name__ == "__main__":
    app = Universe()
    app.run() 
