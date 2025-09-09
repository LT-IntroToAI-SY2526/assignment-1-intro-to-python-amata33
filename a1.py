# Assignment 1: AI-Generated Python Problems
# Name: [Aaron Mata]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[give me, in python code, coding problems in python for a beginner. I'm only experienced with Java and want to learn another coding language]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 6-7 practice problems that cover..."
"""
# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================
# Python Coding Problems for Java Developers
# These problems introduce key Python concepts and syntax

# Problem 1: Basic Syntax and Variables
# Write a function that takes a name and age, then returns a formatted string
# Java equivalent would use String concatenation or String.format()
def introduce_yourself(name, age):
    whattoReturn = "hello, I'm " + name + "and I'm " + age + " years old":
    """
    Return a string like "Hello, I'm Alice and I'm 25 years old"
    Notice: No explicit type declarations needed!
    """
    # TODO: Implement this function
    return whattoReturn

# Test your function
# print(introduce_yourself("Alice", 25))


# Problem 2: Lists vs Arrays
# Create a function that finds the second largest number in a list
# Notice how Python lists are more flexible than Java arrays
def second_largest(numbers):
    
    """
    Find the second largest number in a list
    Example: [1, 3, 4, 2] -> 3
    Handle edge cases like empty lists or lists with < 2 elements
    """
    # TODO: Implement this function
    # Hint: Python's built-in functions like max(), sorted() can help
    

# Test cases
# print(second_largest([1, 3, 4, 2]))  # Should return 3
# print(second_largest([5, 5, 5]))     # Should return 5 or handle duplicates
# print(second_largest([1]))           # Edge case


# Problem 3: Dictionary Usage (like HashMap in Java)
# Count the frequency of each character in a string
def char_frequency(text):
    """
    Count frequency of each character in a string
    Return a dictionary where keys are characters, values are counts
    Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # TODO: Implement using a dictionary
    # Hint: Use dict.get() method or collections.defaultdict
    pass

# Test your function
# print(char_frequency("hello"))


# Problem 4: List Comprehensions (Python's powerful feature)
# Create a function that returns squares of even numbers from a list
def squares_of_evens(numbers):
    """
    Return a list of squares of even numbers
    Example: [1, 2, 3, 4, 5, 6] -> [4, 16, 36]
    
    Try to solve this in two ways:
    1. Using a traditional for loop
    2. Using a list comprehension (Python's concise way)
    """
    # Traditional approach:
    # TODO: Implement with for loop
    
    # List comprehension approach:
    # TODO: Implement with list comprehension
    # Hint: [expression for item in iterable if condition]
    pass

# Test your function
# print(squares_of_evens([1, 2, 3, 4, 5, 6]))


# Problem 5: String Methods and Slicing
# Write a function to check if a string is a palindrome
def is_palindrome(text):
    """
    Check if a string reads the same forwards and backwards
    Ignore case and spaces
    Example: "A man a plan a canal Panama" -> True
    """
    # TODO: Implement this function
    # Hints: 
    # - Use string.lower() method
    # - Use string.replace() to remove spaces
    # - Python string slicing: text[::-1] reverses a string
    pass

# Test cases
# print(is_palindrome("racecar"))      # True
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("hello"))        # False


# Problem 6: Working with Functions as First-Class Objects
# Create a simple calculator that uses functions
def calculator(operation, x, y):
    """
    Perform calculation based on operation string
    Operations: "add", "subtract", "multiply", "divide"
    Example: calculator("add", 5, 3) -> 8
    
    This shows how Python treats functions as first-class objects
    """
    # TODO: Implement this function
    # Hint: You can store functions in a dictionary!
    pass
"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]
Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""












# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


