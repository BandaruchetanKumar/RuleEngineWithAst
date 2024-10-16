# Rule Engine with Abstract Syntax Tree (AST)

## Overview

The Rule Engine with AST is a flexible and extensible framework designed to evaluate business rules using an Abstract Syntax Tree (AST). This project allows users to define rules in a structured manner and evaluate them against input data, making it suitable for various applications such as validation, filtering, and decision-making processes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Dynamic Rule Evaluation**: Easily define and evaluate rules dynamically at runtime.
- **Extensible**: Add custom functions and operators to enhance the rule engine's capabilities.
- **User -Friendly**: Simple syntax for defining rules that can be easily understood and modified.
- **Performance Optimized**: Efficient evaluation of rules using AST for faster processing.

## Installation

To install the Rule Engine with AST, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BandaruchetanKumar/RuleEngineWithAst.git
2. Navigate to project directory:
   cd RuleEngineWithAst
3. Install the required dependencies:
   npm install
## Usage
To use the Rule Engine, follow these steps:

1. **Import the Engine:**
   const RuleEngine = require('path/to/ruleEngine');
2. **Define Rules:** Create rules using a simple syntax. For example:
   const rules = [
    { condition: 'age > 18', action: 'allow' },
    { condition: 'age <= 18', action: 'deny' }
    ];
3.  **Evaluate Rules:** Pass the input data to the engine for evaluation:
    const inputData = { age: 20 };
    const result = RuleEngine.evaluate(rules, inputData);
    console.log(result); // Output: 'allow'

## Architecture
The Rule Engine is built on a modular architecture that consists of the following components:

**Parser:** Converts rule definitions into an AST.
**Evaluator:** Traverses the AST to evaluate conditions and execute actions.
**Context:** Holds the input data and provides it to the evaluator.

## Contributing
Contributions are welcome! If you would like to contribute to the Rule Engine, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a Pull Request.
