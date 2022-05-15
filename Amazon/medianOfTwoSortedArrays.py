
def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]

def medianOfTwoSortedArrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    print(arr1)
    return median(arr1)

nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [2, 3, 4, 5]
print(medianOfTwoSortedArrays(nums1, nums2))
# print(median(nums1))


# print(median(nums1))
