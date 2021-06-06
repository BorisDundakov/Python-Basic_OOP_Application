class UniversityStudent:
    n_students = 0

    def __init__(self, first_name, last_name, age, fac_number, specialty, nationality, year, qualification):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fac_number = fac_number
        self.specialty = specialty
        self.nationality = nationality
        self.year = year
        self.qualification = qualification
        self.university_email = first_name[0] + '.' + last_name + '@universiltyName.com'

        UniversityStudent.n_students += 1

    def start_year(self):
        # in my university, the first 2 numbers of the faculty number are the last 2 digitis of the enrollment year of
        # the student
        return '20{}{}'.format(self.fac_number[0], self.fac_number[1])

    def predicted_graduation(self):
        if self.qualification == 'Bachelor':
            int_result = int(self.fac_number[0] + self.fac_number[1]) + 4
            final_result = '20' + str(int_result)
            return final_result

        elif self.qualification == 'Master':
            int_result = int(self.fac_number[0] + self.fac_number[1]) + 4
            final_result = '20' + str(int_result)
            return final_result


student_1 = UniversityStudent('Boris', 'Dundakov', 22, '18114052', 'Business Informatics', 'Bulgarian', 3, 'Bachelor')
student_2 = UniversityStudent('Anton', 'Nedyalkov', 28, '20111111', 'Journalism', 'Bulgarian', 1, 'Bachelor')

print(student_1.__dict__)
print(student_1.year)
print(student_1.start_year())
print(student_1.predicted_graduation())
print(student_1.university_email)
print(UniversityStudent.n_students)
