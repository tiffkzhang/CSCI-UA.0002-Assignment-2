print("Your Screen Printing Quote\n")

shirts = int(input('How many T-shirts would you like to have printed? '))
colors = int(input('How many colors will each shirt be printed with (1, 2 ,or 3)? '))
cost = 0

if colors == 1:
    if shirts >= 1 and shirts <= 99:
        cost = shirts * 10
    elif shirts >= 100 and shirts <= 249:
        cost = shirts * 8
    else: 
        cost = shirts * 7
elif colors == 2:
    if shirts >= 1 and shirts <= 99:
        cost = shirts * 11
    elif shirts >= 100 and shirts <= 249:
        cost = shirts * 9
    else:
        cost = shirts * 8
else:
    if shirts >= 1 and shirts <= 99:
        cost = shirts * 12
    elif shirts >= 100 and shirts <= 249:
        cost = shirts * 10
    else:
        cost = shirts * 9

color_output = ''
if colors == 1:
    color_output = ' color: $'
else:
    color_output = ' colors: $'

shirt_output = ''
if shirts == 1:
    shirt_output = ' shirt screen printed with '
else:
    shirt_output = ' shirts screen printed with '

total = 1.08875 * cost

print('\n', shirts, shirt_output, colors, color_output, format(total, ',.2f' ), sep='')
        