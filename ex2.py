f = open("input2.txt", "r")
commands = []


# def task_one():
#     x_pos = 0
#     y_pos = 0
#     for x in f:
#         commands.append(x)
#         split = x.split()
#         if split[0] == 'forward':
#             x_pos += int(split[1])
#         if split[0] == 'up':
#             y_pos -= int(split[1])
#         if split[0] == 'down':
#             y_pos += int(split[1])
#     print(f'The X Position is {x_pos}')
#     print(f'The Y Position is {y_pos}')
#     print(f'Final overall position for task 1 is', x_pos * y_pos)

def task_two():
    x_pos = 0
    y_pos = 0
    y_aim = 0
    for x in f:
        commands.append(x)
        split = x.split()
        if split[0] == 'forward':
            x_pos += int(split[1])
            y_pos += int(split[1]) * y_aim
        if split[0] == 'up':
            y_aim -= int(split[1])
        if split[0] == 'down':
            y_aim += int(split[1])
    print(f'The X Position is {x_pos}')
    print(f'The Y Position is {y_pos}')
    print(f'Final overall position is', x_pos * y_pos)



task_two()
f.close()
