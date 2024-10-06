# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division and handles errors such as division by zero and non-numeric inputs.
    
    Args:
    numerator (any): The numerator for the division.
    denominator (any): The denominator for the division.
    
    Returns:
    str: The result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Both numerator and denominator must be numbers."
    
    else:
        # Return simplified result message
        return f"The result of the division is {result}"

# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments and perform division.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform division using the safe_divide function
    result = safe_divide(numerator, denominator)

    # Display result or error
    print(result)

if __name__ == "__main__":
    main()

