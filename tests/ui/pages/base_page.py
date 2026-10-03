import allure


class BasePage:
    path = None

    def __init__(self, page):
        self.page = page

    @allure.step("Open page")
    def open(self):
        self.page.goto(self.path)