# Write a python function to count true booleans in the given list.

def count_true(bools: list[bool]) -> int:
    return bools.count(True)

if __name__ == "__main__":
    
    print(count_true([True, False, False, True, False, True, True, False]))