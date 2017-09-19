class Student:
    def __init__(self, last_name, first_name, status, scheduled_hours, financial_status, ADA_req=None ):
        self.last_name = last_name
        self.first_name = first_name
        self.status = status
        self.scheduled_hours = scheduled_hours
        self.financial_status = financial_status
        self.ADA_req = ADA_req
        self.schedule = []

    def add_course(self, course):
        added = course.add_student(self)
        if added == "Student added to course roster.":
            if self.ADA_req:
                if course.room.ADA_access == None:
                    course.note = "Student requiring ADA access enrolled.  Room not equipped."
                    print("This classroom does not meet ADA.  Please call the department or instructor to request a change.")

            self.schedule.append(course)
            return "Course added to student schedule."
        return "Course enrollment full."


class Classroom:
    def __init__(self, building, room_number, capacity, ADA_access=None):
        self.building = building
        self.room_number = room_number
        self.capacity = capacity
        self.ADA_access = ADA_access

class Course:
    def __init__(self, department, title, hours, capacity, room=None):
        self.department = department
        self.title = title
        self.hours = hours
        self.room = room
        self.capacity = capacity
        self.roster = []
        self.note = ""

    def add_student(self, student):
        if len(self.roster) < self.room.capacity:
            self.roster.append(student)
            return "Student added to course roster."
        else:
            return "The classroom only holds {}. {} students are enrolled".format(self.room.capacity, str(len(self.roster)))


if __name__ == '__main__':

    student0001 = Student("West", "Jane", "Enrolled, Full-Time", 0, "Paid In Full")
    student0002 = Student("Parker", "Sam", "Enrolled, Part-Time", 0, "Pending", "ADA")
    student0003 = Student("Vole", "Jennifer", "Hiatus", 0, "Hiatus")

    westhall = Classroom("Samstead", "189B", 2)

    foodjustice = Course("Interdisciplinary Studies", "Food Justice", 4, None, 4)

    foodjustice.room = westhall

    student0001.add_course(foodjustice)
    student0002.add_course(foodjustice)
    student0003.add_course(foodjustice)

    print(foodjustice.note)
    print(foodjustice.roster)
    print(len(foodjustice.roster))
    print(foodjustice.room.capacity)


