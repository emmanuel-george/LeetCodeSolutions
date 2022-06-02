def binary_search(list_of_numbers):
    left_index = 0
    right_index = len(list_of_numbers) - 1
    mid_index = 0
    while(left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        if(list_of_numbers[mid_index] == number_to_find):
            return mid_index
        elif(number_to_find > mid_index):
            left_index = mid_index +1
        else:
            right_index = mid_index-1;

def recursive_binary_search(list_of_numbers, number_to_find, left_index, right_index):
    if(right_index < left_index):
      return -1

    mid_index = (left_index + right_index ) //2
    mid_number = list_of_numbers[mid_index]

    if(mid_number == number_to_find):
        return mid_index

    if(mid_number< number_to_find):
        left_index = mid_index + 1
    else:
        right_index = mid_index -1

    return recursive_binary_search(list_of_numbers, number_to_find, left_index, right_index)




if __name__ == '__main__':
    list_of_numbers = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    number_to_find = 99


    index = recursive_binary_search(list_of_numbers,number_to_find, 0, len(list_of_numbers))
    print(f'Number found at index {index} using binary search')
