import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.aer import StatevectorSimulator
from qiskit.visualization import plot_histogram

qreg_q = QuantumRegister(4, "q")

circuit = QuantumCircuit(qreg_q)

circuit.h(qreg_q[0])
#circuit.h(qreg_q[1])
#circuit.h(qreg_q[2])
#circuit.h(qreg_q[3])

circuit.draw("mpl", plot_barriers=False)

# Use the StatevectorSimulator

sim = StatevectorSimulator()

circuit = transpile(circuit, sim)

result = sim.run(circuit).result()

# Retrieve the probabilities (N.b. it won't return null values)

sequence_probabilities = result.get_counts(circuit)
for k, v in sequence_probabilities.items():
	print(k, v)

# Plot the histogram
plot_histogram(sequence_probabilities)
plt.tight_layout()

# Show the plots
plt.show()
