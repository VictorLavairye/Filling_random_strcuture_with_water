import time
import random as rd
import numpy as np
import matplotlib.pyplot as plt


def get_index_list(l, element):
    index_list = []
    for i in range(len(l)):
        if l[i] == element:
            index_list.append(i)
    return index_list


def get_volume(construction_list):
    construction_list_length  = len(construction_list)
    if construction_list_length <= 2:
        volume = 0
        return volume
    if construction_list_length == 3:
        volume = max(0, min(construction_list[0], construction_list[2]) - construction_list[2])
        return volume
    else:
        reverse_sorted_list = sorted(construction_list, reverse=True)
        highest_wall = reverse_sorted_list[0]
        highest_wall_index = construction_list.index(highest_wall)
        second_highest_wall = reverse_sorted_list[1]
        second_highest_wall_index_list = get_index_list(construction_list, second_highest_wall)
        second_highest_wall_index_distance_to_highest_wall_index = [
            abs(second_highest_wall_index_list[i] - highest_wall_index)
            for i in range(len(second_highest_wall_index_list))]
        second_highest_wall_index = second_highest_wall_index_list[
            second_highest_wall_index_distance_to_highest_wall_index.index(
                max(second_highest_wall_index_distance_to_highest_wall_index))]
        max_index = max(highest_wall_index, second_highest_wall_index)
        min_index = min(highest_wall_index, second_highest_wall_index)
        #Construction of subset lists from construction_list
        left_construction_list = construction_list[0: min_index + 1]
        middle_construction_list = construction_list[min_index: max_index + 1]
        right_construction_list = construction_list[max_index: len(construction_list)]
        #print(left_construction_list, middle_construction_list, right_construction_list)
        #Computation of the water volume in the middle_construction subset
        if max_index + 1 - min_index > 2:
            volume = second_highest_wall * (max_index - 1 - min_index) - sum(middle_construction_list[1 : max_index - 1])
            #print(middle_construction_list, middle_construction_list[1 : max_index], second_highest_wall * (max_index - 1 - min_index), sum(middle_construction_list[1 : max_index - 1]))
            return volume + get_volume(left_construction_list) + get_volume(right_construction_list)
        else:
            return get_volume(left_construction_list) + get_volume(right_construction_list)


"""
N = [100, 500, 1000, 5000]
h = [10, 20, 50, 100, 1000]
j = 0
for n in N:
    print(n)
    total_time = 0
    total_volume = 0
    average_time = [0.0] * len(N)
    average_volume = [0.0] * len(N)
    print(average_volume[0])
    for i in range(0,10000):
        l = [rd.randint(0, h[4]) for j in range(0,n)]
        time_1 = time.time()
        volume = get_volume(l)
        time_2 = time.time() - time_1
        total_time += time_2
        total_volume += volume
    average_time[j] = total_time/10000
    average_volume[j] = total_volume/10000
    print(average_time[j], average_volume[j])
    j += 1
print(average_time)
print(average_volume)


construction_list = [2, 0, 0, 1, 0]
reverse_sorted_list = sorted(construction_list, reverse=True)
print('s_list = ', reverse_sorted_list)
highest_wall = reverse_sorted_list[0]
highest_wall_index = construction_list.index(highest_wall)
second_highest_wall = reverse_sorted_list[1]
second_highest_wall_index_list = get_index_list(construction_list, second_highest_wall)
print('2_h_list = ', second_highest_wall_index_list)
second_highest_wall_index_distance_to_highest_wall_index = [abs(second_highest_wall_index_list[i] - highest_wall_index)
                                                            for i in range(len(second_highest_wall_index_list))]
print('indexes_distance = ', second_highest_wall_index_distance_to_highest_wall_index)
second_highest_wall_index = second_highest_wall_index_list[second_highest_wall_index_distance_to_highest_wall_index.index(max(second_highest_wall_index_distance_to_highest_wall_index))]
print('highest_wall = ', highest_wall, '  secon_highest_wall = ', second_highest_wall)
print('highest_wall_index = ', highest_wall_index, '  second_highest_wall_index = ', second_highest_wall_index)
max_index = max(highest_wall_index, second_highest_wall_index)
min_index = min(highest_wall_index, second_highest_wall_index)
left_construction_list = construction_list[0 : min_index + 1]
middle_construction_list = construction_list[min_index : max_index + 1]
right_construction_list = construction_list[max_index : len(construction_list)]
print(left_construction_list, middle_construction_list, right_construction_list)
"""
N = [100, 500, 1000, 5000]
h = [10, 20, 50, 100, 1000]

t_N_h_10 = [3.418853282928467e-05, 0.00010270278453826905, 0.00018180413246154784, 0.0008590479612350464]
v_N_h_10 = [446.3436, 2446.6061, 4946.7381, 24945.6098]

t_N_h_20 = [3.83847713470459e-05, 0.00010116238594055175, 0.00017894892692565918, 0.0009477747917175293]
v_N_h_20 = [865.9229, 4866.2582, 9865.4247, 49874.5016]

t_N_h_50 = [5.37524938583374e-05, 0.00013159544467926024, 0.00021569743156433106, 0.0010141419887542726]
v_N_h_50 = [2100.7542, 12065.997, 24565.7737, 124551.772]

