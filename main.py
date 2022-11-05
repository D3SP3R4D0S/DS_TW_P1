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
    screen.setup(100,100)
    # 스크린 배경색 지정
    screen.bgcolor("white")
    screen.tracer(2)
    return screen


def mypen():
    # 울타리 그리기
    mypen = t.Turtle()
    mypen.penup()
    mypen.setposition(-100, 100)
    mypen.pendown()
    mypen.pensize(3)
    return mypen


def target():
    target = t.Turtle() #목표지점1
    target.color("red")
    target.shape("circle")
    target.speed(0)
    target.penup()
    target.goto(random.randint(-100,100), random.randint(-100, 100))
    return target


def turn_right():
    global tryCount
    tryCount = tryCount + 1
    mypen.right(10)


def turn_left():
    global tryCount
    tryCount = tryCount + 1
    mypen.left(10)


def turn_down():
    global tryCount
    tryCount = tryCount + 1
    mypen.backward(10)


def turn_up():
    global tryCount
    tryCount = tryCount + 1
    mypen.forward(10)


def getname():
    name = t.textinput("터틀게임", "플레이어 이름을 입력하세요")
    return name



if __name__ == '__main__':
    plater = getname()
    screen = init()
    mypen = mypen()
    target = target()
    tryCount = 0
    mypen.goto(0, 0)
    target.forward(2)
    while True:
        mypen.clear()
        screen.onkeypress(turn_right, "Right")
        screen.onkeypress(turn_left, "Left")
        screen.onkeypress(turn_up, "Up")
        screen.onkeypress(turn_down, "Down")
        screen.listen()
