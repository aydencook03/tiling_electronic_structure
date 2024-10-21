# Tiling Electronic Structure

Exploring novel electronic structures through k-uniform planar tilings to discover interesting and useful materials.

## Project Overview

This project combines geometric tiling patterns with tight-binding model analysis to investigate unique electronic properties. By systematically generating k-uniform planar tilings and treating them as atomic lattices, we aim to uncover new materials with interesting or useful characteristics that could lead to technological advancements in various fields.

## Key Components

1. **Tiling Generation**: Python-based creation of k-uniform planar tilings, serving as the foundation for atomic lattice structures.
2. **Tight-Binding Model**: Application of the tight-binding model to simulate electron behavior in the lattice.
3. **Band Structure Analysis**: Exploration of electronic band structures for different tilings and atomic compositions.

## Features

- Generation of 1-uniform tilings
- Visualization of tiling patterns and their corresponding band structures
- Customizable tight-binding model parameters for different atomic species
- Efficient handling of geometric calculations and tiling manipulations

## Examples

| Tiling Unit | Full Tiling | Band Structure |
|-------------|-------------|-----------------|
| ![Tiling Unit: square triangle square](./images/Tiling_Unit:_square_triangle_square.png) | ![Full Tiling: square triangle square](./images/Full_Tiling:_square_triangle_square.png) | ![Band Structure: square triangle square](./images/Band_Structure:_square_triangle_square.png) |
| ![Tiling Unit: dodecagon hexagon square](./images/Tiling_Unit:_dodecagon_hexagon_square.png) | ![Full Tiling: dodecagon hexagon square](./images/Full_Tiling:_dodecagon_hexagon_square.png) | ![Band Structure: dodecagon hexagon square](./images/Band_Structure:_dodecagon_hexagon_square.png) |

## Installation

1. Ensure you have Python installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/aydencook03/tiling_electronic_structure.git
   cd tiling_electronic_structure
   ```

3. Install dependencies using Pipenv:

   ```bash
   pip install pipenv
   pipenv install
   ```

## Usage

1. Activate the Pipenv shell:

   ```bash
   pipenv shell
   ```

2. Generate and visualize tiling patterns:

   ```bash
   python uniform_tilings_1.py
   ```

3. Analyze band structures:

   ```bash
   python tight_binding.py
   ```

## Project Structure

- `vec.py`: 2D vector class for geometric calculations
- `uniform_tilings_1.py`: Unit pattern generators for 1-uniform tilings
- `tiling.py`: Classes for tiling representation and manipulation
- `tight_binding.py`: Tight-binding model implementation for electronic structure computation

## Roadmap

For information about upcoming features and planned improvements, please refer to the [TODO.md](TODO.md) file in the project repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PythTB](https://www.physics.rutgers.edu/pythtb/) for tight-binding calculations
- [Matplotlib](https://matplotlib.org/) for visualization

## Contact

For questions or collaborations, please open an issue or contact [Your Name] at [your.email@example.com].
