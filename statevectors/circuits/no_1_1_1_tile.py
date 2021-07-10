from qiskit import QuantumCircuit, QuantumRegister

def no_1_1_1_tile() -> QuantumCircuit:

	qreg = QuantumRegister(3, "q")

	circuit = QuantumCircuit(qreg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])

	circuit.ccx(qreg[0], qreg[1], qreg[2])
	circuit.cx(qreg[2], qreg[0])

	return circuit