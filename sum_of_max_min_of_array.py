def get_sum_of_max_min_of_array(num_array):
    max_element = num_array[0]
    min_element = num_array[0]
    for element in num_array[1:]:
        if element > max_element:
            max_element = element
        if element < min_element:
            min_element = element
    return max_element + min_element


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    print("Sum of maximum amd minimum element in array is : ", get_sum_of_max_min_of_array(nums_array))
except ValueError:
    print("Invalid input. Enter Only Integers")
