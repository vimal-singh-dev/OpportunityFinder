
# ============================================
# OPPORTUNITYFINDER AGENT
# ============================================


# ============================================
# 1. INPUT VALIDATION FUNCTIONS
# ============================================


def get_required_text(message):
    """
    Ask the user for text.
    The user cannot leave the field empty.
    """

    while True:

        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty. Please try again.")


def get_number(message, minimum=0):
    """
    Ask the user for a number.
    The number must be greater than or equal to minimum.
    """

    while True:

        value = input(message).strip()

        try:

            number = float(value)

            if number >= minimum:
                return number

            print(
                f"Please enter a number greater than "
                f"or equal to {minimum}."
            )

        except ValueError:

            print("Please enter a valid number.")


def get_yes_no(message):
    """
    Ask the user a yes/no question.
    Returns True for yes and False for no.
    """

    while True:

        value = input(message).strip().lower()

        if value == "yes":
            return True

        elif value == "no":
            return False

        else:
            print("Please enter yes or no.")


def get_list(message):
    """
    Ask the user for comma-separated values.
    Converts the input into a list.
    """

    while True:

        value = input(message).strip()

        if value != "":

            items = [
                item.strip()
                for item in value.split(",")
                if item.strip() != ""
            ]

            if len(items) > 0:
                return items

        print(
            "Please enter at least one value."
        )


def get_job_types():
    """
    Ask the user which types of opportunities
    they are interested in.
    """

    while True:

        print("\nWhat type of opportunities are you looking for?")

        print("1. Internship")
        print("2. Full-time")
        print("3. Both")

        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":

            return ["internship"]

        elif choice == "2":

            return ["full-time"]

        elif choice == "3":

            return [
                "internship",
                "full-time"
            ]

        else:

            print(
                "Invalid choice. Please choose 1, 2, or 3."
            )


# ============================================
# 2. PROGRAM START
# ============================================


print("==========================================")
print("        OPPORTUNITYFINDER AGENT")
print("==========================================")

print("\nLet's create your profile.\n")


# ============================================
# 3. PERSONAL INFORMATION
# ============================================

print("---------- PERSONAL INFORMATION ----------")

name = get_required_text("Name: ")

email = get_required_text("Email: ")

phone = get_required_text("Phone: ")


# ============================================
# 4. EDUCATION
# ============================================

print("\n---------- EDUCATION ----------")

degree = get_required_text("Degree: ")

field = get_required_text("Field / Branch: ")

university = get_required_text("University: ")

graduation_year = get_number(
    "Graduation year: ",
    minimum=1900
)


# ============================================
# 5. CAREER INFORMATION
# ============================================

print("\n---------- CAREER INFORMATION ----------")

skills = get_list(
    "Skills (separate with commas): "
)

experience = get_required_text(
    "Experience (if none, enter 'Fresher'): "
)

preferred_roles = get_list(
    "Preferred job roles (separate with commas): "
)


# ============================================
# 6. JOB TYPE CONSTRAINT
# ============================================

job_types = get_job_types()


# ============================================
# 7. LOCATION CONSTRAINT
# ============================================

print("\n---------- LOCATION PREFERENCES ----------")

preferred_locations = get_list(
    "Preferred locations (separate with commas): "
)

remote_allowed = get_yes_no(
    "Are you open to remote opportunities? (yes/no): "
)

max_distance_km = get_number(
    "Maximum distance you're willing to travel (km): ",
    minimum=0
)


# ============================================
# 8. COMPENSATION CONSTRAINTS
# ============================================

print("\n---------- COMPENSATION ----------")

minimum_stipend = get_number(
    "Minimum acceptable internship stipend: ",
    minimum=0
)

minimum_salary = get_number(
    "Minimum acceptable annual salary: ",
    minimum=0
)


# ============================================
# 9. SKILL-GAP OPPORTUNITIES
# ============================================

print("\n---------- SKILL-GAP OPPORTUNITIES ----------")

allow_skill_gap = get_yes_no(
    "Should I show opportunities where you "
    "are missing some skills? (yes/no): "
)


# ============================================
# 10. APPLICATION SETTINGS
# ============================================

print("\n---------- APPLICATION SETTINGS ----------")

require_approval = get_yes_no(
    "Require your approval before submitting "
    "an application? (yes/no): "
)


max_applications_per_day = get_number(
    "Maximum applications per day: ",
    minimum=1
)


# ============================================
# 11. CREATE USER PROFILE
# ============================================

user_profile = {

    "personal": {

        "name": name,

        "email": email,

        "phone": phone
    },


    "education": {

        "degree": degree,

        "field": field,

        "university": university,

        "graduation_year": graduation_year
    },


    "career": {

        "skills": skills,

        "experience": experience,

        "preferred_roles": preferred_roles
    },


    "constraints": {

        "job_types": job_types,


        "location": {

            "preferred_locations": preferred_locations,

            "remote_allowed": remote_allowed,

            "max_distance_km": max_distance_km
        },


        "compensation": {

            "minimum_stipend": minimum_stipend,

            "minimum_salary": minimum_salary
        },


        "skill_gap": {

            "allowed": allow_skill_gap
        },


        "application": {

            "require_approval": require_approval,

            "max_applications_per_day":
                max_applications_per_day
        }
    }
}


# ============================================
# 12. DISPLAY PROFILE
# ============================================

print("\n")
print("==========================================")
print("          PROFILE CREATED")
print("==========================================")


print("\nPERSONAL INFORMATION")

print(
    "Name:",
    user_profile["personal"]["name"]
)

print(
    "Email:",
    user_profile["personal"]["email"]
)

print(
    "Phone:",
    user_profile["personal"]["phone"]
)


print("\nEDUCATION")

print(
    "Degree:",
    user_profile["education"]["degree"]
)

print(
    "Field:",
    user_profile["education"]["field"]
)

print(
    "University:",
    user_profile["education"]["university"]
)

print(
    "Graduation Year:",
    user_profile["education"]["graduation_year"]
)


print("\nCAREER")

print(
    "Skills:",
    user_profile["career"]["skills"]
)

print(
    "Experience:",
    user_profile["career"]["experience"]
)

print(
    "Preferred Roles:",
    user_profile["career"]["preferred_roles"]
)


print("\nCONSTRAINTS")

print(
    "Job Types:",
    user_profile["constraints"]["job_types"]
)

print(
    "Preferred Locations:",
    user_profile["constraints"]
    ["location"]
    ["preferred_locations"]
)

print(
    "Remote Allowed:",
    user_profile["constraints"]
    ["location"]
    ["remote_allowed"]
)

print(
    "Maximum Distance:",
    user_profile["constraints"]
    ["location"]
    ["max_distance_km"],
    "km"
)

print(
    "Minimum Stipend:",
    user_profile["constraints"]
    ["compensation"]
    ["minimum_stipend"]
)

print(
    "Minimum Salary:",
    user_profile["constraints"]
    ["compensation"]
    ["minimum_salary"]
)

print(
    "Skill-Gap Opportunities:",
    user_profile["constraints"]
    ["skill_gap"]
    ["allowed"]
)

print(
    "Application Approval Required:",
    user_profile["constraints"]
    ["application"]
    ["require_approval"]
)

print(
    "Maximum Applications Per Day:",
    user_profile["constraints"]
    ["application"]
    ["max_applications_per_day"]
)


print("\n==========================================")
print("      PROFILE SETUP COMPLETE")
print("==========================================")
