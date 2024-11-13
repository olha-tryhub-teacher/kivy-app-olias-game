from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

from random import randint, shuffle

import text
from buttons import AnimatedButton, AnswerButton


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bg_img = Image(source="images/backgrounds/main.jpg",
                       allow_stretch=True,
                       keep_ratio=False,
                       size_hint=(1, 1))
        hello_lbl = Label(text=text.hello_text, halign="center", font_size="30px")
        question1_btn = Button(background_normal="images/normal_buttons/Arrow-Up.png",
                               background_down="images/down_buttons/Arrow-Up.png",
                               size_hint=(None, None),
                               height=150,
                               width=150,
                               pos_hint={"center_x": 0.5, "top": 1})
        question2_btn = Button(background_normal="images/normal_buttons/Arrow-Left.png",
                               background_down="images/down_buttons/Arrow-Left.png",
                               size_hint=(None, None),
                               height=150,
                               width=150,
                               pos_hint={"center_y": 0.5, "left": 1})
        question3_btn = Button(background_normal="images/normal_buttons/Arrow-Right.png",
                               background_down="images/down_buttons/Arrow-Right.png",
                               size_hint=(None, None),
                               height=150,
                               width=150,
                               pos_hint={"center_y": 0.5, "right": 1})
        question4_btn = Button(background_normal="images/normal_buttons/Arrow-Down.png",
                               background_down="images/down_buttons/Arrow-Down.png",
                               size_hint=(None, None),
                               height=150,
                               width=150,
                               pos_hint={"center_x": 0.5, "bottom": 1})

        question1_btn.on_press = self.go_up
        question2_btn.on_press = self.go_left
        question3_btn.on_press = self.go_right
        question4_btn.on_press = self.go_down

        main_layout = FloatLayout()
        main_layout.add_widget(bg_img)

        main_layout.add_widget(question1_btn)
        main_layout.add_widget(question2_btn)
        main_layout.add_widget(hello_lbl)
        main_layout.add_widget(question3_btn)
        main_layout.add_widget(question4_btn)

        self.add_widget(main_layout)

    def go_up(self):
        self.manager.transition.direction = "down"
        self.manager.current = "UpScreen"

    def go_left(self):
        self.manager.transition.direction = "right"
        self.manager.current = "LeftScreen"

    def go_right(self):
        self.manager.transition.direction = "left"
        self.manager.current = "RightScreen"

    def go_down(self):
        self.manager.transition.direction = "up"
        self.manager.current = "DownScreen"


class UpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bg_img = Image(source="images/backgrounds/up.jpg",
                       allow_stretch=True,
                       keep_ratio=False,
                       size_hint=(1, 1))

        bg_layout = FloatLayout()
        bg_layout.add_widget(bg_img)

        main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        question_line1 = BoxLayout(orientation="horizontal", padding=8, spacing=8)
        question_line2 = BoxLayout(orientation="horizontal", padding=8, spacing=8)

        to_menu_btn = Button(background_normal="images/normal_buttons/Arrow-Down.png",
                             background_down="images/down_buttons/Arrow-Down.png",
                             size_hint=(None, None),
                             height=150,
                             width=150,
                             pos_hint={"center_x": 0.5, "bottom": 1})
        to_menu_btn.on_press = self.go_down

        self.question = text.questions_up[randint(0, 2)]
        self.question_lbl = Label(text=self.question[0], font_size="30px", pos_hint={"x_center": .5})
        self.result_lbl = Label(text="", font_size="30px", pos_hint={"x_center": .5})

        self.right_answer = AnswerButton(text=self.question[1], font_size="30px", lbl_result=self.result_lbl,
                                         is_right=True)
        self.wrong_answer1 = AnswerButton(text=self.question[2], font_size="30px", lbl_result=self.result_lbl,
                                          is_right=False)
        self.wrong_answer2 = AnswerButton(text=self.question[3], font_size="30px", lbl_result=self.result_lbl,
                                          is_right=False)
        self.wrong_answer3 = AnswerButton(text=self.question[4], font_size="30px", lbl_result=self.result_lbl,
                                          is_right=False)

        self.answers = [self.right_answer, self.wrong_answer1, self.wrong_answer2, self.wrong_answer3]
        shuffle(self.answers)
        question_line1.add_widget(self.answers[0])
        question_line1.add_widget(self.answers[1])
        question_line2.add_widget(self.answers[2])
        question_line2.add_widget(self.answers[3])

        main_layout.add_widget(self.question_lbl)
        main_layout.add_widget(self.result_lbl)
        main_layout.add_widget(question_line1)
        main_layout.add_widget(question_line2)
        main_layout.add_widget(to_menu_btn)

        bg_layout.add_widget(main_layout)
        self.add_widget(bg_layout)

    def go_down(self):
        self.question = text.questions_up[randint(0, len(text.questions_up) - 1)]
        self.result_lbl.text = ""
        self.question_lbl.text = self.question[0]
        self.right_answer.text = self.question[1]
        self.wrong_answer1.text = self.question[2]
        self.wrong_answer2.text = self.question[3]
        self.wrong_answer3.text = self.question[4]
        self.manager.transition.direction = "up"
        self.manager.current = "MainScreen"


class LeftScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bg_img = Image(source="images/backgrounds/left.jpg",
                       allow_stretch=True,
                       keep_ratio=False,
                       size_hint=(1, 1))
        bg_layout = FloatLayout()
        bg_layout.add_widget(bg_img)
        self.add_widget(bg_layout)

        to_menu_btn = Button(background_normal="images/normal_buttons/Arrow-Right.png",
                             background_down="images/down_buttons/Arrow-Right.png",
                             size_hint=(None, None),
                             height=150,
                             width=150,
                             pos_hint={"center_y": 0.5, "right": 1})
        to_menu_btn.on_press = self.go_right

        self.random_int = randint(0, 100)
        lbl_instr = Label(text="Відгадай число 0 до 100!", font_size="30px", pos_hint={"x_center": .5})
        lbl_your_num = Label(text="Введи сюди твоє число", font_size="30px", halign="right", pos_hint={"x_center": .5})
        self.input_num = TextInput(font_size="30px", size_hint=(1, .5), pos_hint={"y_center": .5})
        self.lbl_result = Label(text="", font_size="30px", pos_hint={"x_center": .5})
        self.btn_check_res = Button(text="Відгадати", font_size="30px",
                                    pos_hint={"x_center": .5}, width=250, height=150)
        self.btn_check_res.on_press = self.check_res

        main_layout = BoxLayout(orientation="horizontal", padding=8, spacing=8)
        question_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        question_line = BoxLayout(orientation="horizontal", padding=8, spacing=8)

        question_layout.add_widget(lbl_instr)

        question_line.add_widget(lbl_your_num)
        question_line.add_widget(self.input_num)

        question_layout.add_widget(question_line)
        question_layout.add_widget(self.lbl_result)
        question_layout.add_widget(self.btn_check_res)

        main_layout.add_widget(question_layout)
        main_layout.add_widget(to_menu_btn)
        bg_layout.add_widget(main_layout)

    def check_res(self):
        try:
            num = int(self.input_num.text)
            if num > self.random_int:
                self.lbl_result.color = (1, 0, 0, 1)
                self.lbl_result.text = "Спробуй менше"
            elif num < self.random_int:
                self.lbl_result.color = (1, 0, 0, 1)
                self.lbl_result.text = "Спробуй більше"
            else:
                self.lbl_result.color = (0, 1, 0, 1)
                self.lbl_result.text = "Ура! Відгадав!"
        except:
            self.lbl_result.color = (1, 0, 0, 1)
            self.lbl_result.text = "Треба вводити число!"

    def go_right(self):
        self.manager.transition.direction = "left"
        self.manager.current = "MainScreen"
        self.lbl_result.text = ""
        self.random_int = randint(0, 100)
        self.input_num.text = ""


class RightScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bg_img = Image(source="images/backgrounds/right.jpg",
                       allow_stretch=True,
                       keep_ratio=False,
                       size_hint=(1, 1))

        bg_layout = FloatLayout()
        bg_layout.add_widget(bg_img)

        to_menu_btn = Button(background_normal="images/normal_buttons/Arrow-Left.png",
                             background_down="images/down_buttons/Arrow-Left.png",
                             size_hint=(None, None),
                             height=150,
                             width=150,
                             pos_hint={"center_y": 0.5, "left": 1})
        to_menu_btn.on_press = self.go_left

        story = text.stories_right[randint(0, len(text.stories_right) - 1)]
        lbl_instructions = Label(text=text.instructions_right, font_size="25px", pos_hint={"x_center": .5})
        scrl_text = ScrollView(size_hint=(1, None), size=(400, 300))
        text_layout = GridLayout(cols=1, size_hint_y=None)
        text_layout.bind(minimum_height=text_layout.setter("height"))
        self.lbl_story = Label(text=story[0], font_size="25px", size_hint_y=None, text_size=(400, None),
                               halign="left", valign="top")
        self.lbl_story.bind(texture_size=self.lbl_story.setter("size"))
        text_layout.add_widget(self.lbl_story)

        scrl_text.add_widget(text_layout)

        self.question = Label(text=story[1], font_size="30px", pos_hint={"x_center": .5})
        self.result_lbl = Label(text="", font_size="30px", pos_hint={"x_center": .5})
        self.btn_true_answer = AnswerButton(text="Правда", font_size="30px", lbl_result=self.result_lbl,
                                            is_right=story[2])
        self.btn_false_answer = AnswerButton(text="Неправда", font_size="30px", lbl_result=self.result_lbl,
                                             is_right=not story[2])

        main_layout = BoxLayout(orientation="horizontal", padding=8, spacing=8)
        story_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        answer_line = BoxLayout(orientation="horizontal", padding=8, spacing=8)

        story_layout.add_widget(lbl_instructions)
        story_layout.add_widget(scrl_text)
        story_layout.add_widget(self.question)
        story_layout.add_widget(self.result_lbl)

        answer_line.add_widget(self.btn_true_answer)
        answer_line.add_widget(self.btn_false_answer)

        story_layout.add_widget(answer_line)

        main_layout.add_widget(to_menu_btn)
        main_layout.add_widget(story_layout)

        bg_layout.add_widget(main_layout)

        self.add_widget(bg_layout)

    def go_left(self):
        story = text.stories_right[randint(0, len(text.stories_right) - 1)]
        self.lbl_story.text = story[0]
        self.question.text = story[1]
        self.btn_true_answer.is_right = story[2]
        self.btn_false_answer.is_right = not story[2]
        self.result_lbl.text = ""

        self.manager.transition.direction = "right"
        self.manager.current = "MainScreen"


class DownScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bg_img = Image(source="images/backgrounds/down.jpg",
                       allow_stretch=True,
                       keep_ratio=False,
                       size_hint=(1, 1))

        bg_layout = FloatLayout()
        bg_layout.add_widget(bg_img)

        to_menu_btn = Button(background_normal="images/normal_buttons/Arrow-Up.png",
                             background_down="images/down_buttons/Arrow-Up.png",
                             size_hint=(None, None),
                             height=150,
                             width=150,
                             pos_hint={"center_x": 0.5, "top": 1})
        to_menu_btn.on_press = self.go_up
        lbl_instructions = Label(text="Скоріше! Упіймай кнопку!", font_size="25px", pos_hint={"x_center": .5, "top": 1})
        btn_animated = AnimatedButton()
        btn_animated.start_animation()

        main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_layout.add_widget(to_menu_btn)
        main_layout.add_widget(lbl_instructions)
        main_layout.add_widget(btn_animated)
        bg_layout.add_widget(main_layout)
        self.add_widget(bg_layout)

    def go_up(self):
        self.manager.transition.direction = "down"
        self.manager.current = "MainScreen"
