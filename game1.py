human = int(input('请输入您的等级：'));
angel = int(input('请输入天使的等级：'));
devil = int(input('请输入恶魔的等级：'));

humanlife = human * 100;
angellife = angel * 200;
devillife = devil * 250;

while(humanlife > 0 and devillife > 0):
    print('你砍了恶魔一刀，伤害20生命');
    devillife -= 20;
    print('恶魔砍了你一刀，伤害30生命');
    humanlife -= 30;
while(humanlife <= 0 and devillife > 0):
    print("你被恶魔打败了！是否需要天使？");
    need = int(input("1：需要；2：不需要" +"\n" ));
    if(need == 1):
        while(angellife > 0 and devillife > 0):
            print('天使砍了恶魔一刀，伤害30生命');
            devillife -= 30;
            print('恶魔砍了天使一刀，伤害20生命');
            angellife -= 20;
        if(angellife <= 0 and devillife > 0):
            print('天使也无能为力，恶魔笑到了最后');
            print("游戏结束");
            break;
        elif(angellife > 0 and devillife <= 0):
            print("在天使的帮助下，恶魔被打败了");
            print("游戏结束");
    else:
        print("天使已经远离，你失去了生命");
        print("游戏结束");
        break;
while (humanlife > 0 and devillife <=  0):
    print("恭喜你，你成功把恶魔打败了！");
    print("游戏结束");
    break;
