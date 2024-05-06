#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' (string) if it's
#  the initial module being run

# if __name__ == '__main__'

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

import module2

# print(__name__)
# print(module2.__name__)

# if __name__ == '__main__':     # we are checking if this module is being run directly or indirectly(if True -> directly)
#     print("running this module directly")
# else:
#     print("running other module indirectly")
#
# if module2.__name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")


if __name__ == '__main__':
    pass

# module2.hello()
module2.main()


























