# 按行读取txt文件，保留每行第二个和第五个元素，写入到另一个json文件

import os
import json

def process_file(file_path, output_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                continue
            elements = line.split()
            for i in elements:
                if len(i)==3:
                    flag = False
                    for ii in i:
                        #如果ii属于A Z的大写字母
                        if ord(ii) >= 65 and ord(ii) <= 90:
                            continue
                        else : 
                            flag = True
                            break
                    if flag == False:
                        # 将数据添加到字典中
                        data[i] = elements[1]
                else :
                    continue

    # 将字典写入 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    file_path = "data.txt"
    output_path = "output.json"
    process_file(file_path, output_path)
    print("Done")