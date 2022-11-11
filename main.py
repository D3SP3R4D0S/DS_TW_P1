# 100x100의 맵이 있고, 맵에서의 움직임은 좌,우,위,아래 (대각석 x)로 움직임이 가능하다.
#
# 처음 임의로 설정된 목표
# 처음 (0,0)에 설정된 터틀을 통해서
# 터틀이 목표에 다가가는 것을 위한 게임이다.
#
# 터틀은 사용자가 직접 입력을 통해 이동하고,
# 목표는 사용자의 움직임에 맞게 최대한 잡히지 않도록 이동한다.
#
# 터틀의 이동은 한번에 3개 좌,우,위,아래를 선택할 수 있고
# 목표의 이동은 한번에 2개 좌,우,위,아래를 통해 나타난다.
#
# 처음 이동은 목표부터 시작
# 다음에 터틀의 이동 순으로 진행한다.
#
# 이를 통해 총 5번의 게임이 이루어졌을 때 시도횟수와 사용자이름을 기록하여 이를 정렬하여 보여주어라.
#
# 제출자료 : 아이디어에 대한 간단한 정리문서(word 혹은 hwp), 프로그램코드
import time
import turtle as t
import random


def init():
    # 스크린 객체 생성
    screen = t.Screen()
    screen.setup(300,300)
    # 스크린 배경색 지정
    screen.bgcolor("white")
    screen.tracer(2)
    return screen


def user():
    # 울타리 그리기
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.pendown()
    turtle.setposition(-100, 100)
    turtle.penup()
    turtle.pensize(2)
    return turtle


def target():
    target = t.Turtle() #목표지점1
    target.color("red")
    target.shape("square")
    target.speed(0)
    target.penup()
    target.goto(random.randint(0,10)*10, random.randint(0, 10)*10)
    return target


def move_right():
    #벽(100)인 경우 count처리않고 return
    if user.xcor() >= 100:
        return
    global tryCount
    tryCount += 1
    user.setheading(0)
    user.forward(10)


def move_left():
    #벽(0)인 경우 count처리않고 return
    if user.xcor() <= 0:
        return
    global tryCount
    tryCount += 1
    user.setheading(180)
    user.forward(10)


def move_up():
    #벽(100)인 경우 count처리않고 return
    if user.ycor() >= 100:
        return
    global tryCount
    tryCount += 1
    user.setheading(90)
    user.forward(10)


def move_down():
    #벽(0)인 경우 count처리않고 return
    if user.ycor() <= 0:
        return
    global tryCount
    tryCount += 1
    user.setheading(270)
    user.forward(10)


def getname():
    name = t.textinput("터틀게임", "플레이어 이름을 입력하세요")
    return name


def targetmove():
    x = target.xcor()
    y = target.ycor()
    # 알고리즘 구성
    # 4분면으로 나눈다 각 0~50 50~100 씩 x y 좌표로 할당
    # 사용자가 각 사분면에 있을때의 행동이 변화한다
    # 사용자가 반대 되는 사분면에 있을경우 벽쪽으로 도망
    # 사용자가 맞은편 사분면에 있을경우 반대편 사분면으로 도망

    x_to_user = x - user.xcor()
    y_to_user = y - user.ycor()
    # x to user + y to user +  동북쪽, case1
    # x to user + y to user -  동남쪽, case2
    # x to user - y to user +  서북쪽, case3
    # x to user - y to user -  서남쪽, case4
    if x == 100:
        if y == 100:
            if x_to_user > y_to_user-30:
                target.setx(x - 10)
            else:
                target.sety(y - 10)
        else:
            # move y or move x -
            if abs(x_to_user) > abs(y_to_user):
                target.setx(x - 10)
            elif y_to_user > 0:
                target.sety(y + 10)
            elif y_to_user < 0:
                target.sety(y - 10)
    elif x == 0:
        if y == 100:
            if x_to_user > y_to_user-30:
                target.setx(x+10)
            else:
                target.sety(y+10)
            # move x or move y -
        else:
            if abs(x_to_user) > abs(y_to_user):
                target.setx(x + 10)
            elif y_to_user > 0:
                target.sety(y + 10)
            elif y_to_user < 0:
                target.sety(y - 10)
    elif y == 100:
        # move x or move y -
        if abs(y_to_user) > abs(x_to_user):
            target.sety(y-10)
        elif x_to_user > 0:
            target.setx(x+10)
        elif x_to_user < 0:
            target.setx(x-10)
        # move y or move x -
    elif y == 0:
        if abs(y_to_user) > abs(x_to_user):
            target.sety(y-10)
        elif x_to_user > 0:
            target.setx(x+10)
        elif x_to_user < 0:
            target.setx(x-10)
        # move y or move x -
    else:
        if x_to_user > 0:
            if y_to_user > 0:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x + 10)
                else:
                    target.sety(y + 10)
            else:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x + 10)
                else:
                    target.sety(y - 10)
        elif x_to_user < 0:
            if y_to_user > 0:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x - 10)
                else:
                    target.sety(y + 10)
            else:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x - 10)
                else:
                    target.sety(y - 10)
        else:
            a = random.randint(1,5)
            if a == 1:
                target.sety(y-10)
            elif a == 2:
                target.sety(y+10)
            elif a == 3:
                target.setx(x-10)
            elif a == 4:
                target.setx(x+10)
    t.clear()
    t.write("PLAYER : " + player +
            "\nSCORE : " + str(tryCount) +
            "\nPOSITION : " + str(user.position()) +
            "\nTARGET : " + str(target.position()))



