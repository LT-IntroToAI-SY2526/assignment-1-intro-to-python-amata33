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
[I'm learning Python basics in a high school programming class. I have some experience with coding but only with Java, since I took AP Computer Science A sophomore year (2 years ago). Can you create 5-7 practice problems that cover: Variables and basic data types Conditionals (if/elif/else) Loops (for and while) Functions Basic list operations]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 6-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

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
# Function Syntax Quiz

score = 0

# Question 1
answer1 = input("1️⃣ Fill in the blank to define a function:\n___ greet():\n    print('Hi')\nYour answer: ")
if answer1.strip().lower() == "def":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Nope! The correct answer is 'def'.")

# Question 2
answer2 = input("\n2️⃣ What symbol starts the function body?\nYour answer: ")
if answer2.strip() == ":":
    print("✅ Correct!")
    score += 1
else:
    print("❌ It's ':' (colon).")

# Question 3
answer3 = input("\n3️⃣ What keyword is used to send back a value from a function?\nYour answer: ")
if answer3.strip().lower() == "return":
    print("✅ Nailed it!")
    score += 1
else:
    print("❌ It's 'return'.")

# Question 4
answer4 = input("\n4️⃣ What’s wrong with this function?\n   def say_hi(name)\n       print('Hi ' + name)\nYour answer: ")
if "colon" in answer4.lower() or ":" in answer4:
    print("✅ Yep! It's missing a colon after the function declaration.")
    score += 1
else:
    print("❌ It's missing a colon ':' after say_hi(name).")

# Final Score
print(f"\n🎉 You scored {score}/4!")











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


