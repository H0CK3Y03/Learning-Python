def longest(list_of_words):
    length = 0
    longest_word = ''
    for word in list_of_words:
        if len(word) > length:
            length = len(word)
            longest_word = word
    return length, longest_word

my_list = []
n = []

while n != '':
    n = input("Your words: ")
    my_list.append(n)
my_list.pop()

print(longest(my_list))
print(my_list)





