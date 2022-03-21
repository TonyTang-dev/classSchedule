import copy
import json


def main1(result):
    li = []

    js = {
        "name": ['', '', '', '', ''],
        "classroom": ['', '', '', '', ''],
        "teacher": ['', '', '', '', ''],
        "flex": [2, 2, 2, 2, 2],
        "id": [0, 0, 0, 0, 0],
    }

    for i in range(7):
        tempJs = copy.deepcopy(js)
        li.append(tempJs)

    # with open("test.txt", "r") as f:
    # while True:
    for line in result:
        # line = f.readline()
        if not line:
            break

        lineArray = line.split(",")
        item = li[int(lineArray[4]) - 1]
        index = int(lineArray[5])

        item["name"][index] = lineArray[1]
        item["classroom"][index] = lineArray[3]
        item["teacher"][index] = lineArray[2]
        item["flex"][index] = int(lineArray[-1])
        item["id"][index] = int(lineArray[0])

    print(li)


def main(result):

    if len(result) == 0:
        return None

    parentDir = {}
    li = []

    js = {
        "name": ["", "", "", "", ""],
        "classroom": ["", "", "", "", ""],
        "teacher": ["", "", "", "", ""],
        "flex": ["2", "2", "2", "2", "2"],
        "id": ["0", "0", "0", "0", "0"],
    }

    for i in range(25):
        for j in range(7):
            tempJs = copy.deepcopy(js)
            li.append(tempJs)
        i = str(i)
        parentDir[i] = li
        li = copy.deepcopy(li)
        li.clear()

    # print(parentDir)

    # return

    # with open("class.txt", "r") as f:
    week = -1
    # while True:
    for line in result:
        week += 1
        # line = f.readline()
        if not line:
            break
        # if line == "\n":
        #     week += 1
        #     continue

        weekIndex = str(week)
        tempWeekLi = parentDir[weekIndex]

        lineArray = line.split(",")
        item = tempWeekLi[int(lineArray[4]) - 1]  # 星期几索引
        index = int(lineArray[5])   # 课程索引

        item["name"][index] = lineArray[1]
        item["classroom"][index] = lineArray[3]
        item["teacher"][index] = lineArray[2]
        item["flex"][index] = lineArray[-1][0]
        item["id"][index] = lineArray[0]

    print(parentDir)
    print(json.dumps(parentDir, ensure_ascii=False))

    return json.dumps(parentDir, ensure_ascii=False)


# if __name__ == '__main__':
#     main()