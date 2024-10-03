import multiprocessing
from datetime import datetime


def read_info(*filenames):
    all_data = []
    start = datetime.now()
    for filename in filenames:
        my_file = open(f'{filename}', 'r')
        while True:
            r_r = my_file.readline()
            if not r_r:
                break
            all_data.append(r_r)
    end = datetime.now()
    return end - start


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    print(read_info(*filenames))

    with multiprocessing.Pool(processes=4) as pool:
        start1 = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start1)
