whole_number = input("100% is: ")
not_total_number = input("Second number: ")
percentage = input("The percentage: ")

if whole_number != "":
    float_whole_number = float(whole_number)
if not_total_number != "":
    float_not_total_number = float(not_total_number)
if percentage != "":
    float_percentage = float(percentage)

if whole_number and not_total_number != "":
    new_percentage = (float_not_total_number / float_whole_number) * 100
    print(f"The percentage is: {new_percentage}%")
elif whole_number and percentage != "":
    new_number = (float_whole_number / 100) * float_percentage
    print(f'The number is: {new_number}')
elif not_total_number and percentage != "":
    total_number = (float_not_total_number / float_percentage) * 100
    print(f"100% is: {total_number}")
else:
    print("All is fine. Don't worry about it.")
