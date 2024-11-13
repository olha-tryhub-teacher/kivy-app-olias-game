from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window

from random import randint


class AnswerButton(Button):
    def __init__(self, lbl_result: Label, is_right: bool, **kwargs):
        super().__init__(**kwargs)
        self.lbl_result = lbl_result
        self.is_right = is_right

    def on_press(self):
        if self.is_right:
            self.lbl_result.color = (0, 1, 0, 1)
            self.lbl_result.text = "Відповідь правильна"
        else:
            self.lbl_result.color = (1, 0, 0, 1)
            self.lbl_result.text = "Відповідь неправильна"


class AnimatedButton(Button):
    def __init__(self, text="Упіймай мене!", height=100, width=150, **kwargs):
        super().__init__(text=text, size_hint=(None, None), height=height, width=width, **kwargs)
        self.bind(on_press=self.toggle_animation)
        self.animation = None
        self.is_animating = False

    def start_animation(self):
        if not self.is_animating:
            self.is_animating = True
            self.text = "Упіймай мене!"
            self.animate_to_random_position()

    def animate_to_random_position(self):
        new_x = randint(0, Window.width - self.width)
        new_y = randint(0, Window.height - self.height)

        self.animation = Animation(x=new_x, y=new_y, duration=1)

        self.animation.bind(on_complete=lambda *args: self.animate_to_random_position() if self.is_animating else None)

        self.animation.start(self)

    def toggle_animation(self, *args):
        if self.is_animating:
            self.is_animating = False
            self.text = "Упіймав!"
            if self.animation:
                self.animation.stop(self)
                self.animation = None
        else:
            self.start_animation()
