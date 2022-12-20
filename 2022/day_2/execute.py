import rock_paper_scissors;

with open('input') as file:
    lines = [line.rstrip() for line in file]

print(rock_paper_scissors.calculate_score(lines))
print(rock_paper_scissors.calculate_score_with_suggested_output(lines))
