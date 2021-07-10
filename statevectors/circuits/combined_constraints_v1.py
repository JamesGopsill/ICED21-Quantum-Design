from qiskit import QuantumCircuit, QuantumRegister

def combined_constraints_v1() -> QuantumCircuit:

	qreg = QuantumRegister(10, "q")

	circuit = QuantumCircuit(qreg)

	circuit.h(qreg[0])
	circuit.h(qreg[1])
	circuit.h(qreg[2])
	circuit.h(qreg[3])

	circuit.barrier()

	circuit.ccx(qreg[0], qreg[1], qreg[4])
	circuit.cx(qreg[4], qreg[0])

	circuit.barrier()

	circuit.ccx(qreg[2], qreg[3], qreg[5])
	circuit.cx(qreg[5], qreg[2])

	circuit.barrier()

	circuit.ccx(qreg[0], qreg[2], qreg[6])
	circuit.x(qreg[0])
	circuit.x(qreg[2])

	circuit.barrier()

	circuit.ccx(qreg[0], qreg[2], qreg[6])
	circuit.x(qreg[0])
	circuit.x(qreg[2])

	circuit.barrier()

	circuit.ccx(qreg[1], qreg[3], qreg[7])
	circuit.x(qreg[1])
	circuit.x(qreg[3])

	circuit.barrier()

	circuit.ccx(qreg[1], qreg[3], qreg[7])
	circuit.x(qreg[1])
	circuit.x(qreg[3])

	circuit.barrier()

	circuit.ccx(qreg[6], qreg[7], qreg[8])
	circuit.cx(qreg[8], qreg[3])

	return circuit
