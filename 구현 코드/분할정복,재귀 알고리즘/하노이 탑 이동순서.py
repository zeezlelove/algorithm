def hanoi(num,A,B,C): #A에 꽃혀있는 num개의 원반을 B를 거쳐 C로 이동한다.
    #이동할 원반이 한개라면?
    if num == 1:
        return
        print("원반 {}을 {}에서 {}로 이동".format(num,A,C))
    else:
        #1.num-1개를 A에서 B로 이동
        hanoi(num-1,A,C,B)
        #2.1개를 A에서 B로 이동
        print("원반 {}을 {}에서 {}로 이동".format(num,A,C))
        #3.num-1개를 B에서 C로 이동
        hanoi(num-1,B,A,C)
hanoi(int(input()),1,2,3) #원반개수,A기둥번호,B기둥번호,C기둥번호
