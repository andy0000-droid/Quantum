from qiskit import *
# Using Qiskit Aer's Qasm Simulator
simulator = BasicAer.get_backend('qasm_simulator')

# Simulating the circuit using the simulator to get the result
job = execute(circuit, simulator)
result = job.result()

# Getting the aggregated binary outcomes of the circuit.
counts = result.get_counts(circuit)
print (counts)
