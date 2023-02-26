import sys
sys.path.append("Calculator")

from Calculator.calculator import Calculator
from Calculator.matherror import ParenthesisError, InputExpressionError

calculator_ = Calculator()
calculator_.load_new_expression(input())
result = calculator_.calc()
print(result)