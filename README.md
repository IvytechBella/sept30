# sept30

def myRange(start=None, stop=None, step=None):
    # Handle the parameters based on what was provided
    if stop is None:  
        stop = start
        start = 0  
    if step is None:  
        step = 1
    
    # Create an empty list to store the range values
    result = []
    
    # Generate the numbers based on start, stop, and step
    if step > 0:  # Incremental range
        while start < stop:
            result.append(start)
            start += step
    elif step < 0:  # Decremental range
        while start > stop:
            result.append(start)
            start += step

    return result

# Test the function
if __name__ == "__main__":
    print(myRange(10))          
    print(myRange(1, 10))        
    print(myRange(1, 10, 2))     
    print(myRange(10, 0, -2))   
