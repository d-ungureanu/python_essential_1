class Employee:

    def __init__(self, fn, ln, d, m, y, pos, grad, ids):
        self.first_name = fn
        self.last_name = ln
        self.birth_day = d
        self.birth_month = m
        self.birth_year = y
        self.position = pos
        self.graduated = grad
        self.ids = ids

    def set_first_name(self, firstname):
        self.first_name = firstname

    def set_last_name(self, lastname):
        self.last_name = lastname

    def set_birth_day(self, birthday):
        self.birth_day = birthday

    def set_birth_month(self, birthmonth):
        self.birth_month = birthmonth

    def set_birth_year(self, birthyear):
        self.birth_year = birthyear

    def set_position(self, pos):
        self.position = pos

    def set_graduation(self, grad):
        self.graduated = grad

    def set_ids(self, emplid):
        self.ids = emplid
