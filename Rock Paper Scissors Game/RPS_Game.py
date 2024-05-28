from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RockPaperScissors(App):
    def build(self):
        self.user_score = 0
        self.computer_score = 0

        self.layout = BoxLayout(orientation='vertical')
        self.title_label = Label(text="Rock, Paper, Scissors", font_size=24)
        self.layout.add_widget(self.title_label)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        self.user_choice_label = Label(text="")
        self.layout.add_widget(self.user_choice_label)

        self.computer_choice_label = Label(text="")
        self.layout.add_widget(self.computer_choice_label)

        button_layout = BoxLayout(orientation='horizontal')

        rock_button = Button(text='Rock')
        rock_button.bind(on_press=lambda instance: self.play_round(1))
        button_layout.add_widget(rock_button)

        paper_button = Button(text='Paper')
        paper_button.bind(on_press=lambda instance: self.play_round(2))
        button_layout.add_widget(paper_button)

        scissors_button = Button(text='Scissors')
        scissors_button.bind(on_press=lambda instance: self.play_round(3))
        button_layout.add_widget(scissors_button)

        self.layout.add_widget(button_layout)

        return self.layout

    def play_round(self, user_choice):
        computer_choice = random.randint(1, 3)
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.text = result
        self.user_choice_label.text = f"You chose: {choices[user_choice]}"
        self.computer_choice_label.text = f"Computer chose: {choices[computer_choice]}"

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            return "You win!"
        else:
            return "You lose!"

    def on_stop(self):
        print("Final Score:")
        print(f"Your score: {self.user_score}")
        print(f"Computer's score: {self.computer_score}")

if __name__ == '__main__':
    RockPaperScissors().run()
