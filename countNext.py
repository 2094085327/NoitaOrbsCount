import readFile


def getNextOrbsNum():
    ngPlusNum = int(readFile.getWorldPlusNum())
    orbsGetNow = readFile.getOrbsNum()
    if int(ngPlusNum) == 0:
        print("现在是初始世界")
    else:
        print("现在是第 " + str(ngPlusNum) + " 个新世界(NG+" + str(ngPlusNum) + ")")

    print("当前周目已经获取到 " + str(orbsGetNow) + " 个魔球")

    if ngPlusNum < 6:
        print("能够进入NG+" + str(ngPlusNum + 1) + "的魔球数为: " + str(5 + ngPlusNum) + "-10")
        print("进入下一世界还需要获得至少 " + str(5 + ngPlusNum - orbsGetNow) + " 个魔球")
    elif ngPlusNum == 6:
        print("能够进入NG+" + str(ngPlusNum + 1) + "的魔球数为: 10")
        print("进入下一世界还需要获得至少 " + str(10 - orbsGetNow) + " 个魔球")

    elif 6 < ngPlusNum < 28:
        print("能够进入NG+" + str(ngPlusNum + 1) + "的魔球数为:" + str(5 + ngPlusNum) + "-32")
        print("进入下一世界还需要获得至少 " + str(5 + ngPlusNum - orbsGetNow) + " 个魔球")

    else:
        print("现在已经是NG+28了，总共需要33个魔球")
