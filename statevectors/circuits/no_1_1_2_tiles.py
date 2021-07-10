from qiskit import QuantumCircuit, QuantumRegister

def no_1_1_2_tiles() -> QuantumCircuit:

	# Initialise the quantum register
	qreg = QuantumRegister(6, "q")

	# Initialise the circuit
	circuit = QuantumCircuit(qreg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])
	circuit.h(qreg[2])
	circuit.h(qreg[3])

	circuit.ccx(qreg[0], qreg[1], qreg[4])
	circuit.cx(qreg[4], qreg[0])

	circuit.barrier()

	circuit.ccx(qreg[2], qreg[3], qreg[5])
	circuit.cx(qreg[5], qreg[2])

	return circuit