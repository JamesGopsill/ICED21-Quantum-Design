import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.aer import StatevectorSimulator
from qiskit.visualization import plot_histogram
import itertools

# Initialise the quantum register
qreg_q = QuantumRegister(6, "q")

# Initialise the circuit
circuit = QuantumCircuit(qreg_q)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[2])
circuit.h(qreg_q[3])

circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[4])
circuit.cx(qreg_q[4], qreg_q[0])

circuit.barrier()

circuit.ccx(qreg_q[2], qreg_q[3], qreg_q[5])
circuit.cx(qreg_q[5], qreg_q[2])

# Draw the quantum circuit

circuit.draw("mpl", plot_barriers=False)

# Use the StatevectorSimulator

sim = StatevectorSimulator()

circuit = transpile(circuit, sim)

result = sim.run(circuit).result()

# Retrieve the probabilities (N.b. it won't return null values)

sequence_probabilities = result.get_counts(circuit)

plot_histogram(sequence_probabilities)

# Generate all the binary sequences for n bits
binary_sequences = ["".join(seq) for seq in itertools.product("01", repeat=4)]

# Map (combine) the probabilities as we're only interested in the 4 bits sequences
# N.b. the bit sequences in the key are in reverse order!
final_results = {}
for s in binary_sequences:
	final_results[s] = 0.

for k, v in sequence_probabilities.items():
	print(k, v)
	reverse = k[-1]+k[-2]+k[-3]+k[-4]
	final_results[reverse] += v

for k, v in final_results.items():
	print(k, v)

# Plot the histogram
plot_histogram(final_results)
plt.tight_layout()

# Show the plots
plt.show()