# Write a function to convert snake case string to camel case string.

def snakeCase_to_camelCase(snake_str: str) -> str:

    split_strs = snake_str.split("_")
    
    for i in range(1, len(split_strs)):
        split_strs[i] = split_strs[i].capitalize()

    return "".join(split_strs) 

if __name__ == '__main__':
    print(snakeCase_to_camelCase("snake_case"))
    print(snakeCase_to_camelCase("user_name"))
    print(snakeCase_to_camelCase("student_roll_number"))