

def load_array(file_name):
    with open(file_name,"r") as f:
        str_array = f.readlines()
    return list(map(int,str_array))

def count_sort(array): # do not modity the origin array
    n = len(array)
    if n > 1:
        left_count, left_array = count_sort(array[:n//2])
        right_count, right_array = count_sort(array[n//2:])
        split_count, merge_array = merge_count(left_array,right_array)

        return left_count+right_count+split_count, merge_array
    else:
        return 0,array 
def merge_count(left, right):
    l = len(left)
    r = len(right)
    count_inversion = 0
    i, j = 0,0
    merged = []
    while i < l and j < r:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            count_inversion += l-i
            merged.append(right[j])
            j += 1
    while i< l :
        merged.append(left[i])
        i += 1
    while j< r :
        merged.append(right[j])
        j += 1
    return count_inversion, merged
if __name__ == "__main__":

    file_name = "IntegerArray.txt"
    array = load_array(file_name)
    test_case1 = [3,2,1]
    test_case2 = [4,2,1,3,6,5]
    assert count_sort(test_case1) == (3,[1,2,3])
    assert count_sort(test_case2) == (5,[1,2,3,4,5,6])
    print("test cases passed !!!")
    print(count_sort(array)[0])