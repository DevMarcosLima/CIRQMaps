# CIRQMaps: Quantum Approach to Urban Route Optimization

## Overview

CIRQMaps is an innovative project that leverages quantum computing to optimize urban routes efficiently. By pre-calculating possible paths from various starting points within a city, the system combines quantum computing with real-time traffic data to offer fast and precise routing, even in dynamic conditions such as roadblocks or construction.

The core of the project uses the Quantum Approximate Optimization Algorithm (QAOA) implemented via the Cirq library, a Python framework for creating, simulating, and executing quantum circuits.

## How It Works

1. **Graph Creation**: The application creates a complex graph representing streets and intersections with fixed weights corresponding to distances or times.
2. **Quantum Circuit Construction**: Quantum circuits are built using the Cirq library, where each possible route between a source and destination is represented by a quantum state.
3. **Route Simulation**: The quantum circuit is simulated multiple times to determine the most probable optimal route based on the given criteria.
4. **Graph Visualization**: The selected routes are visualized and saved as images for further analysis.

## Prerequisites

Before running the project, ensure you have Python installed (preferably Python 3.11 or higher).

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/CIRQMaps.git
   cd CIRQMaps

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project
After setting up the environment and installing the dependencies, you can run the main script to generate and save the routes:

    ```bash
    python main.py
    ```

## How It Works

This script will:

- Generate a complex graph representing the streets of a city.
- Construct and simulate quantum circuits for possible routes.
- Select and visualize the optimal route.
- Save the visualizations of the selected routes in the `routes` directory.

## Quantum Application Summary

CIRQMaps utilizes quantum computing to handle the complexity of route optimization in urban environments. The Quantum Approximate Optimization Algorithm (QAOA) is applied to explore multiple paths in parallel, allowing for the selection of the most efficient route based on pre-defined criteria such as distance or time.

By simulating quantum circuits, the system evaluates all possible routes simultaneously and identifies the best option, offering significant advantages in scenarios where real-time traffic data is essential. The pre-calculation of routes, combined with quantum optimization, enables fast decision-making, which is particularly useful in rapidly changing urban settings.

## Future Enhancements

- **Real-time Traffic Data Integration**: Integrate live traffic data to adjust pre-calculated routes dynamically.
- **Scalability Improvements**: Expand the system to handle larger urban environments and more complex routing scenarios.
- **User Preferences**: Incorporate user-specific preferences for route selection, such as avoiding toll roads or preferring scenic routes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or inquiries, please contact Marcos Antunes Alves de Lima.
Email: marcos_dev@icloud.com
Phone number: +55 11911225579
