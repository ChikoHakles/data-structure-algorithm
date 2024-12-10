import search_algorithm as sa
import random as r

data_size = 10000
test_count = 100
data = sa.append_data(data_size)

data_seq = []
data_bin = []
def main():
    for i in range(test_count):
        inp = r.randint(0, data_size)
        res_seq = sa.seq_search(data, inp)
        res_bin = sa.binary_search(data, inp)
        data_seq.append(res_seq)
        data_bin.append(res_bin)
    print("Below are result of search, formatted as (Value to Search, Loop Count) : ")
    print("  Sequential Search Highest :", max(data_seq))
    print("  Binary Search Highest :", max(data_bin))
    print("  Sequential Search Lowest :", min(data_seq))
    print("  Binary Search Lowest:", min(data_bin))


if __name__ == "__main__":
    main()