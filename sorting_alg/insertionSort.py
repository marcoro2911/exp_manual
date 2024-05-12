def insertionSort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


input_string = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, input_string.split()))
print("Original array:", numbers)
insertionSort(numbers)
print("Sorted array:", numbers)