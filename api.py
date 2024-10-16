
import mysql.connector
import json
from ast_node import Node

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chetan333!!##",
    database="rule_engine"
)

# Create a cursor object to execute queries
cursor = db.cursor()

def create_rule(rule_expression):
    # Insert the rule into the Rules table
    import json
    rule_expression_dict = json.loads(rule_expression)
    if rule_expression_dict["type"] == "operand" and isinstance(rule_expression_dict["value"], int):
        rule_expression_dict["value"] = {"attribute": "value", "operator": "=", "value": rule_expression_dict["value"]}
    query = "INSERT INTO Rules (rule_expression) VALUES (%s)"
    cursor.execute(query, (json.dumps(rule_expression_dict),))
    db.commit()
    return cursor.lastrowid

def combine_rules(rule_ids):
    # Retrieve the AST representations of the individual rules
    query = "SELECT rule_expression FROM Rules WHERE id IN (%s)"
    cursor.execute(query, (",".join(map(str, rule_ids)),))
    rule_expressions = [row[0] for row in cursor.fetchall()]
    
    # Combine the AST representations
    combined_expression = combine_ast_expressions(rule_expressions)
    combined_expression_str = json.dumps({
        "type": "operator",
        "value": "AND",
        "left": json.loads(rule_expressions[0]),
        "right": json.loads(rule_expressions[1]) if len(rule_expressions) > 1 else None
    })
    query = "INSERT INTO Rules (rule_expression) VALUES (%s)"
    cursor.execute(query, (combined_expression_str,))
    db.commit()
    return cursor.lastrowid

def evaluate_rule(rule_id, user_data):
    # Retrieve the AST representation of the rule
    query = "SELECT rule_expression FROM Rules WHERE id = %s"
    cursor.execute(query, (rule_id,))
    import json
    rule_expression = cursor.fetchone()[0]
    if isinstance(rule_expression, dict):
        rule_expression = json.dumps(rule_expression)
    elif isinstance(rule_expression, str):
        rule_expression = json.dumps(rule_expression)
    rule_expression = parse_ast_expression(rule_expression)
    
    # Evaluate the rule against the user data
    result = evaluate_ast_expression(rule_expression, user_data)
    return result

def parse_ast_expression(expression):
    import json
    if isinstance(expression, str):
        expr_dict = json.loads(expression)
    else:
        expr_dict = expression
    left = parse_ast_expression(expr_dict["left"]) if "left" in expr_dict and isinstance(expr_dict["left"], dict) else expr_dict.get("left")
    right = parse_ast_expression(expr_dict["right"]) if "right" in expr_dict and isinstance(expr_dict["right"], dict) else expr_dict.get("right")
    return Node(expr_dict["type"], left=left, right=right, value=expr_dict.get("value"))

def combine_ast_expressions(expressions):
    # Create a new AST node for the combined expression
    if not expressions:
        return None

    combined_node = parse_ast_expression(expressions[0])
    current_node = combined_node

    for expression in expressions[1:]:
        new_node = Node("operator", left=current_node, right=parse_ast_expression(expression), value="AND")
        current_node = new_node

    return current_node

def evaluate_ast_expression(expression, user_data):
    # Evaluate the AST expression recursively
    if expression.type == "operand":
        # Evaluate the operand node
        return evaluate_operand(expression, user_data)
    elif expression.type == "operator":
        # Evaluate the operator node
        return evaluate_operator(expression, user_data)

def evaluate_operand(node, user_data):
    # Evaluate the operand value against the user data
    attribute = node.value["attribute"]
    operator = node.value["operator"]
    value = node.value["value"]
    
    if operator == "=":
        return user_data[attribute] == value
    elif operator == ">":
        return user_data[attribute] > value
    # Add more operator evaluations as needed
    
    return False

def evaluate_operator(node, user_data):
    # Evaluate the left and right child nodes
    left_result = evaluate_ast_expression(node.left, user_data)
    right_result = evaluate_ast_expression(node.right, user_data)
    
    # Apply the operator logic
    if node.value == "AND":
        return left_result and right_result
    elif node.value == "OR":
        return left_result or right_result
    
    return False
