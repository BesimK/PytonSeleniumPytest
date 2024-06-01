from Main.Pages.HomePage import HomePage


class Pages:
    _homepage = HomePage()

    @staticmethod
    def get_homepage():
        return Pages._homepage
