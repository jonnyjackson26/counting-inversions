
# Read data from data.py and put it into an array called arr
arr = []
with open('data.py', 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Skip empty lines
            arr.append(int(line))


#count inversions
def count_inversions(array):
    def sort_and_count_inversions(subarray):
        # Base case: a single element has no inversions
        if len(subarray) <= 1:
            return subarray, 0

        # Split the subarray into two halves
        midpoint = len(subarray) // 2
        left_half, inversions_left = sort_and_count_inversions(subarray[:midpoint])
        right_half, inversions_right = sort_and_count_inversions(subarray[midpoint:])

        # Merge the two halves and count cross (split) inversions
        merged_array, split_inversions = merge_and_count_split_inversions(left_half, right_half)
        print(f"Merging {left_half} and {right_half} -> {merged_array} with {split_inversions} split inversions")

        # Total inversions = left side + right side + cross inversions
        total_inversions = inversions_left + inversions_right + split_inversions
        return merged_array, total_inversions

    def merge_and_count_split_inversions(left_half, right_half):
        index_left = index_right = 0
        merged_array = []
        split_inversions = 0

        # Standard merge process with inversion counting
        while index_left < len(left_half) and index_right < len(right_half):
            if left_half[index_left] <= right_half[index_right]:
                merged_array.append(left_half[index_left])
                index_left += 1
            else:
                merged_array.append(right_half[index_right])
                # Every remaining element in left_half is greater than right_half[index_right]
                split_inversions += len(left_half) - index_left
                index_right += 1

        # Append any leftovers
        merged_array.extend(left_half[index_left:])
        merged_array.extend(right_half[index_right:])

        return merged_array, split_inversions

    # Start recursion and return only the inversion count (ignoring the sorted array)
    _, total_inversions = sort_and_count_inversions(array)
    return total_inversions


print(count_inversions(arr))





""" BRUTE FORCE APPROACH
inversions=0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i]>arr[j]:
            inversions+=1
print(inversions)
"""


