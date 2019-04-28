def get_file_data(num, filename):
    data = []
    with open(filename, 'r') as f:
        while True:
            line_str = f.readline().strip()
            # print('读取一行信息：', line_str)
            if not line_str:
                break
            if '[' in line_str:
                str = line_str[:line_str.rindex('[')].replace(' ', '')
            else:
                str = line_str
            # print('读取数据长度：', len(line_str))
            if len(str) != 74:
                # print('数据长度有误')
                continue

            data.append(int(str[num * 2: num * 2 + 2], 16))
    return data
