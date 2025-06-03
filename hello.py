import sys
from loguru import logger

def main():
    name = "World"
    # 从命令行获取参数
    if len(sys.argv) > 1:
        name = sys.argv[1]
    logger.info(f"Hello, {name}! This is a Python script running.")
    logger.info(f"Python version: {sys.version}")

if __name__ == "__main__":
    main()