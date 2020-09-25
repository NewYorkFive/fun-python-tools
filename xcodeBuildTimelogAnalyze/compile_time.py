#!/usr/bin/python
import json
import re
from typing import Set


def filter_log(log_file_path: str, dont_check_libs: Set, time_limits: float, types: Set):
    """
    过滤spotify/XCLogParser日志，将日志中超过time_limits，编译类型在types里的，不在dont_check_libs里的编译时间
    :param log_file_path: 日志文件路径
    :param dont_check_libs: 不检查的pod库
    :param time_limits: 时间限制
    :param types: 需要检查的编译类型，不过滤编译类型传空
    """

    # 截取pod引用库的库名称,使用lib这个group获取
    pattern = ".*\/Pods\/(?P<lib>[0-9a-zA-Z.-]+)\/.*"
    with open(log_file_path, 'r') as fr:
        data = json.load(fr)
        data2 = list()
        for item in data:
            # 超过timelimits且编译类型在types中
            if item["compilationDuration"] > time_limits and item["detailStepType"] in types:
                match = re.match(pattern, item["documentURL"])
                if match:
                    lib = match["lib"]
                    # 过滤不检查的库
                    if len(lib) > 0 and lib not in dont_check_libs:
                        data2.append(item)
                else:
                    data2.append(item)
        # 耗时排序，逆序
        data2.sort(key=lambda x: x["compilationDuration"], reverse=True)
        with open('data.json', 'w') as fw:
            json.dump(data2, fw, indent=4)


# cCompilation
compile_type = {"swiftCompilation"}
file_path = "sudoku.json"
dont_check_libs = {"SwiftSoup", "RxSwift", "YYCache", "libwebp", "YYText", "SwifterSwift", "RxCocoa", "HandyJSON",
                        "SnapKit", "Starscream", "SNS", "Socket.IO-Client-Swift"}

filter_log(file_path, dont_check_libs, 0.2, compile_type)
