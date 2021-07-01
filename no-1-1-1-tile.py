import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.aer import StatevectorSimulator
from qiskit.visualization import plot_histogram
import itertools

qreg_q = QuantumRegister(3, "q")

circuit = QuantumCircuit(qreg_q)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])

circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[2], qreg_q[0])

# Draw the quantum circuit

circuit.draw("mpl", plot_barriers=False)

# Use the StatevectorSimulator

sim = StatevectorSimulator()

circuit = transpile(circuit, sim)

result = sim.run(circuit).result()

# Retrieve the probabilities (N.b. it won't return null values)

sequence_probabilities = result.get_counts(circuit)

print(sequence_probabilities)

plot_histogram(sequence_probabilities)

# Generate all the binary sequences for n bits
binary_sequences = ["".join(seq) for seq in itertools.product("01", repeat=2)]

# Map (combine) the probabilities as we're only interested in the 4 bits sequences
final_results = {}
for s in binary_sequences:
	final_results[s] = 0.

for k, v in sequence_probabilities.items():
	reverse = k[-1]+k[-2]
	final_results[reverse] += v

# Plot the histogram
plot_histogram(final_results)
plt.tight_layout()

# Show the plots
plt.show()