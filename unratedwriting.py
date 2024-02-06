import time

def typewrite(text, delay=0.05):
    """
    This prints like a typewriter
    >>> typewrite(090)
    090
    """
    try:
        if not isinstance(text, str):
            try:
               text = str(text)
            except:
                raise TypeError("Input must be convertible to string")
        
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        time.sleep(0.4)  # Print a newline character at the end

    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
