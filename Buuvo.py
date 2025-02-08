from subprocess import call
from time import sleep as wait



call("cls", shell=True)

inputs_prefix = "[Buuvo v1]: "
input_commands = [
    
    "exit",
    "%switch Function A",
    "%switch Function B",
    "%switch Function C",
    "%switch Function D"
    
    ]



# 1. --- Function Handler --- #

class function_switch:

    def __init__(self, A, B, C, D):

        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def inputs(self, option_a, option_b, option_c, option_d):

        if option_a:
            self.A()

        if option_b:
            self.B()

        if option_c:
            self.C()

        if option_d:
            self.D()

def function_a():
    call("cls", shell=True)
    print(inputs_prefix + "Executing function A")
    wait(1.5)
    call("cls", shell=True)

def function_b():
    call("cls", shell=True)
    print(inputs_prefix + "Executing function B")
    wait(1.5)
    call("cls", shell=True)

def function_c():
    call("cls", shell=True)
    print(inputs_prefix + "Executing function C")
    wait(1.5)
    call("cls", shell=True)

def function_d():
    call("cls", shell=True)
    print(inputs_prefix + "Executing function D")
    wait(1.5)
    call("cls", shell=True)

switch = function_switch(function_a, function_b, function_c, function_d)

# --- Function Handler --- #



# 2. --- User Input --- #

while True:

    user_input = input(inputs_prefix)
    if user_input not in input_commands:

        call("cls", shell=True)

    if user_input == input_commands[0]:

        exit()

    elif user_input == input_commands[1]:

        function_a()

    elif user_input == input_commands[2]:

        function_b()

    elif user_input == input_commands[3]:

        function_c()

    elif user_input == input_commands[4]:

        function_d()

# --- User Input --- #