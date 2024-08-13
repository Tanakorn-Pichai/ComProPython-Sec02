survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]
choices_sets = [set(languages) for languages in survey_results]
print(choices_sets)

common_languages = set.intersection (*choices_sets)
print("Languages chosen by all participants:", common_languages)


# single_choice_languages = {language for language, count in language_counts.items() if count == 1}
