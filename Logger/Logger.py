class Logger:
    isLogged = False

    def __init__(self):
        pass

    def loggin(self, user, password, bd):
        if user in bd.users.keys() and bd.check_user(user,password):
            self.isLogged = True
        else:
            print("Intente de nuevo")
