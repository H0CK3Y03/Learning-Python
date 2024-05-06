def check_float(potential_float):
    try:
        float(potential_float)

        return True
    except ValueError:
        return False

a_string = "1.33"

is_valid_float = check_float(a_string)

print(is_valid_float)