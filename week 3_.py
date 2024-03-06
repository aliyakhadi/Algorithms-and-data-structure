def solve(self, A, B):
    zero_i_list = []
    n = len(A)
    for i in range(n):
        if A[i] == 0:
            zero_i_list.append(i)
    zero_index = 0
    start = 0
    current_len, count_zeroes, maxlen = 0, 0, 0
    for i in range(n):
        current_len += 1
        if A[i] == 0:
            count_zeroes += 1
        if count_zeroes > B:
            count_zeroes -= 1
            current_len -= len(A[start:zero_i_list[zero_index]+1])
            start = zero_i_list[zero_index] + 1
            zero_index += 1
        maxlen = max(maxlen, current_len)
    return maxlen


print(solve(0, [1, 0, 0, 1, 1, 0, 1], 1))

# time complexity is O(n)
# memory complexity is O(1) but if number of zeroes is close to n it is O(n)

#Correct
