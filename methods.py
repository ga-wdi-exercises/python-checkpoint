# Create the following methods and make sure they return the correct data type
# and/or value

# #1: Create a method called num_list_with_arg that takes a positive integer and
# returns a list of integers between 1 and the number passed in.
#
# So if the number 5 is passed in, num_list_with_arg should return [1, 2, 3, 4]
newArray = []


def num_list_with_arg(num):
    for i in range(num):
        if i > 0:
            newArray.append(i)
    return newArray


num_list_with_arg(5)


# #2: Modify the has_ruby_exp method below so that it returns a SORTED list of
# all instructors who have Ruby experience (i.e. where "ruby" == True)
# The list should contain only names of instructors.
# make sure you name the list ruby_experience before returning it.


def has_ruby_exp():
    ruby_experience = []

    experience = {
        'jimmy': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': True,
            'biking': True,
            'pasta': False
        },
        'don': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': True,
            'biking': False,
            'pasta': False
        },
        'zakk': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': False,
            'biking': False,
            'pasta': True
        },
        'hector': {
            'bjj': True,
            'soccer': True,
            'ruby': False,
            'baking': False,
            'biking': True,
            'pasta': False
        }

    }
    for teach in experience:
        if(experience[teach]['ruby']):
            ruby_experience.append(teach)
    return ruby_experience


has_ruby_exp()
# #3: Create a method called toggle_str_num that takes an argument. If the
# argument is a string, convert it to an integer and return the integer; If the
# argument is an integer, convert it to a string and return the string; If the
# argument is neither a string nor an integer, return the string "this is not a
# str or a int":


def toggle_strt_num(value):
    int_num = []
    str_num = []
    if isinstance(value, int):
        str_num.append(str(value))
        return str_num
    elif isinstance(value, str):
        int_num.append(int(value))
        return int_num


print(toggle_strt_num('3'))
# Commit when you finish working on these questions!
