# Write a program to remove duplicates in a list
numbers = [1, 3, 2, 4, 4, 8, 6, 8, 9, 0, 4, 1, 5, 7, 9,]
print(f'Initial list:{numbers}')

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(f'final list after removing duplicates:{uniques}')