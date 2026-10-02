"""对 src/calculator.py 的黑盒测试用例。

用例设计方法：
- 等价类划分：把输入分成有效等价类（0-100 数字）和无效等价类（负数、超过100、非数字）
- 边界值分析：在每个等价类边界附近取值（-1, 0, 59, 60, 80, 89, 90, 100, 101）
"""
import pytest

from src.calculator import get_grade, divide


class TestGetGrade:
    # ---------- 有效等价类：分数段边界值测试 ----------

    @pytest.mark.parametrize("score, expected", [
        (90, "A"),   # A 段下界
        (95, "A"),   # A 段中间
        (100, "A"),  # A 段上界
        (80, "B"),   # B 段下界
        (89, "B"),   # B 段上界
        (60, "C"),   # C 段下界
        (79, "C"),   # C 段上界
        (0, "F"),    # F 段下界
        (59, "F"),   # F 段上界
    ])
    def test_valid_scores(self, score, expected):
        assert get_grade(score) == expected

    # ---------- 无效等价类：越界 ----------

    def test_negative_score_raises(self):
        with pytest.raises(ValueError):
            get_grade(-1)

    def test_over_100_raises(self):
        with pytest.raises(ValueError):
            get_grade(101)

    # ---------- 无效等价类：类型错误 ----------

    @pytest.mark.parametrize("bad_input", ["abc", None, [], {}])
    def test_non_number_raises_type(self, bad_input):
        with pytest.raises(TypeError):
            get_grade(bad_input)


class TestDivide:
    def test_normal_division(self):
        assert divide(10, 2) == 5

    def test_division_negative(self):
        assert divide(-9, 3) == -3

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)
