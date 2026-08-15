# ============================================
# Part 1: Basic Exercises (if, if)
# ============================================

# ---------- Question 1: Age check ----------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")


# ---------- Question 2: Compare my_age and your_age ----------
my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    word = "year" if diff == 1 else "years"
    print(f"You are {diff} {word} older than me.")
elif my_age > your_age:
    diff = my_age - your_age
    word = "year" if diff == 1 else "years"
    print(f"I am {diff} {word} older than you.")
else:
    print("We are the same age.")


# ---------- Question 3: Season checker ----------
month = input("Enter a month: ")

if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
else:
    print("Please enter a valid month name.")
