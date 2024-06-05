from Main.Pages.HomePage import HomePage


class Pages:
    def __init__(self):
        self._homepage = HomePage()

    def get_homepage(self):
        return self._homepage
