
A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))
equation = ''
if A == 1:
  
    equation+= 'x^2' 
  
elif A == -1:
  equation += "- x^2"
elif A != 0:
  equation += f"{A}x^2 = 0"
# Handle B coefficient
if B == 1:
  if equation:
    equation += " + x"
  else:
    equation += "x"  
elif B == -1:
  if equation:
    equation += " - x"
  else:
    equation += "- x"
elif B > 0:
  if equation:
    equation += f" + {B}x "
  else:
    equation += f"{B}x"
elif B < 0:
  if equation:
    equation += f" - {-B}x"
  else:
    equation += f"- {-B}x = 0"
# Handle C coefficient
if C > 0:
  if equation:
    equation += f" + {C} = 0"
  else:
    equation += f"{C} = 0"
elif C < 0:
  if equation:
    equation += f" - {-C} = 0"
  else:
    equation += f"- {-C} = 0"
print('The quadratic equation is', equation)




