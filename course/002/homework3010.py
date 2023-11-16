def sort_by_column(column, top):
    data_copy = data.copy()
    data_copy.sort(key=lambda x: x[column])

    result = []
    while len(result) < top:
        result.append()

def change_top():
    global top
    user_top = int(input())