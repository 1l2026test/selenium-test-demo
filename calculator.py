"""被测函数：一个简单的成绩等级计算器，用于演示黑盒测试。

输入：score 分数（0-100 的数字）
输出：A(90-100) / B(80-89) / C(60-79) / F(<60)
异常：分数越界或类型错误时抛出对应异常
"""


def get_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("分数必须是数字")
    if score < 0 or score > 100:
        raise ValueError("分数必须在 0 到 100 之间")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "F"


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a / b
