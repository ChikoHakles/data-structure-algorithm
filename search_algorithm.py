def append_data(count):
    data = []
    for i in range(1, count):
        data.append(i)
    return data

#mencari data secara berurutan dari index 0
def seq_search(data, search):
    i = -1
    loop = 0
    while 1:
        #naik 1 index setiap loop
        i = i+1
        loop = loop + 1
        if data[i] == search:
            #selesai saat mendapat angka yang sesuai
            break
    return i, loop

#mencari data dari tengah, dan akan mengarah ke angka yang lebih kecil / besar sesuai komparasi pertama
def binary_search(data, search):
    #index awal = 0, index akhir = jumlah data, index tengah = jumlah data dibagi 2
    min_index = 0
    max_index = len(data)
    to_search = int(max_index/2)
    i = -1
    loop = 0
    while 1:
        #setiap perulangan akan cek, apakah angka sama, lebih kecil, atau lebih besar
        loop = loop + 1
        #jika lebih kecil, maka akan ke kiri garis bilangan (cari yang lebih kecil dari angka tengah)
        if search < data[to_search]:
            max_index = to_search
            to_search = int(max_index/2)
        #jika lebih besar, maka akan ke kanan garis bilangan (cari yang lebih besar dari angka tengah)
        elif search > data[to_search]:
            min_index = to_search
            to_search = min_index + int((max_index - min_index)/2)
        #jika sama, maka itulah angka yg dicari
        else :
            i = to_search
            break
    return i, loop