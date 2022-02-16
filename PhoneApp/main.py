import json
import glob
import random
from datetime import datetime
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior





Builder.load_file('design.kv')

class LoginScreen(Screen):
    """Displays the login screen for the quote app."""
    def sign_up(self):
        """Method that defines the instructions for the sign up button."""
        self.manager.current = "sign_up_screen"
    
    def login(self, uname, pword):
        """Method that defines the instructions for the login button."""
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong user or password :("
    
    def forgot_password(self):
        """Method that defines the instructions for the forgot password button."""
        self.manager.current = "forgot_password_screen"

class ForgotPasswordScreen(Screen):
    """Displays the forgot password screen for the quote app."""
    def back_to_login(self):
        """Defines the back to login button instructions"""
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def security_question(self, uname, maiden_name):
        """Defines the security question button enter button"""
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['maiden'] == maiden_name:
            self.ids.name_response.text = f"your password is: {users[uname]['password']}"
        else:
            self.ids.name_response.text = "That username and security answer do not match."

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
    def add_user(self, uname, pword, mname):
        """Method that defines the instructions for the add user button."""
        with open("users.json") as file:
            users = json.load(file)
        mname = mname.lower()
        users[uname] = {'username': uname, 'password': pword, 'maiden': mname, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
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
