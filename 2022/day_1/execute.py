import calorie;

with open('input') as file:
    lines = [line.rstrip() for line in file]

print(calorie.max_calorie(lines))
print(calorie.top_three_calories_total(lines))
