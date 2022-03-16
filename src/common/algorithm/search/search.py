# 顺序查找，遍历列表，查找
# 问题规模：数组长度， 一个for循环，没有循环减半(logn),即时间复杂度为 O(n)
def linear_search(list_data, k):
    for index, value in enumerate(list_data):
        if k == value:
            print(f"在列表中第{index + 1}个元素中找到了{value}")
            return index
    return None


# 二分查找 时间复杂度 O(logn) list必须有序，如果列表是无序，那么可以直接顺序查询
def binary_search(list_data, k):
    # 使用 left mid right 值位于 左右元素中间 left左边元素下标 right右边元素下标,mid元素中间值下标
    left = 0
    right = len(list_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_data[mid] == k:
            print(f"二分查找，查找到元素，下标是 {mid}")
            return mid
        elif list_data[mid] > k:
            # 中间值大于value,则value位于左侧，移动right 到 mid
            right = mid - 1
        # list_data[mid] < k value位于右侧，移动left 到 mid
        else:
            left = mid + 1
    else:
        return None


if __name__ == '__main__':
    list_data = [1, 2, 3, 3, 4, 5, 6]
    list_data.sort()
    linear_search(list_data, 3)
    binary_search(list_data, 3)
