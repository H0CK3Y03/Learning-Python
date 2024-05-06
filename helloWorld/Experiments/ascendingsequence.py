def longest_section(list_of_numbers):
    previous = my_list[0]
    count = 1
    max_count = 0
    for number in list_of_numbers:
        if number > previous:
            count += 1
        else:
            count = 1
        previous = number
        if count > max_count:
            max_count = count
        else:
            continue
    return max_count


my_list = []
n = []

try:
    while n != '':
        n = int(input("Your numbers: "))
        my_list.append(n)

except:
    sequence = longest_section(my_list)
    print(longest_section(my_list))
    print(my_list)
    print(f'The longest sequence of ascending numbers is {sequence}')
