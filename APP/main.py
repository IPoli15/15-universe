import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
import requests

kivy.require('2.3.0')

LabelBase.register(
    name='Montserrat', 
    fn_regular='assets/fonts/Montserrat-Bold.ttf'
)

BACKEND_URL = 'http://localhost:5001'

class RootScreen(Screen):
    def logout(self):
        App.get_running_app().is_logged_in = False
        App.get_running_app().root.current = 'Log'
        App.get_running_app().root.get_screen('Log').ids.username.text = ''
        App.get_running_app().root.get_screen('Log').ids.password.text = ''

class ReservaScreen(Screen):
    def check_reservation(self, id_reserva):
        try:
            response = requests.get(f"{BACKEND_URL}/consultar-reserva/{id_reserva}")
            if response.status_code == 200:
                data = response.json()
                detalles = (
                    f"ID de la Reserva: {data['id_reserva']}\n"
                    f"Cantidad de tickets: {data['cant_tickets']}\n"
                    f"Nombre del evento: {data['nombre_evento']}\n"
                    f"Precio entrada: ${data['precio_entrada']:.2f}"
                )
                self.show_popup("Reserva encontrada", detalles)
            else:
                self.show_popup("No se encontró la reserva.", "Revisa tu numero de reserva")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3),
            background_color=(0.1, 0.1, 0.15, 0.9),
            title_color=(1, 1, 1, 1),
            title_size='18sp',
            separator_color=(0.3, 0.2, 0.8, 1)
        )
        popup.content.color = (1, 1, 1, 1)
        popup.open()

class LoginScreen(Screen):
    pass

class MyRoot(BoxLayout):
    def switch_screen(self, screen_name):
        self.parent.parent.transition = SlideTransition(direction='left')
        self.parent.parent.current = screen_name

    def access_category(self, category):
        print(f"Accediendo a la categoría: {category}")
        try:
            response = requests.get(f"{BACKEND_URL}/consultar-eventos/{category}")
            if response.status_code == 200:
                events = response.json()
                print(f"Eventos en la categoría {category}:", events)
            else:
                print(f"Error al obtener eventos de la categoría {category}")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {str(e)}")

class Reserva(BoxLayout):
    def switch_root(self):
        self.parent.parent.transition = SlideTransition(direction='right')
        self.parent.parent.current = 'Root'

    def check_reservation(self, id_reserva):
        App.get_running_app().root.get_screen('Res').check_reservation(id_reserva)

class Login(BoxLayout):
    def send_login(self, username, password):
        try:
            response = requests.post(
                f"{BACKEND_URL}/usuarios-password",
                json={"nombre": username, "password": password}
            )
            if response.status_code == 200:
                data = response.json()
                self.show_login_popup("Login exitoso", f"Bienvenido, {username}")
                App.get_running_app().is_logged_in = True
                self.switch_root()
            else:
                self.show_login_popup("Error", "Credenciales inválidas")
        except requests.exceptions.RequestException as e:
            self.show_login_popup("Error de conexión", str(e))

    def switch_root(self):
        self.parent.parent.transition = SlideTransition(direction='up')
        self.parent.parent.current = 'Root'

    def show_login_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3),
            background_color=(0.1, 0.1, 0.15, 0.9),
            title_color=(1, 1, 1, 1),
            title_size='18sp',
            separator_color=(0.3, 0.2, 0.8, 1)
        )
        popup.content.color = (1, 1, 1, 1)
        popup.open()

class UniverseApp(App):
    is_logged_in = BooleanProperty(False)

    def build(self):
        Builder.load_file('templates/universe.kv')

        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(RootScreen(name='Root'))
        self.screen_manager.add_widget(ReservaScreen(name='Res'))
        self.screen_manager.add_widget(LoginScreen(name='Log'))

        return self.screen_manager

if __name__ == "__main__":
    UniverseApp().run()
