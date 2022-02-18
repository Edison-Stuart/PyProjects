import os
import glob
import random
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
from password import hash_password, DataBase
from password import validate_password




db = DataBase("users.db")
Builder.load_file('design.kv')

class LoginScreen(Screen):
    """Displays the login screen for the quote app."""
    def sign_up(self):
        """Method that defines the instructions for the sign up button."""
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        """Method that defines the instructions for the login button."""
        saved_code = db.view_user_login_data(uname)[0]

        my_salt = saved_code[0][:32]
        my_saved_password = saved_code[0][32:]
    
        my_hashed_pword = validate_password(pword, my_saved_password, my_salt)
        if my_hashed_pword is True:
            self.manager.transition.direction = 'left'
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong password"
    
    def forgot_password(self):
        """Method that defines the instructions for the forgot password button."""
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password_screen"

class ForgotPasswordScreen(Screen):
    """Displays the forgot password screen for the quote app."""
    def back_to_login(self):
        """Defines the back to login button instructions"""
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def security_question_answer(self, answer, uname):
        """Method that defines the button for the final security question"""
        try:
            user_info = db.view_user_security_data(uname)
            if answer == user_info[0][1]:
                self.manager.current = "change_password_screen"
                self.ids.name_response.text = "That is not a correct security answer"
        except:
            self.ids.name_response.text = "That username is not in our file"

class ChangePasswordScreen(Screen):
    """Class that displays a change password screen for the app"""
    def change_password(self, uname, pword):
        """Method that defines the instructions for the change password button"""
        
        my_salt = os.urandom(32)
        hashed_pword = hash_password(pword, my_salt)
        key_combo = my_salt + hashed_pword
        db.update_password(key_combo, uname)
        self.ids.password_response_label.text = "Your password has been reset!"
    
    def back_to_login(self):
        """A method that moves us back to the login screen"""
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    """Displays the Login Success screen for the quote app."""
    def log_out(self):
        """Method that defines the instructions for the log out button."""
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def get_quote(self, feel):
        """Method that defines the instructions for the get quote button."""
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "That isn't a feeling you idiot!"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    """This class allows us to have a special button animation"""
    pass

class SignUpScreen(Screen):
    """Displays the sign up screen for the quote app."""
    def add_user(self, uname, pword, answer):
        """Method that defines the instructions for the add user button."""
        my_salt = os.urandom(32)
        hashed_pword = hash_password(pword, my_salt)
        key_combo = my_salt + hashed_pword

        db.insert(uname,key_combo,answer)
        self.manager.current = "sign_up_screen_success"

    def back_to_login(self):
        """Method that defines the instructions for the back to login button."""
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    """Displays the sign up success screen for the quote app."""
    def back_to_login(self):
        """Method that defines the instructions for the back to login button."""
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    """Class that is connected to the kivy screen manager and helps us control the various screens."""
    pass

class MainApp(App):
    """Class that runs all of our code and returns the app."""
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
