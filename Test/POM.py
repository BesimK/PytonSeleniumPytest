import pytest
from Main.Pages.HomePage import HomePage
from Test.Hooks import hooks


@pytest.mark.usefixtures("hooks")
def test_wiki_test():
    homePage = HomePage()
    homePage.do_the_trick()
