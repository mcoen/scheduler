class Clinician:
    def __init__(self, first_name, last_name, role, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.employee_id = employee_id

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.role} {self.employee_id}'

    @property
    def name(self):
        return f'{self.last_name}, {self.first_name}, {self.role}, {self.employee_id}'
