# Function to calculate total course fees for SIT
def CalculateSITcourseFees(course_name, TIGans, entrance_test, Male):
    # Course data: course_code : [course_name, no_of_semesters, admission_fee, remaining_semester_fee]
    courses = {
        1: ["BTech", 8, 100000, 75000],
        2: ["BCA", 8, 70000, 50000],
        3: ["BBA", 8, 70000, 50000],
        4: ["BHHA", 6, 60000, 45000],
        5: ["BSc", 6, 50000, 30000],
        6: ["MBA", 4, 140000, 100000],
        7: ["MCA", 4, 120000, 80000]
    }

    # Extract course details
    course = courses.get(course_name)
    if course is None:
        print("Invalid course code!")
        return

    name, semesters, admission_fee, sem_fee = course

    # Initialize scholarships
    total_scholarship = 0
    first_sem_scholarship = 0

    # --- Apply Scholarship Rules ---
    # 1. If student is from Techno India Group
    if TIGans == 1:
        # UG: codes 1 to 5  → 10K per semester
        # PG: codes 6,7     → 15K per semester
        if course_name <= 5:
            sem_scholarship = 10000
        else:
            sem_scholarship = 15000
        total_scholarship += sem_scholarship * semesters
    else:
        sem_scholarship = 0

    # 2. If entrance test qualified
    if entrance_test == 1:
        first_sem_scholarship += 15000

    # 3. If female student
    if Male == 0:
        first_sem_scholarship += 10000

    # --- Fee Calculation ---
    # Adjust first semester (admission + 1st sem)
    total_first_sem_fee = admission_fee - first_sem_scholarship
    # Remaining semesters
    remaining_fee = (semesters - 1) * (sem_fee - sem_scholarship)

    total_fee = total_first_sem_fee + remaining_fee

    print(f"Course Name: {name}")
    print(f"Total Course Fee after Scholarship: ₹{total_fee:,.2f}")


# ----------------------------
# Example Test
# ----------------------------
# Example from question: BTech, TIGans=1, Male=1, entrance_test=0
CalculateSITcourseFees(1, 1, 0, 1)
