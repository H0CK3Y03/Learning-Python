# map() = applies a function to each item in a iterable (list, tuple, etc.)
#
# map(function, iterable)

# store = [("shirt",20.00),     # USD  -> EUR  ~= *0.82
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
#
# to_euros = lambda data: (data[0],data[1] * 0.82)
#
# store_euros = list(map(to_euros, store))
#
# for i in store_euros:
#     print(i)

store = [("shirt",20.00),     # USD <- EUR  ~= /0.82
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_dollars = lambda data: (data[0],data[1] / 0.82)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    # print(i)
    print(f'{i[0]} -> {i[1]:.2f}')






























