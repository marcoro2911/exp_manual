def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

input_string = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, input_string.split()))
print("Original array:", numbers)
bubbleSort(numbers)
print("Sorted array:", numbers)