def gameturn():
    global tryCount
    tryCount = 0
    oldcount = -1
    user.goto(0, 0)
    target.color("red")
    target.speed(0)
    target.penup()
    target.goto(random.randint(0, 10) * 10, random.randint(0, 10) * 10)
    beforemoved = 0
    while True:
        user.clear()
        if tryCount%3 == 0 and beforemoved != tryCount:
            targetmove()
            time.sleep(0.1)
            targetmove()
            beforemoved = tryCount
        screen.onkeypress(move_right, "Right")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.listen()
        #User가 벽을 넘어가지 못 하도록 하는 코드
        if user.xcor() > 100:
            user.setx(100)
        elif user.xcor() < 0:
            user.setx(0)

        if user.ycor() > 100:
            user.sety(100)
        elif user.ycor() < 0:
            user.sety(0)

        #Target이 벽을 넘지 못 하게 하는 코드
        if target.xcor() > 100:
            targetmove()
        elif target.xcor() < 0:
            targetmove()

        if target.ycor() > 100:
            targetmove()
        elif target.ycor() < 0:
            targetmove()

        if oldcount != tryCount:
            t.clear()
            t.write("PLAYER : " + player +
                    "\nSCORE : " + str(tryCount) +
                    "\nPOSITION : " + str(user.position()) +
                    "\nTARGET : " + str(target.position()))

        oldcount = tryCount
        if user.distance(target) < 1:
            user.reset()
            screen.reset()
            target.reset()
            break
    return tryCount


if __name__ == '__main__':
    stagecount = 0
    scores = []
    user = user()
    target = target()
    screen = init()
    while True:
        while stagecount < 5:
            player = getname()
            score = gameturn()

            scores.append([player, score])
            stagecount += 1

        scores.sort(key=lambda x: x[1])
        print(scores)
        t.clear()
        t.write("1st : " + scores[0][0] + " score : " + str(scores[0][1]) +
                "\n2nd : " + scores[1][0] + " score : " + str(scores[1][1]) +
                "\n3rd : " + scores[2][0] + " score : " + str(scores[2][1]) +
                "\n4th : " + scores[3][0] + " score : " + str(scores[3][1]) +
                "\n5th : " + scores[4][0] + " score : " + str(scores[4][1]) +
                "\nplease go to target to restart")
        target.color("red")
        target.speed(0)
        target.penup()
        target.goto(100,100)
        while True:
            user.clear()
            screen.onkeypress(move_right, "Right")
            screen.onkeypress(move_left, "Left")
            screen.onkeypress(move_up, "Up")
            screen.onkeypress(move_down, "Down")
            if user.distance(target) < 1:
                user.reset()
                screen.reset()
                target.reset()
                scores = []
                stagecount = 0
                break

