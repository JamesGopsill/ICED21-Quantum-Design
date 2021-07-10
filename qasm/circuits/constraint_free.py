from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def constraint_free() -> QuantumCircuit:

	# Initialise the quantum register
	qreg = QuantumRegister(4, "q")
	creg = ClassicalRegister(4, "c")

	# Initialise the circuit
	circuit = QuantumCircuit(qreg, creg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])
	circuit.h(qreg[2])
	circuit.h(qreg[3])

	circuit.barrier()

	circuit.measure(0, 0)
	circuit.measure(1, 1)
	circuit.measure(2, 2)
	circuit.measure(3, 3)

	return circuit