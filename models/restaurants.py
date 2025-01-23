from models.assessments import Assessments

class Restaurants:
    """..."""

    restaurant = []

    def __init__(self, name, category): # "self" can be any word...
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._assessment = []
        Restaurants.restaurant.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def restaurant_list(cls):
        print(f'{'name'.ljust(25)} | {'category'.ljust(25)} | {'assessment'.ljust(25)} | {'status'}')
        for r in cls.restaurant:
            print(f'{r._name.ljust(25)} | {r._category.ljust(25)} | {str(r.grade_avg).ljust(25)} | {r.restaurant_status}')

    @property
    def restaurant_status(self):
        return '✔' if self._status else '✘'
    
    def change_restaurant_status(self):
        self._status = not self._status

    def get_assesment(self, customer, grade):
        assessment = Assessments(customer, grade)
        self._assessment.append(assessment)
        #
        #if 0 < grade <= 5:
        #    a = Assessments(customer, grade)
        #    self._assessment.append(a)

    @property
    def grade_avg(self):
        if not self._assessment:
            return 'not assessments!'
        s = sum(assessment._grade for assessment in self._assessment)
        c = len(self._assessment)
        a = 5.0 if round(s / c, 1) >= 5.0 else round(s / c, 1)
        return a
