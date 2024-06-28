class Scheduler(object):
    def __init__(self, classlist):
        self.classlist = classlist

    def schedule(self, start_time, end_time):
        # Sort the courses by the end time.
        sorted_courses = sorted(self.classlist, key=lambda x: x[1])

        # Track the max num of courses using variable num_classes.
        num_courses = 0
        current_end_time = start_time

        #  Using loop to check whether the course's start time is
        #  at least 10 units later than the current_end_time.
        for courses in sorted_courses:

            if courses[0] >= current_end_time + 10 and courses[1] < end_time:
                # Update the current end time to the end time of the current course.
                current_end_time = courses[1]
                # Increment the number of courses.
                num_courses += 1

        # Return the maximum number of courses that can be taken.
        return num_courses
