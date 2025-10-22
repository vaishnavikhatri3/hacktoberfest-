def next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n  # initialize all NGEs as -1
    stack = []  # will store indices

    for i in range(n):
        # Pop elements smaller than current
        while stack and arr[i] > arr[stack[-1]]:
            top_index = stack.pop()
            result[top_index] = arr[i]
        stack.append(i)

    return result


# --- Driver Code ---
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    ans = next_greater_elements(arr)
    print("Next Greater Elements:", ans)
