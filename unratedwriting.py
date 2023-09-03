import time

def typewrite(text, delay=0.05):
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        time.sleep(0.4)  # Print a newline character at the end

    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
