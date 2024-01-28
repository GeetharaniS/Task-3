# You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two List one which have all the Even Numbers and another List which will have all the ODD numbers in it ?
#Answer:
nos = [10, 501, 22, 37, 100, 999, 87, 351]

even_nos = [i for i in nos if i % 2 == 0]
odd_nos = [i for i in nos if i % 2 != 0]

print("Even Numbers:", even_nos)
print("Odd Numbers:", odd_nos)

# Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count all the Prime Numbers and create a new Python List which will contain all the Prime Numbers in it ?
#Answer:
print(end="\n")
def is_prime(i):
    if i < 2:
        return False
    for j in range(2, int(i**0.5) + 1):
        if j % i == 0:
            return False
    return True

nos = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [j for j in nos if is_prime(j)]

print(" The Prime Numbers are: ", prime_numbers)
print("Total Count of Prime Numbers are: ", len(prime_numbers))

# Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] Find out how many numbers are there in the given Python List which are Happy Numbers ?
#Answer:
print(end="\n")
def is_happy(i):
    seen = set()
    while i != 1 and i not in seen:
        seen.add(i)
        i = sum(int(digit)**2 for digit in str(i))
    return i == 1

nos = [10, 501, 22, 37, 100, 999, 87, 351]

happy_nos = [i for i in nos if is_happy(i)]

print("Happy Numbers are: ", happy_nos)
print("Count of Happy Numbers is: ", len(happy_nos))

# Write a python program to find the sum of the first and last digit of an integer ?
#Answer:
print(end="\n")
def sum_first_last_digit(nos):
    str_nos = str(nos)
    return int(str_nos[0]) + int(str_nos[-1])

a = input("Enter the integers ")
b = sum_first_last_digit(a)
print("Sum of First and Last Digit:", b)
# You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable number of Mangoes. There are M students in a Guvi class, your task is to distribute the Mangoes in such a way that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with minimum Mangoes given to the student is minimum ?
#Answer:
print(end="\n")
def distribute_mangoes(mangoes_list, students):
    sorted_mangoes = sorted(mangoes_list)
    min_difference = float('inf')
    result_distribution = []

    for i in range(len(sorted_mangoes) - students + 1):
        current_difference = sorted_mangoes[i + students - 1] - sorted_mangoes[i]
        if current_difference < min_difference:
            min_difference = current_difference
            result_distribution = sorted_mangoes[i:i + students]

    return result_distribution

mangoes_list = [10, 5, 20, 15, 8]
students = 3
result = distribute_mangoes(mangoes_list, students)
print("Mangoes Distribution:", result)

# You have been given three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists ?
#Answer:
print(end="\n")
list1 = [1, 2, 3, 4, 5]
list2 = [12, 3, 14, 5, 16]
list3 = [5, 16, 4, 1, 19]

duplicates = set(list1) & set(list2) & set(list3)

print("Duplicates:", list(duplicates))

# Write a python program to find the first non - repeating elements in a given list of integers?
#Answer:
print(end="\n")
def first_non_repeating(nos):
    counts = {}
    
    for num in nos:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num in nos:
        if counts[num] == 1:
            return num
    return None

nos = [1, 7, 1, 6, 9, 6, 7]
result = first_non_repeating(nos)
print("First Non-Repeating Element:", result)

# Write a python program to find the minimum element in a rated and sorted list ?
#Answer:
print(end="\n")
sorted_list = [1, 2, 6, 9,11, 18, 21]

min_element = sorted_list[0]
print("Minimum Element:", min_element)

# You have been given a Python list [10,20,30,9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value ?
#Answer:
print(end="\n")
def find_triplet_sum(nums, target):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [nums[i], nums[j], nums[k]]
    return None

nos = [10, 20, 30, 9]
target_value = 59
result = find_triplet_sum(nos, target_value)
print("Triplet with Sum Equal to", target_value, ":", result)

# Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to Zero ?
#Answer:
print(end="\n")
def sublist_with_zero_sum(numbers):
    prefix_sum = set()
    current_sum = 0

    for num in nos:
        current_sum += num
        if current_sum in prefix_sum or current_sum == 0:
            return True
        prefix_sum.add(current_sum)

    return False

nos = [4, 2, -3, 1, 6]
result = sublist_with_zero_sum(nos)
print("Sub-list with Sum Equal to Zero:", result)
