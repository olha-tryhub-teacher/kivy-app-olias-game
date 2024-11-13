from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import MainScreen, UpScreen, LeftScreen, RightScreen, DownScreen


class OliasGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="MainScreen"))
        sm.add_widget(UpScreen(name="UpScreen"))
        sm.add_widget(LeftScreen(name="LeftScreen"))
        sm.add_widget(RightScreen(name="RightScreen"))
        sm.add_widget(DownScreen(name="DownScreen"))

        return sm


app = OliasGameApp()
app.run()
