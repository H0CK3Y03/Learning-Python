final_num = int(input("What range?: "))
num_str = str(final_num)

for i in range(final_num):
    if str(i+1)[-2:-1] != "1":
        if str(i+1)[-1] == '1':
            print(str(i+1)+"st")
        elif str(i+1)[-1] == '2':
            print(str(i+1)+"nd")
        elif str(i+1)[-1] == '3':
            print(str(i+1)+"rd")
        else:
            print(str(i+1)+"th")
    else:
        print(str(i+1) + "th")
