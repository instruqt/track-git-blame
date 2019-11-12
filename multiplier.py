# This script takes two input variables and prints their product

import sys

variable_1 = int(sys.argv[1])
variable_2 = int(sys.argv[2])

# Define a multiplier function
def multiplier(a,b):
    return(a+b)

# Print the product
print(multiplier(variable_1, variable_2))
