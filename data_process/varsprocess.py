from data_process import getsourcedata


def vars_process(var_name_list, lines_num, filename):
    var_list = []
    if var_name_list:
        for var in var_name_list:
            if var.startswith('a'):
                # var_list.append([0 for _ in range(lines_num)])
                # 剥离数字
                var_list.append(getsourcedata.get_file_data(int(var[1:]), filename))
                # print('已经返回')
            else:
                var_list.append([0 for _ in range(lines_num)])
    return var_list
