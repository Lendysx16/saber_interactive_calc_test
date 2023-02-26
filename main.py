import sys
sys.path.append("Calculator")

from Calculator.calculator import Calculator


calculator_ = Calculator()
calculator_.load_new_expression(input())
result = calculator_.calc()
print(result)
