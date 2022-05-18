from qiskit import *
# Create a Quantum Circuit acting on a quantum register of three qubits
circ_q = QuantumRegister(3)
circ_c = ClassicalRegister(3)
circ = QuantumCircuit(circ_q,circ_c)
# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(circ_q[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
circ.cx(circ_q[0], circ_q[1])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
# the qubits in a GHZ state.
circ.cx(circ_q[0], circ_q[2])
circ.measure(circ_q,circ_c)
print(circ)
