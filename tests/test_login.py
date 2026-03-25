import pytest
from pages.loginpage import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login_page_title(self):
        login_page = LoginPage(self.driver)
        assert "Google" in login_page.get_title()
