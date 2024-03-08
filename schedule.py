class Schedule:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    @property
    def details(self):
        return f'{self.name} {self.date}'
