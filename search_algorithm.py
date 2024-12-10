def append_data(count):
    data = []
    for i in range(1, count):
        data.append(i)
    return data

data = append_data(1000)

def seq_search(data, search):
    i = -1
    loop = 0
    while 1:
        i = i+1
        loop = loop + 1
        if data[i] == search:
            break
    return i, loop

def binary_search(data, search):
    min_index = 0
    max_index = len(data)
    to_search = int(max_index/2)
    i = -1
    loop = 0
    while 1:
        loop = loop + 1
        if search < data[to_search]:
            max_index = to_search
            to_search = int(max_index/2)
        elif search > data[to_search]:
            min_index = to_search
            to_search = min_index + int((max_index - min_index)/2)
        else :
            i = to_search
            break
    return i, loop

def main():
    print(data)
    inp  = int(input("Input an int : "))
    res_seq = seq_search(data, inp)
    res_bin = binary_search(data, inp)
    print("Sequential Search : Integer", inp, "Found in index", res_seq[0]) if res_seq[0] != -1 else print("Integer not found")
    print("Loop :", res_seq[1], "times")
    print("Binary Search : Integer", inp, "Found in index", res_bin[0]) if res_bin[0] != -1 else print("Integer not found")
    print("Loop :", res_bin[1], "times")

if __name__ == "__main__":
    main()