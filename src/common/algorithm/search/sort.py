# 冒泡排序 从小到大排序 n-1趟 比较2个相邻的数字，将较小的数字排到前面 时间复杂度 O(n^2)
def bubble_sort(list_data):
    for i in range(len(list_data) - 1):  # 第i趟
        for j in range(len(list_data) - i - 1):  # 指向位置 从索引0开始
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
        print(list_data)
    return list_data


# 如果某一趟，没有任何交换，说明已经排好序，已经不需要再次排序
def better_bubble_sort(list_data):
    for i in range(len(list_data) - 1):  # 第i趟
        flag = False
        for j in range(len(list_data) - i - 1):  # 指向位置 从索引0开始
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
                flag = True
        print(list_data)
        if not flag:
            return list_data
    return list_data


# 简单选择排序 遍历列表，每次找到最小的元素，放到一个新列表中. 不推荐：创建了新list,内存消耗，有remove操作 时间复杂度O(n^2)
def simple_select_sort(list_data):
    list_new = []
    for i in range(len(list_data)):
        min_value = min(list_data)
        list_new.append(min_value)
        list_data.remove(min_value)
    print(list_new)

if __name__ == "__main__":
    list_data = [4, 6, 3, 7, 8, 9, 1]
    better_bubble_sort(list_data)
    simple_select_sort(list_data)
