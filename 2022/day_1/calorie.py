def max_calorie(input: list[str]):
    if '' in input:
        index = input.index('')
        current_maximum = max_calorie(input[0:index])
        others_maximum = max_calorie(input[index+1:])
        return current_maximum if current_maximum > others_maximum else others_maximum
    else:
        return sum(map(lambda x: int(x), input))

def all_elves_calories(input: list[str]):
    if '' in input:
        index = input.index('')
        current_maximum = all_elves_calories(input[0:index])
        others_maximum = all_elves_calories(input[index+1:])
        return current_maximum + others_maximum
    else:
        return [sum(map(lambda x: int(x), input))]

def top_three_calories_total(input: list[str]):
    return sum(sorted(all_elves_calories(input))[-3:])
