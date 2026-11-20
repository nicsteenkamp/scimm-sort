import random

type num = int

### LINEAR SEARCH SCIMMING ###
# while True:
#     complexity += 1
#     if elem >= buckets[i][-1]:
#         buckets[i].append(elem)
#         break
#     i += 1
#     if i >= len(buckets):
#         buckets.append([elem])
#         break
###                       ###

def merge(arr: list[list[num]]):
    complexity = 0
    arr_out = []
    top_position = [0]*len(arr)
    while True:
        min_val: num|None = None
        min_val_index = 0
        min_val_pos = 0
        for index in range(len(arr)):
            pos = top_position[index]
            if len(arr[index]) > pos:
                complexity += 1
                if min_val is None:
                    min_val = arr[index][pos]
                    min_val_index = index
                    min_val_pos = pos
                else:
                    complexity += 1
                    if arr[index][pos] < min_val:
                        min_val = arr[index][pos]
                        min_val_index = index
                        min_val_pos = pos

        if min_val is None:
            break
        arr_out.append(arr[min_val_index][min_val_pos])
        top_position[min_val_index] += 1
    return arr_out,complexity


def heap_merge(arr: list[list[num]]) ->list[num]:
    complexity = 0
    merged_arr = []
    while arr[0][0] < len(arr[0]):
        head = arr[0][0]
        merged_arr.append(arr[0][head])
        arr[0][0] += 1
        pointer = 0
        head = arr[0][0]
        pointer_empty = head >= len(arr[pointer])
        while True:
            swap = False
            l = pointer*2+1
            r = pointer*2+2
            comp_index = -1
            comp_index_head = -1
            if r < len(arr):
                l_head = arr[l][0]
                l_empty = l_head >= len(arr[l])
                complexity +=1
                r_head = arr[r][0]
                r_empty = r_head >= len(arr[r])
                complexity += 1
                if not (l_empty and r_empty):
                    if l_empty:
                        comp_index= r
                        comp_index_head = r_head
                    elif r_empty:
                        comp_index= l
                        comp_index_head = l_head
                    else:
                        complexity += 1
                        if arr[l][l_head] > arr[r][r_head]:
                            comp_index = r
                            comp_index_head = r_head
                        else:
                            comp_index = l
                            comp_index_head = l_head
            elif l < len(arr):
                l_head = arr[l][0]
                l_empty = l_head >= len(arr[l])
                if not l_empty:
                    comp_index = l
                    comp_index_head = l_head

            if comp_index != -1:
                complexity += 1
                if pointer_empty or arr[comp_index][comp_index_head] < arr[pointer][head]:
                    arr[comp_index], arr[pointer] = arr[pointer], arr[comp_index]
                    pointer = comp_index
                    swap = True
            if swap ==False:
                break
    return merged_arr,complexity



def heapify(arr: list[list[num]]):
    complexity = 0
    for index in range(1,len(arr),1):
        pointer = index
        while True:
            swap = False
            parent_index = (pointer-1) // 2
            if arr[parent_index][1] > arr[pointer][1]:
                complexity += 1
                arr[pointer], arr[parent_index] = arr[parent_index], arr[pointer]
                pointer = parent_index
                swap = True
            if not swap or pointer == 0:
                break
    return complexity



def scim_sort(arr:list[num])->list[num]:
    complexity = 0
    buckets = [[1,arr[0]]]
    for elem in arr[1:]:
        # i = 0
        # while True:
        low_b = 0
        hi_b = len(buckets)

        while low_b < hi_b:
            mid = (low_b + hi_b) // 2

            complexity += 1
            if buckets[mid][-1] > elem:
                low_b = mid + 1
            else:
                hi_b = mid

        # complexity += 1
        if low_b < len(buckets):
            buckets[low_b].append(elem)
        else:
            buckets.append([1,elem])

    # print(complexity)

    # merged,comp = merge(buckets)
    heap_comp = heapify(buckets)
    # print(buckets)
    arr_sorted,merge_comp = heap_merge(buckets)
    print(arr_sorted)
    # print(buckets)
    # print(len(merged),',',comp+complexity)
    # print(merged)

    # return merged
    print(f"{complexity} | {heap_comp} | {merge_comp} -> {complexity+heap_comp+merge_comp}")

if __name__ == "__main__":
    test = [random.randint(1, 20) for i in range(1000000)]
    scim_sort(test)
