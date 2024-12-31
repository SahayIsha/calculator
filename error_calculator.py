def safe_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Invalid input. Please enter a number.")
        
