

################################ LOOPS ########################################


### Example - 1:

# Let's define a function that will calculate the increased salary when the salary information is received from the user:
    # Not : If the salary amount is 3000 TL or more, 20% raise, and if it is below 3000 TL, a 30% increase will be applied.

# Let's define a function that returns the waige increase according to the salary amount:
def calc_waige_raise(salary):
    if salary >= 3000:
        waige_raise = 0.20
    else:
        waige_raise = 0.30
    return(waige_raise)

# Now, let's define a function that returns the new salary amount increase according to waige increase:
def new_salary(salary):
    waige_raise = calc_waige_raise(salary)
    new_salary = salary + salary * waige_raise
    print(new_salary)

# Let's define a function that asks the user for salary amount, and returns the new salary amount:
def calc_new_salary():
    salary = int(input("Enter salary information:"))
    calc_waige_raise(salary)
    new_salary(salary)

calc_new_salary()

################################ ####################### ####################### #######################

### Example - 2:

# Let's define a function that calculates the summation of elements of list:

liste =  [1, 4, 5, 6, 8, 3, 3, 4, 67]

summation = 0
for idx in range(0,len(liste)):
    summation += liste[idx]
    idx +=1

print(summation)

################################ ####################### ####################### #######################

### Example - 3:
# Let's define a function that finds the minimum element of the list.


def calc_min_val(min_val = 9999999999):

    for idx in range(0,len(liste)):
        if liste[idx] < min_val:
            min_val = liste[idx]
            idx += 1
        else:
            min_val
    return min_val


################################ ####################### ####################### #######################

### Example - 4:

# Let's define a function such that text_1 produces the output in text_2

text_1 =  "hi my name is mark and i am learning python"
text_2 =  "Hi mY NaMe iS MaRk aNd i aM LeArNiNg pYtHoN"

##### Solution - 1:
def text_transforming(string):

    new_string = ""

    for idx in range(0, len(string)):
        if idx % 2 == 0:
            new_string += string[idx].upper()
        else:
            new_string += string[idx].lower()
    print(new_string)

text_transforming(text_1)


##### Solution - 2:
def text_transforming(string):

    new_string = []

    for idx in range(0, len(string)):
        if idx % 2 == 0:
            new_string.append(string[idx].upper())
        else:
            new_string.append(string[idx].lower())
    print("".join(new_string))

text_transforming(text_1)


##### Solution - 3:
def alternating_with_enumerate(string):
    liste = []

    for idx, word in enumerate(string):
        if idx % 2 == 0:
            liste.append(word.upper())
        else:
            liste.append(word.lower())
    listToStr = ''.join([str(elem) for elem in liste])
    return listToStr

alternating_with_enumerate("hi my name is mark and i am learning python")

################################ ####################### ####################### #######################

### Example - 5:

# Let's define a function to divide the list of students into 2 groups as "students_group" and show them in a single list.

students = ["John", "Mark", "Venessa", "Mariam", "Sam", "Paul"]
students_group = [["John","Venessa","Sam"], ["Mark", "Mariam", "Paul"]]

def division_students(students):

    students_group = [[],[]]

    for idx, student in enumerate(students):
        if idx % 2 == 0:
            students_group[0].append(student)
        else:
            students_group[1].append(student)
    print(students_group)

division_students(students)



