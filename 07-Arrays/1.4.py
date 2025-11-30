'''
An array contains values: 2, 3, 7, 5, 4. Write a program that prints:

the array
number of elements
first value
second value
last value
last but one value (do not use negative index values)
sum of the first and last value
middle value
all array values separated by a single space (use a loop statement)
###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[...])
print('Second value', arr[...])
...
'''


arr=[2,3,7,5,4]
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print("last value: ", arr[-1])
print("last but one value: ", arr[-2])
print("sum of the first and the last value: ", arr[0]+arr[-1])
print("middle value: ", arr[len(arr)//2])



