import os
import cirq
import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to create a complex graph of streets with fixed weights
def create_graph():
    G = nx.Graph()

    # Add nodes (intersections)
    for i in range(1, 21):
        G.add_node(f'N{i}')

    # Add edges (streets) with fixed weights
    edges = [
        ('N1', 'N2', 30), ('N1', 'N3', 25), ('N2', 'N4', 20), 
        ('N2', 'N5', 35), ('N3', 'N6', 40), ('N3', 'N7', 50),
        ('N4', 'N8', 45), ('N4', 'N9', 30), ('N5', 'N10', 60),
        ('N6', 'N11', 55), ('N7', 'N12', 70), ('N8', 'N13', 50),
        ('N9', 'N14', 45), ('N10', 'N15', 40), ('N11', 'N16', 35),
        ('N12', 'N17', 25), ('N13', 'N18', 20), ('N14', 'N19', 50),
        ('N15', 'N20', 45), ('N16', 'N18', 30), ('N17', 'N19', 35),
        ('N18', 'N20', 40), ('N19', 'N20', 60), ('N1', 'N10', 55),
        ('N5', 'N15', 50), ('N3', 'N12', 60), ('N2', 'N11', 45),
        ('N6', 'N14', 35), ('N4', 'N19', 30), ('N8', 'N16', 40),
    ]

    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G

# Function to create the quantum circuit
def create_circuit(graph, paths, perturbation_factor):
    num_paths = len(paths)
    qubits = [cirq.LineQubit(i) for i in range(num_paths)]
    circuit = cirq.Circuit()

    # Apply Hadamard gate for superposition of all paths
    circuit.append(cirq.H.on_each(*qubits))

    # Apply rotations conditioned by path weights with perturbation
    for i, path in enumerate(paths):
        total_weight = sum(graph[u][v]['weight'] + random.uniform(-perturbation_factor, perturbation_factor) for u, v in zip(path[:-1], path[1:]))
        circuit.append(cirq.rz(total_weight).on(qubits[i]))

    # Measure the qubits
    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit

# Function to simulate the circuit and choose the route
def run_circuit(circuit, num_paths):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=100)
    frequencies = result.histogram(key='result')

    # Adjust the resulting index to ensure it is within the correct range
    selected_path_index = min(frequencies, key=frequencies.get) % num_paths
    return selected_path_index

# Function to visualize the graph and the selected route
def plot_graph(graph, paths, selected_path_index, file_name, color, pos):
    plt.figure(figsize=(8, 6))

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')

    # Draw all paths
    for path in paths:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='gray', width=2)

    # Highlight the selected path
    selected_path = paths[selected_path_index]
    selected_edges = [(selected_path[i], selected_path[i + 1]) for i in range(len(selected_path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=selected_edges, edge_color=color, width=4)

    plt.savefig(file_name)
    plt.close()
    print(f"Route saved as {file_name}")

# Example usage to generate and save 5 routes
def main():
    # Create the folder to save routes, if it doesn't exist
    os.makedirs("routes", exist_ok=True)

    # Create the complex street graph (used for all routes)
    graph = create_graph()

    # List all possible paths from point N1 to point N20
    paths = list(nx.all_simple_paths(graph, source='N1', target='N20'))

    # Fix the graph layout to ensure visual consistency
    pos = nx.spring_layout(graph, seed=42)  # Using a seed to ensure the layout is always the same

    # Colors for each route
    colors = ['blue', 'green', 'red', 'purple', 'orange']

    for i in range(5):
        # Create the quantum circuit with a small variation
        circuit = create_circuit(graph, paths, perturbation_factor=5 * (i + 1))

        # Run the circuit and get the selected route
        selected_path_index = run_circuit(circuit, len(paths))

        # Visualize the graph and the selected route, saving the image
        plot_graph(graph, paths, selected_path_index, f"routes/route_{i + 1}.png", colors[i], pos)

main()
