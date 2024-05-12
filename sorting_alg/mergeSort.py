def merge(arr, left, mid, right):
  n1 = mid - left + 1
  n2 = right - mid
  left_arr = [0] * n1
  right_arr = [0] * n2
  for i in range(0, n1):
    left_arr[i] = arr[left + i]
  for j in range(0, n2):
    right_arr[j] = arr[mid + 1 + j]
  i = 0
  j = 0
  k = left
  while i < n1 and j < n2:
    if left_arr[i] <= right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1
  while i < n1:
    arr[k] = left_arr[i]
    i += 1
    k += 1
  while j < n2:
    arr[k] = right_arr[j]
    j += 1
    k += 1

def mergeSort(arr, left, right):
  if left < right:
    mid = left + (right - left) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)
  return arr


input_string = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, input_string.split()))
print("Original array:", numbers)
mergeSort(numbers, 0, len(numbers) - 1)
print("Sorted array:", numbers)