# 11. Sum, Product, and Subtraction
def operations(a, b):
    add = a + b
    product = a * b
    subtract = a - b
    return add, product, subtract

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add, product, subtract = operations(num1, num2)
print("Addition:", add, "Product:", product, "Subtraction:", subtract)

# 12. Frequency of Words
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

sentence = input("Enter a sentence: ")
print("Word Frequency:", word_frequency(sentence))

# 13. Gross Salary
def calculate_gross_salary(basic_salary):
    da = 0.8 * basic_salary
    hra = 0.2 * basic_salary
    gross_salary = basic_salary + da + hra
    return gross_salary

basic_salary = float(input("Enter basic salary: "))
print("Gross Salary:", calculate_gross_salary(basic_salary))

# 14. Total and Average
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

input_numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in input_numbers]
total, average = calculate_stats(numbers)
print(f"Total: {total}, Average: {average:.2f}")
