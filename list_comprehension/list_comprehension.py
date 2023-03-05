numbers = [1, 2, 3, 4, 5, 6]

evens = [x for x in numbers if x % 2 == 0]
print(evens)
# [2, 4, 6]

odds = [num for num in numbers if num % 2 != 0]
print(odds)
# [1, 3, 5]

print([x for x in numbers if x < 4])
# [1, 2, 3]

list_objects = [{"id": i, "name": "object_" + str(i), }
                for i in range(4)]

print(list_objects)
# [{'id': 0, 'name': 'object_0'}, {'id': 1, 'name': 'object_1'},
# {'id': 2, 'name': 'object_2'}, {'id': 3, 'name': 'object_3'}]

list_objects_filter = [obj for obj in list_objects if obj["id"] < 2]
print(list_objects_filter)
# [{'id': 0, 'name': 'object_0'}, {'id': 1, 'name': 'object_1'}]
