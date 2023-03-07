"""
Simple code generator which generates python module, test class and tests which copy class/method structure in
given
module.
"""

import importlib

module_path = 'sudoku.sudoku_handler'
module_name = 'sudoku_handler'
class_name = 'SudokuHandler'

module = importlib.import_module(module_path)

test_file = f'../tests/test_{module_name}.py'
functions = [function for function in dir(getattr(module, class_name)) if function.find('__') == -1]

with open(test_file, 'w') as file:
	file.write(f"import pytest\n")
	file.write(f"import {module_path} as {module_name}\n\n\n")
	file.write(f"class Test{class_name}:\n\n")
	for function in functions:
		file.write(f"\tdef test_{function}(self):\n\t\tassert False\n\n")