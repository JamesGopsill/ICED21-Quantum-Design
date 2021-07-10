from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def no_1_1_1_tile() -> QuantumCircuit:

	# Initialise the quantum register
	qreg = QuantumRegister(6, "q")
	creg = ClassicalRegister(4, "c")

	# Initialise the circuit
	circuit = QuantumCircuit(qreg, creg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])

	circuit.ccx(qreg[0], qreg[1], qreg[2])
	circuit.cx(qreg[2], qreg[0])

	circuit.barrier()

	circuit.measure(0, 0)
	circuit.measure(1, 1)
	circuit.measure(2, 2)
	circuit.measure(3, 3)

	return circuit