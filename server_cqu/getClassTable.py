from mycqu.auth import login, NeedCaptcha
from mycqu.mycqu import access_mycqu
import mycqu.course as mc
from requests import Session


def getFlex(a, b):
    if b-a == 1:
        return "2"
    elif b-a == 2:
        return "3"
    else:
        return "1"


def getTime(index):
    _dir = {1: '0', 3: '1', 6: '2', 8: '3', 10: '4'}

    return _dir[index]


def main(author, pwd, stuId):
    result = []  # 用于存储爬取到的结果

    session = Session()
    try:
        login(session, author, pwd)  # 需要登陆
    except NeedCaptcha as e:  # 需要输入验证码的情况
        with open("captcha.jpg", "wb") as file:
            file.write(e.image)
        print("输入 captcha.jpg 处的验证码并回车: ", end="")
        e.after_captcha(input())
    access_mycqu(session)

    timetables = mc.CourseTimetable.fetch(session, stuId)  # 获取学号 201xxxxx 的本学期课表

    # print(timetables)

    _id = 1
    _id_dir = {}

    # with open("C:\\Users\\Administrator\\Desktop\\class.txt", "w") as f:
    for week in range(1, 23):
        # print(f"第 {week} 周的课")
        # f.write("\n")
        weekdays = ["1", "2", "3", "4", "5", "6", "7"]
        for timetable in timetables:
            if timetable.course.name not in _id_dir:
                _id_dir[timetable.course.name] = _id
                _id += 1

            for start, end in timetable.weeks:
                if start <= week <= end:
                    # if timetable.day_time:
                    #     f.write(f"科目：{timetable.course.name},教师：{timetable.course.instructor},教室：{timetable.classroom},"
                    #           f"周{weekdays[timetable.day_time.weekday]},{timetable.day_time.period[0]}~{timetable.day_time.period[1]} 节课\n")
                    # elif timetable.whole_week:
                    #     f.write(f"科目：{timetable.course.name},地点:{timetable.classroom},全周时间\n")
                    # else:
                    #     f.write(f"科目：{timetable.course.name},无明确时间\n")
                    # if timetable.day_time:
                    #     f.write(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},{timetable.classroom},"
                    #           f"{weekdays[timetable.day_time.weekday]},"
                    #           + getTime(timetable.day_time.period[0])+','+getFlex(timetable.day_time.period[0], timetable.day_time.period[1])+"\n")
                    # elif timetable.whole_week:
                    #     f.write(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},{timetable.classroom},1,0,1\n")
                    # else:
                    #     f.write(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},自查,1,0,-1\n")
                    if timetable.day_time:
                        result.append(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},{timetable.classroom},"
                              f"{weekdays[timetable.day_time.weekday]},"
                              + getTime(timetable.day_time.period[0])+','+getFlex(timetable.day_time.period[0], timetable.day_time.period[1])+"\n")
                    elif timetable.whole_week:
                        result.append(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},{timetable.classroom},1,0,1\n")
                    else:
                        result.append(f"{_id_dir[timetable.course.name]},{timetable.course.name},{timetable.course.instructor[:-1]},自查,1,0,-1\n")
    return result


# if __name__ == "__main__":
#     main()
#     print("dealing finish")
