# ============================================
# OPPORTUNITYFINDER AGENT

# ============================================


print("==========================================")
print("        OPPORTUNITYFINDER AGENT")
print("==========================================")

print("\nLet's create your profile.\n")


# ============================================
# 1. PERSONAL INFORMATION
# ============================================

print("---------- PERSONAL INFORMATION ----------")

name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")


# ============================================
# 2. EDUCATION
# ============================================

print("\n---------- EDUCATION ----------")

degree = input("Degree: ")
field = input("Field / Branch: ")
university = input("University: ")
graduation_year = input("Graduation year: ")


# ============================================
# 3. CAREER INFORMATION
# ============================================

print("\n---------- CAREER INFORMATION ----------")

skills_input = input(
    "Skills (separate with commas): "
)

skills = [
    skill.strip()
    for skill in skills_input.split(",")
]


experience = input(
    "Experience (if none, enter 'Fresher'): "
)


roles_input = input(
    "Preferred job roles (separate with commas): "
)

preferred_roles = [
    role.strip()
    for role in roles_input.split(",")
]


# ============================================
# 4. JOB TYPE CONSTRAINT
# ============================================

print("\n---------- JOB TYPE ----------")

print("1. Internship")
print("2. Full-time")
print("3. Both")

job_type_choice = input(
    "Choose 1, 2, or 3: "
)

if job_type_choice == "1":

    job_types = ["internship"]

elif job_type_choice == "2":

    job_types = ["full-time"]

elif job_type_choice == "3":

    job_types = [
        "internship",
        "full-time"
    ]

else:

    print("Invalid choice. No job type selected.")

    job_types = []


# ============================================
# 5. LOCATION CONSTRAINT
# ============================================

print("\n---------- LOCATION PREFERENCES ----------")

locations_input = input(
    "Preferred locations (separate with commas): "
)

preferred_locations = [
    location.strip()
    for location in locations_input.split(",")
]


remote_input = input(
    "Are you open to remote opportunities? (yes/no): "
)

remote_allowed = (
    remote_input.lower() == "yes"
)


max_distance = input(
    "Maximum distance you're willing to travel (km): "
)


# ============================================
# 6. COMPENSATION CONSTRAINTS
# ============================================

print("\n---------- COMPENSATION ----------")

minimum_stipend = input(
    "Minimum acceptable internship stipend: "
)

minimum_salary = input(
    "Minimum acceptable annual salary: "
)


# ============================================
# 7. SKILL-GAP OPPORTUNITY CONSTRAINT
# ============================================

print("\n---------- SKILL-GAP OPPORTUNITIES ----------")

skill_gap_input = input(
    "Should I show opportunities where you "
    "are missing some skills? (yes/no): "
)

allow_skill_gap = (
    skill_gap_input.lower() == "yes"
)


# ============================================
# 8. APPLICATION CONSTRAINT
# ============================================

print("\n---------- APPLICATION SETTINGS ----------")

approval_input = input(
    "Require your approval before submitting "
    "an application? (yes/no): "
)

require_approval = (
    approval_input.lower() == "yes"
)


# ============================================
# 9. MAXIMUM APPLICATIONS PER DAY
# ============================================

max_applications = input(
    "Maximum applications per day: "
)


# ============================================
# 10. CREATE USER PROFILE
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

            "max_distance_km": max_distance
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

            "max_applications_per_day": max_applications
        }
    }
}


# ============================================
# 11. DISPLAY USER PROFILE
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
    user_profile["constraints"]["location"]["preferred_locations"]
)

print(
    "Remote Allowed:",
    user_profile["constraints"]["location"]["remote_allowed"]
)

print(
    "Maximum Distance:",
    user_profile["constraints"]["location"]["max_distance_km"],
    "km"
)

print(
    "Minimum Stipend:",
    user_profile["constraints"]["compensation"]["minimum_stipend"]
)

print(
    "Minimum Salary:",
    user_profile["constraints"]["compensation"]["minimum_salary"]
)

print(
    "Skill-Gap Opportunities:",
    user_profile["constraints"]["skill_gap"]["allowed"]
)

print(
    "Application Approval Required:",
    user_profile["constraints"]["application"]["require_approval"]
)

print(
    "Maximum Applications Per Day:",
    user_profile["constraints"]["application"]["max_applications_per_day"]
)


print("\n==========================================")
print("      PROFILE SETUP COMPLETE")
print("==========================================")