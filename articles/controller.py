from view import UserUnterface

class Controller:
    def __init__(self):
        self.article_model = None
        self.user_interface = UserUnterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()