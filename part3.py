# ============================================
# Part 3: Loops
# ============================================
from collections import Counter

from countries import countries
from countries_details_dat import countries_data

# ---------- 1: Countries containing the word "land" ----------
land_countries = [country for country in countries if 'land' in country.lower()]

print(f"Number of countries containing 'land': {len(land_countries)}")
print(land_countries)

# ---------- 2.1: Total number of unique languages ----------
all_languages = []
for country in countries_data:
    all_languages.extend(country['languages'])

unique_languages = set(all_languages)
print("Total number of languages:", len(unique_languages))

# ---------- 2.2: Top 10 most spoken languages ----------
language_counts = Counter(all_languages)
top_10_languages = language_counts.most_common(10)

print("Top 10 most spoken languages:")
for language, count in top_10_languages:
    print(f"{language}: {count} countries")

# ---------- 2.3: Top 10 most populated countries ----------
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)
top_10_populated = sorted_by_population[:10]

print("Top 10 most populated countries:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']:,}")
