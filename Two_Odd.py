def TwoOdd(arr, size):
    xorof2 = arr[0]
    x = 0
    y = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

        SetBit = xorof2 & ~(xorof2 - 1)
        
    for i in range(size):
        if arr[i] & SetBit:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
        
    print("Two odd occuring elements are", x, "and", y)
    
arr = []
arr_size = int(input("Enter the size of the array: "))

for i in range(arr_size):
    z = int(input("Enter element: "))
    arr.append(z)

TwoOdd(arr, arr_size) 