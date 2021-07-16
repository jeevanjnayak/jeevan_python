def values(list_values):
    list_values = [1, 2, 3, 4, "p", "y", "a", 8.54, 5.44, 4.87]
    int_value = []
    float_value = []
    string_value = []
    for i in list_values:
        if type(i) == int:
            int_value.append(i)