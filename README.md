# Math expression calculator
=======================================

How to use?
-------------
  -firstly you need to import Calculator class

  ```python 
  from Calculator.calculator import Calculator
  ```
   
    
   
 -if you have a problem with import try adding relative path to the package into **sys.path** above
 ```python
  import sys
  sys.path.append("Calculator")
 ```
  
  
  
 -on the next step create an instance of Calculator object
 ```python
 calc_ = Calculator()
 ```
  
  
  
 *the argument can be passed during the initialization*
 ```python
 your_expression = "2+2+3"
 calc_ = Calculator(your_expression)
 ```
  
  
  
 -to solve expression use method **.calc()** that returns float number:
 ```python
 print(calc_.calc())
 ```
  
   
    
 -to load new expression use method **.load_new_expression** that returns pointer to the object in order to be able to use method **.calc()** instantly
 ```python
 your_exp = input()
 
 print(calc_.load_new_expression(your_exp).calc())
 
 # the same result
 calc_.load_new_expression(your_exp)
 print(calc_.calc())
 
 ```
 
 
 
