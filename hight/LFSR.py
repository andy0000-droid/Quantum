#LFSR implemetation with python
def print_bin(m, v):
    print(m+": {:#09b}".format(v))
initial_state = 0b1011010
print_bin("Initial state", initial_state)
output = initial_state & 0b1
print_bin("Output", output)
state = initial_state >> 1
print_bin("State", state)