# main.py
from module.calculator import Calculator


def demonstrate_calculator():
    num1 = 10
    num2 = 5

    sum_result = Calculator.add(num1, num2)
    print(f"演示开始：")
    print(f"计算 {num1} + {num2} 的结果是: {sum_result}")

    # 你还可以添加更多演示，比如：
    # product_result = Calculator.multiply(num1, num2) # 如果你的计算器有乘法
    # print(f"计算 {num1} * {num2} 的结果是: {product_result}")

    print(f"演示结束！Python 模块在 Docker 容器中成功运行！🎉")


if __name__ == "__main__":
    demonstrate_calculator()
