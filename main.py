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
    target.shape("circle")
    target.speed(0)
    target.penup()
    target.goto(random.randint(0,10)*10, random.randint(0, 10)*10)
    return target


def move_right():
    if user.xcor() >= 100:
        return
    global tryCount
    tryCount += 1
    user.setheading(0)
    user.forward(10)


def move_left():
    if user.xcor() <= 0:
        return
    global tryCount
    tryCount += 1
    user.setheading(180)
    user.forward(10)


def move_up():
    if user.ycor() >= 100:
        return
    global tryCount
    tryCount += 1
    user.setheading(90)
    user.forward(10)


def move_down():
    if user.ycor() <= 0:
        return
    global tryCount
    tryCount += 1
    user.setheading(270)
    user.forward(10)


def getname():
    name = t.textinput("터틀게임", "플레이어 이름을 입력하세요")
    return name


def gameturn():
    global tryCount
    tryCount = 0
    oldcount = -1
    user.goto(0, 0)
    target.color("red")
    target.shape("circle")
    target.speed(0)
    target.penup()
    target.goto(random.randint(0, 10) * 10, random.randint(0, 10) * 10)
    while True:
        user.clear()
        screen.onkeypress(move_right, "Right")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.listen()
        if user.xcor() > 100:
            user.setx(100)
        elif user.xcor() < 0:
            user.setx(0)

        if user.ycor() > 100:
            user.sety(100)
        elif user.ycor() < 0:
            user.sety(0)

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

    while stagecount < 5:
        player = getname()
        score = gameturn()

        scores.append([player, score])
        stagecount += 1

    scores.sort(key=lambda x: x[1])
    print(scores)

