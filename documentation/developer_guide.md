# Developer Guide for MQL Generator Project

## Table of Contents
1. [Introduction](#introduction)
2. [Project Setup](#project-setup)
3. [Project Architecture](#project-architecture)
4. [Key Components](#key-components)
5. [Workflow](#workflow)
6. [Debugging and Troubleshooting](#debugging-and-troubleshooting)
7. [How to Add New Features](#how-to-add-new-features)
8. [Testing](#testing)
9. [Best Practices](#best-practices)
10. [Contact](#contact)

---

## Introduction
The MQL Generator project automates the creation of MetaTrader 4 (MT4) Expert Advisors (EAs). It takes structured input data and generates `.mq4` files, which are scripts used for automated trading in the MT4 platform.

This guide provides developers with the necessary information to understand, debug, modify, and extend the project.

---

## Project Setup

### Prerequisites
- Python 3.10 or higher
- MetaTrader 4 installed (for testing generated `.mq4` files)
- A code editor (e.g., VSCode)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mql_generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify the setup:
   ```bash
   python pyfiles/test.py
   ```

---

## Project Architecture

### Directory Structure
```
mql_generator/
├── pyfiles/                # Core Python modules
│   ├── test.py             # Test runner script
│   ├── expert_builder_class.py # Core logic for building MQL scripts
│   ├── mql_generator.py    # MQL generation logic
│   ├── path_root.py        # Handles file paths
│   ├── test_input_*.py     # Test input data
├── output/                 # Generated `.mq4` files
├── .idea/                  # IDE configuration files
├── requirements.txt        # Python dependencies
└── developer_guide.md      # Developer documentation
```

---

## Key Components

### 1. `test.py`
- **Purpose**: Runs the MQL generation process using test inputs.
- **Key Functions**:
  - `test()`: Reads input data, generates MQL code, and writes it to an output file.

### 2. `expert_builder_class.py`
- **Purpose**: Contains the `ExpertBuilder` class, which constructs the MQL script.
- **Key Methods**:
  - `add_consts_user(const_inputs)`: Adds user-defined constants.
  - `add_vars_user(mvars)`: Adds user-defined variables.
  - `process_blocks_*`: Processes different blocks (e.g., `timer`, `trade`, `deinit`).
  - `build()`: Combines all components to generate the final MQL script.

### 3. `mql_generator.py`
- **Purpose**: Converts structured input data into MQL code.
- **Key Functions**:
  - `generate_mql(data)`: Main function to generate MQL code.

### 4. `path_root.py`
- **Purpose**: Provides the root path for the project.
- **Key Functions**:
  - `get()`: Returns the root path.

### 5. Test Inputs (`test_input_*.py`)
- **Purpose**: Provide structured input data for testing.
- **Example**:
  ```python
  input_data_14 = {
      "project_options": {
          "magic_and_other": {"magic_number": 123456},
          "visual": {"display_spread_meter": True},
      },
      "blocks": [
          {"type": "trade", "parameters": {"lot_size": 0.1}},
      ],
  }
  ```

---

## Workflow

1. **Input Data**:
   - The project starts with structured input data (e.g., `test_input_*.py`).
   - This data defines trading strategies, parameters, and configurations.

2. **MQL Generation**:
   - The `mql_generator.generate_mql(data)` function processes the input data.
   - It uses the `ExpertBuilder` class to construct the MQL script.

3. **Output**:
   - The generated `.mq4` file is saved in the `/output/` directory.
   - This file can be tested in the MetaTrader 4 platform.

---

## Debugging and Troubleshooting

### Common Issues
1. **File Not Found**:
   - Ensure the `path_root.get()` function returns the correct root path.
   - Verify the `/output/` directory exists.

2. **Invalid Input Data**:
   - Check the structure of the input data in `test_input_*.py`.
   - Ensure all required fields are present.

3. **MQL Syntax Errors**:
   - Open the generated `.mq4` file in MetaEditor (part of MetaTrader 4).
   - Use the built-in compiler to identify syntax errors.

### Debugging Tips
- Add print statements in `test.py` to inspect intermediate results:
  ```python
  print(data)
  print(result)
  ```
- Use a debugger (e.g., VSCode's Python debugger) to step through the code.
- Log errors and warnings using Python's `logging` module.

---

## How to Add New Features

### Adding a New Block Type
1. Define the block logic in `expert_builder_class.py`:
   ```python
   def process_blocks_new_type(self, data):
       # Add logic for the new block type
   ```
2. Update the `build()` method to include the new block type.

### Adding a New Test Input
1. Create a new file in `pyfiles/` (e.g., `test_input_16.py`).
2. Define the input data:
   ```python
   input_data_16 = {
       "project_options": {...},
       "blocks": [...],
   }
   ```
3. Update `test.py` to use the new input.

---

## Testing

### Running Tests
- Use the `test.py` script to test the MQL generation process:
  ```bash
  python pyfiles/test.py
  ```

### Adding Test Cases
1. Add a new test input file (e.g., `test_input_17.py`).
2. Modify `test.py` to include the new test case.

---

## Best Practices

1. **Follow PEP 8**: Ensure all Python code adheres to the PEP 8 style guide.
2. **Use Meaningful Names**: Use descriptive names for variables, functions, and classes.
3. **Add Comments**: Document all methods and functions for better readability.
4. **Handle Errors Gracefully**: Add error handling for file operations and invalid inputs.
5. **Write Tests**: Ensure all new features are tested with appropriate test cases.
6. **Version Control**: Use Git for version control and commit changes with meaningful messages.

---

## Contact
For questions or contributions, please contact the project maintainer at [email@example.com].

