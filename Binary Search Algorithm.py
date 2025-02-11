#Python Projects for beginners
#Binary Search Algorithm
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#binary-search-algorithm


def binary_search(sorted_list, search_value):
    """
    Perform a binary search on a sorted list to find the index of the search value.

    Args:
        sorted_list (list): A sorted list of elements.
        search_value: The value to search for in the list.

    Returns:
        int: The index of the search value if found, otherwise -1.
    """
    left, right = 0, len(sorted_list) - 1  # Define the search boundaries

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if sorted_list[mid] == search_value:  # Check if the middle element is the target
            return mid  # Return the index of the target
        if sorted_list[mid] < search_value:  # If the target is greater, search the right half
            left = mid + 1
        else:  # If the target is smaller, search the left half
            right = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage
SORTED_LIST = [1, 3, 5, 7, 9, 11, 13, 15]
TARGET = 7

RESULT = binary_search(SORTED_LIST, TARGET)

if RESULT != -1:
    print(f"Element found at index {RESULT}")
else:
    print("Element not found in the array")