t_N_h_100 = [5.6729578971862794e-05, 0.00016744229793548584, 0.00027388546466827394, 0.0010884382963180542]
v_N_h_100 = [4151.0613, 23963.2965, 48947.5686, 248945.4436]

t_N_h_1000 = [8.092024326324464e-05, 0.0003054753065109253, 0.0007216449975967407, 0.0025950706243515016]
v_N_h_1000 = [41130.1953, 237288.8558, 485763.1676, 2484169.5902]

x = np.arange(0, 5000)
f_n_h_10 = [0.0] * len(x)
f_n_h_20 = [0.0] * len(x)
f_n_h_50 = [0.0] * len(x)
f_n_h_100 = [0.0] * len(x)
f_n_h_1000 = [0.0] * len(x)
for i in range(0, 100):
    f_n_h_10[i] = (t_N_h_10[0]/100) * i
    f_n_h_20[i] = (t_N_h_20[0]/100) * i
    f_n_h_50[i] = (t_N_h_50[0] / 100) * i
    f_n_h_100[i] = (t_N_h_100[0] / 100) * i
    f_n_h_1000[i] = (t_N_h_1000[0]/100) * i
for i in range(100, 500):
    f_n_h_10[i] = (t_N_h_10[1] - t_N_h_10[0]) / (500 - 100) * i + (
            t_N_h_10[0] - 100 * (t_N_h_10[1] - t_N_h_10[0]) / (500 - 100))
    f_n_h_20[i] = (t_N_h_20[1] - t_N_h_20[0]) / (500 - 100) * i + (
            t_N_h_20[0] - 100 * (t_N_h_20[1] - t_N_h_20[0]) / (500 - 100))
    f_n_h_50[i] = (t_N_h_50[1] - t_N_h_50[0]) / (500 - 100) * i + (
            t_N_h_50[0] - 100 * (t_N_h_50[1] - t_N_h_50[0]) / (500 - 100))
    f_n_h_100[i] = (t_N_h_100[1] - t_N_h_1000[0]) / (500 - 100) * i + (
            t_N_h_100[0] - 100 * (t_N_h_100[1] - t_N_h_100[0]) / (500 - 100))
    f_n_h_1000[i] = (t_N_h_1000[1] - t_N_h_1000[0]) / (500 - 100) * i + (
            t_N_h_1000[0] - 100 * (t_N_h_1000[1] - t_N_h_1000[0]) / (500 - 100))
for i in range(500, 1000):
    f_n_h_10[i] = (t_N_h_10[2] - t_N_h_10[1]) / (1000 - 500) * i + (
            t_N_h_10[1] - 500 * (t_N_h_10[2] - t_N_h_10[1]) / (1000 - 500))
    f_n_h_20[i] = (t_N_h_20[2] - t_N_h_20[1]) / (1000 - 500) * i + (
            t_N_h_20[1] - 500 * (t_N_h_20[2] - t_N_h_20[1]) / (1000 - 500))
    f_n_h_50[i] = (t_N_h_50[2] - t_N_h_50[1]) / (1000 - 500) * i + (
            t_N_h_50[1] - 500 * (t_N_h_50[2] - t_N_h_50[1]) / (1000 - 500))
    f_n_h_100[i] = (t_N_h_100[2] - t_N_h_100[1]) / (1000 - 500) * i + (
            t_N_h_100[1] - 500 * (t_N_h_100[2] - t_N_h_100[1]) / (1000 - 500))
    f_n_h_1000[i] = (t_N_h_1000[2] - t_N_h_1000[1]) / (1000 - 500) * i + (
            t_N_h_1000[1] - 500 * (t_N_h_1000[2] - t_N_h_1000[1]) / (1000 - 500))
for i in range(1000, 5000):
    f_n_h_10[i] = (t_N_h_10[3] - t_N_h_10[2]) / (5000 - 1000) * i + (
            t_N_h_10[2] - 1000 * (t_N_h_10[3] - t_N_h_10[2]) / (5000 - 1000))
    f_n_h_20[i] = (t_N_h_20[3] - t_N_h_20[2]) / (5000 - 1000) * i + (
            t_N_h_20[2] - 1000 * (t_N_h_20[3] - t_N_h_20[2]) / (5000 - 1000))
    f_n_h_50[i] = (t_N_h_50[3] - t_N_h_50[2]) / (5000 - 1000) * i + (
            t_N_h_50[2] - 1000 * (t_N_h_50[3] - t_N_h_50[2]) / (5000 - 1000))
    f_n_h_100[i] = (t_N_h_100[3] - t_N_h_100[2]) / (5000 - 1000) * i + (
            t_N_h_100[2] - 1000 * (t_N_h_100[3] - t_N_h_100[2]) / (5000 - 1000))
    f_n_h_1000[i] = (t_N_h_100[3] - t_N_h_1000[2]) / (5000 - 1000) * i + (
            t_N_h_1000[2] - 1000 * (t_N_h_1000[3] - t_N_h_1000[2]) / (5000 - 1000))


plt.plot(x, f_n_h_10)
plt.plot(x, f_n_h_20)
plt.plot(x, f_n_h_50)
plt.plot(x, f_n_h_100)
plt.plot(x, f_n_h_1000)
plt.show()