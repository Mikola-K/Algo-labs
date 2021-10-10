from main import heap_sort

print("Input elements using ',' ")
lst = list(map(int, input().split(",")))
print("Input asc or desc")
sort_order = input()

heap_sort(lst, sort_order)
