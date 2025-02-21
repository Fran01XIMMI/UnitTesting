class MathUtils:
  """
  Class that implements mathematical operations.
  """
  
  @staticmethod
  def add(a: int | float, b: int | float) -> int | float:
    """
    Just adds two numbers together.
    """
    return a + b

  @staticmethod
  def subtract(a: int | float, b: int | float) -> int | float:
    """
    Just subtracts two numbers.
    """
    return a - b

  @staticmethod
  def divide(a: int | float, b: int | float) -> float:
    """
    Just divides two numbers.
    """
    if b == 0:
      raise ValueError("You cannot divide by zero!")
    return a / b 
  

# Add more functions of the Utility math

  @staticmethod
  def multiply(a: int | float, b: int | float) -> float:

    return a * b
  
  @staticmethod
  def exponent(a: int | float, b: int | float) -> float:

    return a ** b
  
  @staticmethod
  def mod(a: int | float, b: int | float) -> float:

    if b == 0:
      raise ValueError("You cannot divide by zero!")
    return a % b