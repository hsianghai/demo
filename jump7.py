for jump in range(0,100):
    jump+=1;
    if(jump % 7 == 0):
        print("我是7的倍数");
        continue;
    if (jump // 10 == 7):
        print("我是取整7");
        continue;
    if (jump % 10 == 7):
        print("我是余数7");
        continue;
    print(jump);