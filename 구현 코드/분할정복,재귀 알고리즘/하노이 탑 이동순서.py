def hanoi(num,A,B,C): #A에 꽃혀있는 num개의 원반을 B를 거쳐 C로 이동한다.
    #이동할 원반이 한개라면?
    if num == 1:
        print("원반 {}을 {}에서 {}로 이동".format(num,A,C))
    else:
        #마지막 한개를 제외하고 A기둥에서 C기둥를 거쳐 B기둥으로 옮긴다.
        hanoi(num-1,A,C,B)
        #원반 num을 A 기둥에서 C기둥으로 이동
        print("원반 {}을 {}에서 {}로 이동".format(num,A,C))
        #나머지를 B기둥에서 A기둥을 거쳐 C기둥으로 옮긴다.
        hanoi(num-1,B,A,C)
        
hanoi(int(input()),1,2,3) #원반개수,A기둥번호,B기둥번호,C기둥번호
