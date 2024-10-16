# RuleEngineWithAst
Assignment for rule engine with AST
Rule Engine
Overview
The Rule Engine is a powerful and flexible system designed to create, combine, and evaluate rules based on user data. It allows users to define complex business logic through a simple interface, enabling dynamic decision-making in applications. This project is built using Python and integrates seamlessly with a MySQL database for persistent storage of rules and conditions.

Features
Rule Creation: Easily create rules with defined conditions and operators.
Rule Combination: Combine multiple rules using logical operators (AND, OR) to form complex decision trees.
Rule Evaluation: Evaluate rules against user data to determine outcomes based on defined logic.
Database Integration: Store and manage rules, conditions, and combinations in a MySQL database.
Testing: Comprehensive unit tests to ensure the functionality and reliability of the rule engine.
# Getting Started
# Prerequisites
Python 3.x
MySQL Server
MySQL Workbench (optional, for database management)
Installation
Clone the repository:
git clone https://github.com/BandaruchetanKumar/RuleEngineWithAst
cd rule-engine

Install the required Python packages:

pip install mysql-connector-python

Set up the MySQL database:

Use MySQL Workbench to create a new database.
Execute the SQL scripts provided in schema.sql to create the necessary tables.
Configuration
Update the database connection parameters in your Python scripts to match your MySQL setup.
Usage
Creating Rules: Use the API functions to create rules and define conditions.
Combining Rules: Combine existing rules using logical operators.
Evaluating Rules: Pass user data to the evaluation function to determine the outcome based on the defined rules.
Example

import mysql.connector

# Example of connecting to the database and creating a rule
# (Add your implementation here)
Testing
Run the test suite to validate the functionality of the rule engine:

python -m unittest test_rule_engine.py

# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

# Acknowledgments
MySQL Connector/Python for database connectivity.
Python for the programming language.
