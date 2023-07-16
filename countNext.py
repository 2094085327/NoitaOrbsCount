import readFile


def printMessage(message):
    print(message)


def getNextOrbsNum():
    ngPlusNum = int(readFile.getWorldPlusNum())
    orbsGetNow = readFile.getOrbsNum()

    if ngPlusNum == 0:
        printMessage("现在是初始世界")
    else:
        printMessage(f"现在是第 {ngPlusNum} 个新世界(NG+{ngPlusNum})")

    printMessage(f"当前周目已经获取到 {orbsGetNow} 个魔球")

    if ngPlusNum < 6:
        orbsNeeded = 5 + ngPlusNum - orbsGetNow
        orbsRange = f"{5 + ngPlusNum}-10"
        if orbsGetNow > 10:
            printMessage(
                f"你已经获取到的魔球数已经超出了能够进入下一周目的魔球数，可以进入下一周目的魔球数最大为:{orbsRange}")
        else:
            printMessage(f"进入下一世界还需要获得至少 {orbsNeeded} 个魔球")
    elif ngPlusNum == 6:
        orbsNeeded = 10 - orbsGetNow
        printMessage("能够进入NG+7的魔球数为: 10")
        if orbsGetNow > 10:
            printMessage("你已经获取到的魔球数已经超出了能够进入下一周目的魔球数，可以进入下一周目的魔球数最大为:10")
        else:
            printMessage(f"进入下一世界还需要获得至少 {orbsNeeded} 个魔球")
    elif 6 < ngPlusNum < 28:
        orbsNeeded = 5 + ngPlusNum - orbsGetNow
        orbsRange = f"{5 + ngPlusNum}-32"
        printMessage(f"能够进入NG+{ngPlusNum + 1}的魔球数为:{orbsRange}")
        printMessage(f"进入下一世界还需要获得至少 {orbsNeeded} 个魔球")
    else:
        printMessage("现在已经是NG+28了，总共需要33个魔球")
