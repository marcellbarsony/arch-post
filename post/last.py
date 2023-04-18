class Last():

    """Docstring for Last"""

    def __init__(self, user):
        self.user = user

    def cleanHome(self):
        files = ['.bash_history', '.bash_logout', '.bash_profile', '.bashrc']
        for file in files:
            print(file)

