import random

import LPSort
cost_max = 0
ins_sum = 0
comp_sum = 0
for i in range(100):
    test = [random.randint(0,100) for i in range(500)]

    # print(test)
    predicted, complexity = LPSort.linear_prediction_ranking(test)
    comp_sum += complexity
    ranked,insertions = LPSort.insertion_sort(predicted)
    ins_sum += insertions

    if complexity+insertions > cost_max:
        cost_max = complexity+insertions

    list.sort(test)

    is_sorted = True
    for i in range(len(ranked)):
        if ranked[i] != test[i]:
            is_sorted = False
            break
    print(is_sorted)

print("avrg insersions", ins_sum / 100)
print("avrg complexity", comp_sum / 100)
print("avrg Total comp", (comp_sum+ins_sum)/100)
print("max:", cost_max)

#
# if sorted:
#     print(ranked)
#     print("Sorted")
#     print("insertions: ",insertions)
# else:
#     print("Not sorted")
#     print("ranked: ",ranked)
#     print("true: ",test)
