# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# states_of_america[1] = "Pencilvania"
#
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
#
# print(states_of_america)
import random

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")

print(f"The names are {names_string}")

# number_of_people = len(names)
# random_choice = random.randint(0, number_of_people - 1)
# person_who_will_pay = names[random_choice]
# print(f"{person_who_will_pay} will pay for the bill.")

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} will pay for the bill.")



