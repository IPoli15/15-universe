import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests

kivy.require('2.3.0')

LabelBase.register(
    name='Montserrat', 
    fn_regular='assets/fonts/Montserrat-Bold.ttf'
)

class RootScreen(Screen):
    pass

class ReservaScreen(Screen):
    def check_reservation(self, id_reserva):
        print(f"Verificando reserva con ID: {id_reserva}")

class LoginScreen(Screen):
    pass

class MyRoot(BoxLayout):
    def switch_screen(self, screen_name):
        self.parent.parent.transition = SlideTransition(direction='left')
        self.parent.parent.current = screen_name

    def access_category(self, category):
        print(f"Accediendo a la categoría: {category}")

class Reserva(BoxLayout):
    def switch_root(self):
        self.parent.parent.transition = SlideTransition(direction='right')
        self.parent.parent.current = 'Root'

class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.backend_url = 'http://localhost:5001/usuarios-password'

    def send_login(self, username, password):
        """
        Enviar las credenciales al backend y manejar la respuesta.
        """
        try:
            response = requests.post(
                self.backend_url,
                json={"nombre": username, "contraseña": password}
            )
            if response.status_code == 200:
                self.show_popup("Login exitoso", f"Bienvenido, {username}")
                self.switch_root()
            else:
                self.show_popup("Error", "Error")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))

    def switch_root(self):
        self.parent.parent.transition = SlideTransition(direction='up')
        self.parent.parent.current = 'Root'

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3),
        )
        popup.open()
class UniverseApp(App):
    def build(self):
        Builder.load_file('templates/universe.kv')

        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(RootScreen(name='Root'))
        self.screen_manager.add_widget(ReservaScreen(name='Res'))
        self.screen_manager.add_widget(LoginScreen(name='Log'))

        return self.screen_manager

if __name__ == "__main__":
    UniverseApp().run()
