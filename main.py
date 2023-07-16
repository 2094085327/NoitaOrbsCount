import countNext

if __name__ == '__main__':
    while True:
        command = input("输入read进行读取:")
        if command == "read":
            countNext.getNextOrbsNum()
        else:
            print("无效指令")
