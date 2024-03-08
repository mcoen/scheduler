class SchedulableResource:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.name}'
