def print_id(variable_name: str, variable):
    """
    Prints the id of the given variable.

    Args: 
        variable_name (str): The name of the variable as a string.
        variable: The variable whose id is to be printed.
    """
    print(f"id({variable_name}): {id(variable)}")
    pass

def main():
    original_list = [1, 2, 3]
    new_list = original_list
    
    print_id("original_list", original_list)
    print_id("new_list", new_list)

if __name__ == "__main__":
    main()