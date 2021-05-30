

############################################## FUNCTIONS ########################################################

# When Do We Need to Write a Function?
     # - When we need repetitive operations, it makes our job easier to write a function:

###############################################################################
# Writing Functions in Python

# DRY (dont repeat yourself) : Don't repeat yourself, use a function instead of copy and paste all the time
# PEP8 : Pay attention to PEP8 rules when using functions.
# DoT (Do one Thing): A function should have only one task.
# Modularity: It is a parallel concept with do one thing. Written functions and codes should be generalizable and parametric, and also can be integrated another projects.

###############################################################################

# Example : When we call a function in another function, how do we this?

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

def standardization(a, p):
    """
        The function applies the standardization process using the entered values

        Parameters
        ----------
        a : int
            The output value of "calculate" function will be used as a "a" parameter.
        p : int
            Parameter value to be entered by the user

        Returns
        ----------
            Returns a integer value.
    """
    return a * 10 / 100 * p * p



# Now let's define a new function called "all_calculations", which calls the "calculate function" to provide an argument to the "standardization" function:
    # Note: The basic parameters of all_calculations function are a & p. However, since the argument "a" is derived from the parameters varm, moisture, charge, these parameters should also be given as input to the function.

def all_calculations(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculations(10, 90, 87, 10)
########################################################
