import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.properties import BooleanProperty, StringProperty, DictProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from datetime import datetime
import requests
from functools import partial
import time

kivy.require('2.3.0')

LabelBase.register(
    name='Montserrat', 
    fn_regular='assets/fonts/Montserrat-Bold.ttf'
)

BACKEND_URL = "https://Ruy.pythonanywhere.com"


class PaymentPopup(Popup):
    def __init__(self, event, **kwargs):
        super().__init__(**kwargs)
        self.event = event
        self.title = "Pago seguro"
        self.size_hint = (0.9, 0.9)
        self.background_color = (0.1, 0.1, 0.15, 0.9)
        self.title_color = (1, 1, 1, 1)
        self.title_size = '18sp'
        self.separator_color = (0.3, 0.2, 0.8, 1)

        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        event_info = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=100)
        event_info.add_widget(Label(text="Información del Evento", size_hint_y=None, height=30, color=(1, 1, 1, 1), bold=True))
        event_info.add_widget(Label(text=f"Nombre: {event['nombre_evento']}", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
        event_info.add_widget(Label(text=f"Precio: ${event['precio_entrada']}", size_hint_y=None, height=30, color=(1, 1, 1, 1)))
        content.add_widget(event_info)

        buyer_info = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=100)
        buyer_info.add_widget(Label(text="Detalles del Comprador", size_hint_y=None, height=30, color=(1, 1, 1, 1), bold=True))
        self.username_input = TextInput(text=App.get_running_app().username, readonly=True, size_hint_y=None, height=40,
                                        background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        buyer_info.add_widget(self.username_input)
        content.add_widget(buyer_info)

        purchase_info = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=100)
        purchase_info.add_widget(Label(text="Detalles de la Compra", size_hint_y=None, height=30, color=(1, 1, 1, 1), bold=True))
        self.quantity_input = TextInput(hint_text="Cantidad de Tickets", input_filter='int', size_hint_y=None, height=40,
                                        background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        purchase_info.add_widget(self.quantity_input)
        content.add_widget(purchase_info)

        payment_info = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=250)
        payment_info.add_widget(Label(text="Información de Pago", size_hint_y=None, height=30, color=(1, 1, 1, 1), bold=True))
        
        self.card_number = TextInput(hint_text="Número de Tarjeta", size_hint_y=None, height=40,
                                    background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        self.card_name = TextInput(hint_text="Nombre en la Tarjeta", size_hint_y=None, height=40,
                                background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        self.expiry_date = TextInput(hint_text="Fecha de Vencimiento (MM/AA)", size_hint_y=None, height=40,
                                    background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        self.cvv = TextInput(hint_text="CVV", password=True, size_hint_y=None, height=40,
                            background_color=(0.2, 0.2, 0.25, 1), foreground_color=(1, 1, 1, 1), cursor_color=(1, 1, 1, 1))
        
        payment_info.add_widget(self.card_number)
        payment_info.add_widget(self.card_name)
        payment_info.add_widget(self.expiry_date)
        payment_info.add_widget(self.cvv)
        
        content.add_widget(payment_info)

        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        confirm_button = Button(text="Confirmar Compra", size_hint_x=0.5, background_color=(0.604, 0.302, 0.608, 1))
        confirm_button.bind(on_release=self.confirm_purchase)
        buttons.add_widget(confirm_button)

        cancel_button = Button(text="Cancelar", size_hint_x=0.5, background_color=(0.5, 0.5, 0.5, 1))
        cancel_button.bind(on_release=self.dismiss)
        buttons.add_widget(cancel_button)

        content.add_widget(buttons)
        self.content = content

    def confirm_purchase(self, instance):
        quantity = self.quantity_input.text
        if not quantity or not quantity.isdigit() or int(quantity) <= 0:
            self.show_error_popup("Por favor, ingrese una cantidad válida de tickets")
            return
        
        if not all([self.card_number.text, self.card_name.text, self.expiry_date.text, self.cvv.text]):
            self.show_error_popup("Por favor, complete todos los campos de pago")
            return

        try:
            response = requests.post(f"{BACKEND_URL}/crear-reserva", json={
                "nombre": App.get_running_app().username,
                "id_evento": self.event['id_evento'],
                "cant_tickets": int(quantity)
            })
            if response.status_code == 201:
                data = response.json()
                self.show_success_popup(f"Reserva creada con ID: {data['id_reserva']}")
                self.dismiss()
            else:
                self.show_error_popup("No se pudo completar la compra")
        except requests.exceptions.RequestException as e:
            self.show_error_popup(f"Error de conexión: {str(e)}")

    def show_error_popup(self, message):
        error_popup = Popup(title='Error',
                            content=Label(text=message),
                            size_hint=(0.8, 0.3),
                            background_color=(0.1, 0.1, 0.15, 0.9),
                            title_color=(1, 1, 1, 1),
                            title_size='18sp',
                            separator_color=(0.3, 0.2, 0.8, 1))
        error_popup.content.color = (1, 1, 1, 1)
        error_popup.open()

    def show_success_popup(self, message):
        success_popup = Popup(title='Compra exitosa',
                            content=Label(text=message),
                            size_hint=(0.8, 0.3),
                            background_color=(0.1, 0.1, 0.15, 0.9),
                            title_color=(1, 1, 1, 1),
                            title_size='18sp',
                            separator_color=(0.3, 0.2, 0.8, 1))
        success_popup.content.color = (1, 1, 1, 1)
        success_popup.open()

class RootScreen(Screen):
    def logout(self):
        app = App.get_running_app()
        app.is_logged_in = False
        app.username = ''
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'Root'
        app.root.get_screen('Log').ids.username.text = ''
        app.root.get_screen('Log').ids.password.text = ''
        self.ids.my_root.update_buttons()

class ReservaScreen(Screen):
    def check_reservation(self, id_reserva):
        if not id_reserva:
            self.show_popup("Error", "Por favor, ingrese un ID de reserva")
            return

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
                self.show_popup("Detalles de la reserva", detalles)
            elif response.status_code == 404:
                self.show_popup("Reserva no encontrada", f"No se encontró una reserva con el ID {id_reserva}")
            else:
                self.show_popup("Error", "No se pudo obtener la información de la reserva")
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

"""class CrearEventoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def create_event(self):
        nombre_evento = self.ids.nombre_evento.text
        categoria = self.ids.categoria.text
        descripcion = self.ids.descripcion.text
        imagen_url = self.ids.imagen_url.text
        try:
            entradas_totales = int(self.ids.entradas_totales.text)
            entradas_disponibles = int(self.ids.entradas_disponibles.text)
            precio_entrada = int(self.ids.precio_entrada.text)
        except ValueError:
            self.show_popup("Error", "Ingresar un numero valido")
            return

        fecha_hora = self.ids.fecha_hora.text
        localizacion = self.ids.localizacion.text

        if not all([nombre_evento, categoria, descripcion, imagen_url, 
                self.ids.entradas_totales.text, self.ids.entradas_disponibles.text,
                fecha_hora, localizacion, self.ids.precio_entrada.text]):
            self.show_popup("Error", "Todos los campos son requeridos")
            return

        event_data = {
            'nombre_evento': nombre_evento,
            'categoria': categoria,
            'descripcion': descripcion,
            'entradas_totales': entradas_totales,
            'entradas_disponibles': entradas_disponibles,
            'fecha_hora': fecha_hora,
            'localizacion': localizacion,
            'precio_entrada': precio_entrada,
            'imagen_url': imagen_url,
            'es_recomendacion': False
        }

        try:
            response = requests.post(f"{BACKEND_URL}/api/crear_evento", data=event_data)
            if response.status_code == 201:
                data = response.json()
                id_evento = data.get('id_evento', 'No disponible')
                self.show_popup("Éxito", f"Evento creado correctamente. ID del evento: {id_evento}")
                self.clear_fields()
            else:
                self.show_popup("Error", f"No se pudo crear el evento. Código de estado: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))

    def clear_fields(self):
        fields = ['nombre_evento', 'descripcion', 'imagen_url', 
                'entradas_totales', 'entradas_disponibles', 
                'fecha_hora', 'localizacion', 'precio_entrada']
        for field in fields:
            if hasattr(self.ids, field):
                self.ids[field].text = ''
        if hasattr(self.ids, 'categoria'):
            self.ids.categoria.text = 'Fiesta'

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

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'Root'"""

class BusquedaEventosPopup(Popup):
    events_layout = ObjectProperty(None)

    def __init__(self, busqueda, events, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Resultados para: {busqueda}"
        self.size_hint = (0.9, 0.9)
        self.background_color = (0.1, 0.1, 0.15, 0.9)
        self.title_color = (1, 1, 1, 1)
        self.title_size = '18sp'
        self.separator_color = (0.3, 0.2, 0.8, 1)

        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        scroll_view = ScrollView(size_hint=(1, 1))

        self.events_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.events_layout.bind(minimum_height=self.events_layout.setter('height'))

        for event in events:
            event_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            event_label = Label(text=f"{event['nombre_evento']} - ${event['precio_entrada']}", size_hint_x=0.7)
            buy_button = Button(text="Comprar", size_hint_x=0.3)
            buy_button.bind(on_release=lambda x, e=event: self.purchase_tickets(e))
            event_layout.add_widget(event_label)
            event_layout.add_widget(buy_button)
            self.events_layout.add_widget(event_layout)

        scroll_view.add_widget(self.events_layout)
        content.add_widget(scroll_view)

        back_button = Button(text="Volver", size_hint_y=None, height=40)
        back_button.bind(on_release=self.dismiss)
        content.add_widget(back_button)

        self.content = content

    def purchase_tickets(self, event):
        app = App.get_running_app()
        if not app.is_logged_in:
            self.show_popup("Error", "Debes iniciar sesión para comprar entradas")
            return

        payment_popup = PaymentPopup(event)
        payment_popup.open()

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

class EventsPopup(Popup):
    def __init__(self, category, events, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Eventos de {category}"
        self.size_hint = (0.9, 0.9)
        self.background_color = (0.1, 0.1, 0.15, 0.9)
        self.title_color = (1, 1, 1, 1)
        self.title_size = '18sp'
        self.separator_color = (0.3, 0.2, 0.8, 1)

        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        scroll_view = ScrollView(size_hint=(1, 1))
        events_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        events_layout.bind(minimum_height=events_layout.setter('height'))

        for event in events:
            event_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            event_label = Label(text=f"{event['nombre_evento']} - ${event['precio_entrada']}", size_hint_x=0.7)
            buy_button = Button(text="Comprar", size_hint_x=0.3)
            buy_button.bind(on_release=lambda x, e=event: self.purchase_tickets(e))
            event_layout.add_widget(event_label)
            event_layout.add_widget(buy_button)
            events_layout.add_widget(event_layout)

        scroll_view.add_widget(events_layout)
        content.add_widget(scroll_view)

        back_button = Button(text="Volver", size_hint_y=None, height=40)
        back_button.bind(on_release=self.dismiss)
        content.add_widget(back_button)

        self.content = content

    def purchase_tickets(self, event):
        app = App.get_running_app()
        if not app.is_logged_in:
            self.show_popup("Error", "Debes iniciar sesión para comprar entradas")
            return

        payment_popup = PaymentPopup(event)
        payment_popup.open()

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

class MyRoot(BoxLayout):
    category_cache = DictProperty({})
    category_timers = DictProperty({})
    category_cooldowns = DictProperty({})
    current_popup = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_accessing = False

    def switch_screen(self, screen_name):
        self.parent.parent.transition = SlideTransition(direction='left')
        self.parent.parent.current = screen_name

    def access_category(self, category):
        current_time = time.time()
        if category in self.category_cooldowns and current_time - self.category_cooldowns[category] < 1:
            return

        if category in self.category_timers:
            self.category_timers[category].cancel()

        self.update_category_button_state(category, True)
        print(f"Accediendo a la categoría: {category}")

        if category in self.category_cache:
            Clock.schedule_once(partial(self.show_cached_events, category), 0.1)
        else:
            self.category_timers[category] = Clock.schedule_once(partial(self._delayed_category_access, category), 0.5)

    def _delayed_category_access(self, category, dt):
        try:
            response = requests.get(f"{BACKEND_URL}/consultar-eventos/{category}")
            if response.status_code == 200:
                events = response.json()
                self.category_cache[category] = events
                self.show_events_popup(category, events)
            else:
                self.show_popup("Error", f"No se pudieron obtener los eventos de la categoría {category}")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))
        finally:
            self.update_category_button_state(category, False)
            self.category_cooldowns[category] = time.time()

    def show_cached_events(self, category, dt):
        events = self.category_cache[category]
        self.show_events_popup(category, events)
        self.update_category_button_state(category, False)
        self.category_cooldowns[category] = time.time()

    def update_category_button_state(self, category, is_loading):
        button_id = f'{category.lower().replace(" ", "_")}_button'
        button = self.ids.get(button_id)
        if button:
            button.disabled = is_loading
            button.opacity = 0.5 if is_loading else 1

    def show_events_popup(self, category, events):
        if self.current_popup:
            self.current_popup.dismiss()
        self.current_popup = EventsPopup(category, events)
        self.current_popup.open()

    def update_buttons(self):
        app = App.get_running_app()
        self.ids.login_button.opacity = 1 if not app.is_logged_in else 0
        self.ids.login_button.disabled = app.is_logged_in
        self.ids.reserva_button.opacity = 1 if app.is_logged_in else 0
        self.ids.reserva_button.disabled = not app.is_logged_in
        self.ids.logout_button.opacity = 1 if app.is_logged_in else 0
        self.ids.logout_button.disabled = not app.is_logged_in
#        self.ids.crear_evento_button.opacity = 1 if app.is_logged_in and app.is_admin else 0
#        self.ids.crear_evento_button.disabled = not (app.is_logged_in and app.is_admin)

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

    def logout(self):
        app = App.get_running_app()
        app.is_logged_in = False
        app.username = ''
        self.parent.parent.transition = SlideTransition(direction='right')
        self.parent.parent.current = 'Root'
        
        login_screen = app.root.get_screen('Log')
        if hasattr(login_screen, 'ids') and 'username' in login_screen.ids:
            login_screen.ids.username.text = ''
        if hasattr(login_screen, 'ids') and 'password' in login_screen.ids:
            login_screen.ids.password.text = ''
        
        self.update_buttons()

    def busqueda_eventos(self, texto_ingresado):
        if not texto_ingresado.strip():
            self.show_popup("Error", "Por favor, ingresa un término de búsqueda")
            return

        try:
            response = requests.get(f"{BACKEND_URL}/consultar-eventos")
            response.raise_for_status()
            eventos = response.json()

            eventos_filtrados = []
            for evento in eventos: 
                if texto_ingresado.lower() in evento.get('nombre_evento', '').lower():
                    eventos_filtrados.append(evento)

            if eventos_filtrados:
                popup = BusquedaEventosPopup(busqueda=texto_ingresado, events=eventos_filtrados)
                popup.open()
            else:
                self.show_popup("Sin resultados", "No se encontraron eventos que coincidan con la búsqueda.")

        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))

class Reserva(BoxLayout):
    def switch_root(self):
        self.parent.parent.transition = SlideTransition(direction='right')
        self.parent.parent.current = 'Root'

    def check_reservation(self, id_reserva):
        App.get_running_app().root.get_screen('Res').check_reservation(id_reserva)

    def delete_reservation(self, id_reserva):
        if not id_reserva:
            self.show_popup("Error", "Por favor, ingrese un ID de reserva")
            return

        try:
            response = requests.delete(f"{BACKEND_URL}/eliminar-reserva/{id_reserva}")
            if response.status_code == 200:
                self.show_popup("Éxito", "La reserva ha sido eliminada correctamente")
                Clock.schedule_once(lambda dt: self.clear_reservation_info(), 2)
            elif response.status_code == 404:
                self.show_popup("Error", f"No se encontró una reserva con el ID {id_reserva}")
            else:
                self.show_popup("Error", "Error al eliminar la reserva")
        except requests.exceptions.RequestException as e:
            self.show_popup("Error de conexión", str(e))

    def clear_reservation_info(self):
        self.ids.idreserva.text = ''
    
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
                app = App.get_running_app()
                app.is_logged_in = True
                app.username = username
                app.is_admin = data.get('es_admin', False)
                self.switch_root()
                app.root.get_screen('Root').ids.my_root.update_buttons()
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
    username = StringProperty('')
    is_admin = BooleanProperty(False)

    def build(self):
        Builder.load_file('templates/universe.kv')

        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(RootScreen(name='Root'))
        self.screen_manager.add_widget(ReservaScreen(name='Res'))
        self.screen_manager.add_widget(LoginScreen(name='Log'))
        #self.screen_manager.add_widget(CrearEventoScreen(name='CrearEvento'))

        return self.screen_manager

if __name__ == "__main__":
    UniverseApp().run()
