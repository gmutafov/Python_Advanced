def gather_credits(number_of_credits, *args):
    curr_credits = 0
    courses_enrolled = {}

    for course_name, credits in args:
        if curr_credits < number_of_credits:
            if course_name in courses_enrolled:
                continue
            courses_enrolled[course_name] = credits
            curr_credits += credits
        else:
            break

    if curr_credits >= number_of_credits:
        return f"Enrollment finished! Maximum credits: {curr_credits}.\nCourses: {', '.join(sorted(courses_enrolled))}"

    return f"You need to enroll in more courses! You have to gather {number_of_credits - curr_credits} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
