from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import random

class RockPaperScissors(App):
    def build(self):
        self.user_score = 0
        self.computer_score = 0

        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title label
        title_label = Label(text="Rock, Paper, Scissors", font_size=24, size_hint=(1, 0.2))
        self.layout.add_widget(title_label)

        # Result label
        self.result_label = Label(text="", font_size=20, size_hint=(1, 0.1))
        self.layout.add_widget(self.result_label)

        # Choices layout
        choices_layout = GridLayout(cols=3, spacing=20, size_hint=(1, 0.4))

        # Add buttons for choices
        for choice in ["Rock", "Paper", "Scissors"]:
            btn = Button(text=choice, font_size=20)
            btn.bind(on_press=self.play_round)
            choices_layout.add_widget(btn)

        self.layout.add_widget(choices_layout)

        # User and computer choice labels
        self.user_choice_label = Label(text="", font_size=16, size_hint=(1, 0.1))
        self.computer_choice_label = Label(text="", font_size=16, size_hint=(1, 0.1))
        self.layout.add_widget(self.user_choice_label)
        self.layout.add_widget(self.computer_choice_label)

        # User and computer score labels
        self.user_score_label = Label(text=f"Your Score: {self.user_score}", font_size=18, size_hint=(1, 0.1))
        self.computer_score_label = Label(text=f"Computer Score: {self.computer_score}", font_size=18, size_hint=(1, 0.1))
        self.layout.add_widget(self.user_score_label)
        self.layout.add_widget(self.computer_score_label)

        return self.layout

    def play_round(self, instance):
        user_choice = instance.text
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Update labels with user and computer choices
        self.user_choice_label.text = f"You chose: {user_choice}"
        self.computer_choice_label.text = f"Computer chose: {computer_choice}"

        # Determine the winner
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.text = result

        # Update scores
        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        # Update score labels
        self.user_score_label.text = f"Your Score: {self.user_score}"
        self.computer_score_label.text = f"Computer Score: {self.computer_score}"

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "You lose!"

if __name__ == '__main__':
    RockPaperScissors().run()