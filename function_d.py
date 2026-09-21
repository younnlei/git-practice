def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    " remove the commit"
    if not numbers:
        return None
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    print(num)
    return num
    

    # Trying to break the code

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
