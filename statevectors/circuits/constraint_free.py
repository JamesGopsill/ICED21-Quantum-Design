from qiskit import QuantumCircuit, QuantumRegister

def constraint_free() -> QuantumCircuit:
	qreg = QuantumRegister(4, "q")

	circuit = QuantumCircuit(qreg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])
	circuit.h(qreg[2])
	circuit.h(qreg[3])

	return circuit

