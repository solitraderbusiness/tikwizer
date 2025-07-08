# Technical Documentation for MQL Generator Project

## Table of Contents
1. [Introduction](#introduction)
2. [Modules Overview](#modules-overview)
3. [Classes and Functions](#classes-and-functions)
   - [test.py](#testpy)
   - [expert_builder_class.py](#expert_builder_classpy)
   - [mql_generator.py](#mql_generatorpy)
   - [path_root.py](#path_rootpy)
   - [Test Inputs](#test-inputs)
4. [Data Flow](#data-flow)
5. [Main Flow and Logic of the Generator](#main-flow-and-logic-of-the-generator)

---

## Introduction
This document provides a detailed explanation of all the modules, classes, and functions in the MQL Generator project. It is intended to help developers understand the internal workings of the project.

---

## Modules Overview

### 1. `test.py`
- **Purpose**: Acts as the entry point for testing the MQL generation process.
- **Key Functionality**:
  - Reads input data from test files.
  - Generates `.mq4` files using the `mql_generator` module.
  - Saves the output to the `/output/` directory.

### 2. `expert_builder_class.py`
- **Purpose**: Contains the `ExpertBuilder` class, which is responsible for constructing the MQL script.
- **Key Functionality**:
  - Adds user-defined and system-defined constants and variables.
  - Processes different blocks (e.g., `timer`, `trade`, `deinit`).
  - Combines all components to generate the final MQL script.

### 3. `mql_generator.py`
- **Purpose**: Converts structured input data into MQL code.
- **Key Functionality**:
  - Provides the `generate_mql` function, which acts as the main entry point for MQL generation.

### 4. `path_root.py`
- **Purpose**: Provides the root path for the project.
- **Key Functionality**:
  - Returns the root directory path for file operations.

### 5. Test Inputs (`test_input_*.py`)
- **Purpose**: Provide structured input data for testing the MQL generation process.

---

## Classes and Functions

### test.py
#### `test()`
- **Purpose**: Main function to test the MQL generation process.
- **Parameters**: None.
- **Returns**: None.
- **Workflow**:
  1. Reads input data from `test_input_15`.
  2. Calls `mql_generator.generate_mql(data)` to generate the MQL script.
  3. Saves the generated script to `/output/expert_output.mq4`.
- **Code**:
  ```python
  def test():
      data = test_input_15.input_data_14
      result = mql_generator.generate_mql(data)
      path = path_root.get()
      path_sub = "/output/"
      file_name = "expert_output" + ".mq4"
      with open(path + path_sub + file_name, "w") as result_file:
          result_file.write(result)
  ```

---

### expert_builder_class.py
#### `ExpertBuilder` Class
- **Purpose**: Core class for constructing the MQL script.
- **Attributes**:
  - `consts_user`: List of user-defined constants.
  - `consts_system`: List of system-defined constants.
  - `vars_user`: List of user-defined variables.
  - `data`: Input data for the MQL script.
- **Key Methods**:
  - `add_consts_user(const_inputs)`: Adds user-defined constants.
  - `add_vars_user(mvars)`: Adds user-defined variables.
  - `process_blocks_*`: Processes specific blocks (e.g., `timer`, `trade`).
  - `build()`: Combines all components to generate the final MQL script.

#### `add_consts_user(const_inputs)`
- **Purpose**: Adds user-defined constants to the script.
- **Parameters**:
  - `const_inputs`: List of dictionaries containing constant definitions.
- **Returns**: None.
- **Code**:
  ```python
  def add_consts_user(self, const_inputs):
      for my_input in const_inputs:
          input_str = "extern " + my_input.get("type") + " " + my_input.get("name") \
                      + handle_const_var_value(my_input) + "; // " + my_input.get("description") + "\n"
          self.consts_user.append(input_str)
  ```

#### `build()`
- **Purpose**: Combines all components (constants, variables, blocks) to generate the final MQL script.
- **Parameters**: None.
- **Returns**: The generated MQL script as a string.

---

### mql_generator.py
#### `generate_mql(data)`
- **Purpose**: Main function to generate MQL code from structured input data.
- **Parameters**:
  - `data`: Dictionary containing input data for the MQL script.
- **Returns**: The generated MQL script as a string.
- **Workflow**:
  1. Initializes an `ExpertBuilder` instance.
  2. Calls methods to add constants, variables, and blocks.
  3. Calls `build()` to generate the final script.

---

### path_root.py
#### `get()`
- **Purpose**: Returns the root path for the project.
- **Parameters**: None.
- **Returns**: The root path as a string.
- **Code**:
  ```python
  def get():
      return os.path.dirname(os.path.abspath(__file__))
  ```

---

### Test Inputs
#### Example Input Data
- **Purpose**: Defines trading strategies, parameters, and configurations.
- **Structure**:
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

## Data Flow

1. **Input**:
   - The process starts with structured input data (e.g., `test_input_15.input_data_14`).

2. **Processing**:
   - The `mql_generator.generate_mql(data)` function processes the input data.
   - It uses the `ExpertBuilder` class to construct the MQL script.

3. **Output**:
   - The generated `.mq4` file is saved in the `/output/` directory.

---

## Main Flow and Logic of the Generator

### Overview
The MQL Generator project follows a structured flow to convert user-defined input data into a MetaTrader 4 `.mq4` script. The process involves:
1. **Input Data**: Structured data defining trading strategies, parameters, and configurations.
2. **Processing**: Using the `ExpertBuilder` class to construct the MQL script.
3. **Output**: Saving the generated `.mq4` file to the `/output/` directory.

---

### Step-by-Step Flow

#### 1. Input Data
- Input data is provided in Python files (e.g., `test_input_15.py`) as dictionaries.
- Example structure:
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
- Key sections of the input data:
  - **`project_options`**: Contains global settings like magic numbers and visual options.
  - **`blocks`**: Defines the logic for specific trading actions (e.g., trade, timer).

#### 2. Test Script (`test.py`)
- The `test()` function in `test.py` acts as the entry point for the generator.
- Workflow:
  1. Reads input data from a test input file (e.g., `test_input_15.input_data_14`).
  2. Calls `mql_generator.generate_mql(data)` to process the input data.
  3. Saves the generated `.mq4` file to the `/output/` directory.

#### 3. MQL Generation (`mql_generator.py`)
- The `generate_mql(data)` function is the main entry point for generating the MQL script.
- Workflow:
  1. Initializes an instance of the `ExpertBuilder` class.
  2. Calls methods on the `ExpertBuilder` instance to:
     - Add constants (user-defined and system-defined).
     - Add variables (user-defined and system-defined).
     - Process blocks (e.g., trade logic, timer logic).
  3. Calls the `build()` method of `ExpertBuilder` to combine all components into the final MQL script.
  4. Returns the generated MQL script as a string.

#### 4. ExpertBuilder Class (`expert_builder_class.py`)
- The `ExpertBuilder` class is responsible for constructing the MQL script.
- Key methods:
  - **`add_consts_user(const_inputs)`**:
    - Adds user-defined constants to the script.
    - Example:
      ```python
      extern int lot_size = 1; // Lot size for trading
      ```
  - **`add_vars_user(mvars)`**:
    - Adds user-defined variables to the script.
    - Example:
      ```python
      double account_balance; // Account balance variable
      ```
  - **`process_blocks_*`**:
    - Processes specific blocks (e.g., trade, timer, deinit).
    - Example for a trade block:
      ```python
      void OnTrade() {
          // Logic for handling trades
      }
      ```
  - **`build()`**:
    - Combines all constants, variables, and blocks into the final MQL script.
    - Returns the script as a string.

#### 5. Output
- The generated MQL script is saved as a `.mq4` file in the `/output/` directory.
- Example file path: `/output/expert_output.mq4`.

---

### Data Flow Diagram

```plaintext
Input Data (test_input_*.py)
       ↓
test.py (test() function)
       ↓
mql_generator.py (generate_mql(data))
       ↓
expert_builder_class.py (ExpertBuilder class)
       ↓
Output File (/output/expert_output.mq4)
```

---

### Example Workflow

1. **Input**:
   - Input data in `test_input_15.py`:
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

2. **Processing**:
   - `test.py` calls `mql_generator.generate_mql(data)`.
   - `generate_mql(data)` initializes `ExpertBuilder` and processes the input data.
   - `ExpertBuilder.build()` generates the final MQL script.

3. **Output**:
   - The generated `.mq4` file:
     ```mql
     extern int lot_size = 1; // Lot size for trading

     void OnTrade() {
         // Logic for handling trades
     }
     ```

---

This section provides a detailed explanation of the main flow and logic of the generator. Let me know if you need further clarifications or additional details!