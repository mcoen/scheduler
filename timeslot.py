class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    @property
    def duration(self):
        return f'{self.end_time - self.start_time}'
