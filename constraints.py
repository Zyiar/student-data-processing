def validate_name(student_name):
    if not student_name or len(student_name.split()) < 2:
        raise ValueError("Student name should contain at least two parts.")
