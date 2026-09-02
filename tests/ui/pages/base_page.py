class BasePage:
    path = None

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.path)