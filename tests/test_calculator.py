from module.calculator import Calculator
import math


# 测试add函数
class TestCalculator:
    def test_add(self):
        # 验证整数
        assert Calculator.add(1, 2) == 3
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0

        # 验证浮点数
        assert math.isclose(Calculator.add(1.5, 2.5), 4.0, rel_tol=1e-9)
