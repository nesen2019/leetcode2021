import os
class LoginMsg:
    def __init__(self):
        self.email = "nihaoma-u"
        self.password = "w2849337909"
        self.proxy_dict = dict(
            http="http://127.0.0.1:1081/",
            https="https://127.0.0.1:1081/"
        )


class LeetCode:
    def __init__(self):
        self.PATH_PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.LOGINmsg = LoginMsg()


cfg = LeetCode()