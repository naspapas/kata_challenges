file = open('input3.txt', 'r')
lines = file.readlines()
y = 0
zero_count = 0
one_count = 0
final_number = ''
final_reverse = ''

while y < 12:
    for line in lines:
        characters = list(line)
        if characters[y] == '0':
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        final_number += '0'
    else:
        final_number += '1'
    zero_count = 0
    one_count = 0
    y += 1

print(f'The final Binary number is {final_number}, converted is', int(final_number, 2))

for x in final_number:
    if x == '0':
        final_reverse += '1'
    else:
        final_reverse += '0'
print(f'The final Reverse number is {final_reverse}, converted is', int(final_reverse, 2))

print("As such, answer is Result 1 * Result 2, which is", int(final_number, 2) * int(final_reverse, 2))
