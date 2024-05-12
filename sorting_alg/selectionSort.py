def selectionSort(arr):
  n = len(arr)
  for i in range(n-1):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


input_string = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, input_string.split()))
print("Original array:", numbers)
selectionSort(numbers)
print("Sorted array:", numbers)