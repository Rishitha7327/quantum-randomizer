import streamlit as st
from qiskit import QuantumCircuit, Aer, execute

def quantum_random_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    return list(counts.keys())[0]

st.title("Quantum Randomizer Hub")

option = st.selectbox("Choose your randomizer:", ["Quantum Coin Flip", "Quantum Dice Roll", "Quantum Number (0–7)"])

if option == "Quantum Coin Flip":
    bit = quantum_random_bit()
    st.write("🪙 Result:", "Heads" if bit == '0' else "Tails")

elif option == "Quantum Dice Roll":
    bits = ''.join([quantum_random_bit() for _ in range(3)])
    dice = int(bits, 2) + 1
    st.write("🎲 Dice Roll:", dice)

elif option == "Quantum Number (0–7)":
    bits = ''.join([quantum_random_bit() for _ in range(3)])
    number = int(bits, 2)
    st.write("🔢 Quantum Number:", number)
