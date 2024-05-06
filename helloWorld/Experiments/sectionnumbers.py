def longest_section(list_of_numbers):
    previous = ''
    count = 1
    max_count = 0
    for number in list_of_numbers:
        if number == previous:
            count += 1
        else:
            count = 1
        previous = number
        if count > max_count:
            max_count = count
            the_numbers = number
        else:
            continue
    return max_count, the_numbers

my_list = []
n = []

try:
    while n != '':
        n = int(input("Your numbers: "))
        my_list.append(n)

except:
    sequence, the_number = longest_section(my_list)
    print(longest_section(my_list))
    print(my_list)
    print(f'The longest sequence consists of {sequence} numbers. The numbers are all {the_number}\'s')


































