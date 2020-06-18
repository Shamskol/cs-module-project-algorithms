'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    no_duplicate = []
    for i in arr:
        if i not in no_duplicate:
            no_duplicate.append(i)
        else:
            no_duplicate.remove(i)  
    return no_duplicate.pop()             

  #   Time complexity:O(n)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")