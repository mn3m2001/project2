# ============================================
# Part 2: Dictionary & Conditions Practice
# ============================================

person = {
    'first_name': 'Milaan',
    'last_name': 'Parmar',
    'age': 96,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['Python', 'Matlab', 'R', 'C', 'C++'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# ---------- #1: Print the middle skill ----------
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(skills[middle_index])

# ---------- #2: Check if 'Python' is in skills ----------
if 'skills' in person:
    print('Python' in person['skills'])

# ---------- #3: Determine title based on skills combination ----------
skills = person['skills']

if set(skills) == {'Python', 'Matlab'}:
    print("He knows machine learning")
elif 'Python' in skills and 'R' in skills:
    print("He knows statistics")
elif 'C' in skills and 'C++' in skills:
    print("He knows software development")
else:
    print("unknown title")

# ---------- #4: Print location and marital status ----------
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
