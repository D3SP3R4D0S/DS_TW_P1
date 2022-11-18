# 10*scalex10*scale의 맵이 있고, 맵에서의 움직임은 좌,우,위,아래 (대각석 x)로 움직임이 가능하다.
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
    screen.setup(20*scale,20*scale)
    # 스크린 배경색 지정
    screen.bgcolor("black")
    screen.tracer(2)
    return screen


def user():
    # 유저 Shape 추가 (상, 하, 좌, 우 각각의 형상 추가)
    t.addshape("images\packman_0.gif")
    t.addshape("images\packman_90.gif")
    t.addshape("images\packman_180.gif")
    t.addshape("images\packman_270.gif")
    # 유저 객체 생성
    turtle = t.Turtle()
    turtle.shape("images\packman_0.gif")
    return turtle


def fence(crossline = True):
<<<<<<< Updated upstream
    # 울타리 그리기
    fence = t.Turtle()
    fence.penup()
    fence.hideturtle()
    fence.setposition(-5.5*scale, -5.5*scale)
    fence.color("blue")
    fence.pendown()
    fence.pensize(4)
    for x in range(4):
        fence.forward(11*scale)
        fence.left(90)
    if crossline:
        fence.color("midnightBlue")
        fence.pensize(1)
        for i in range(10):
            fence.penup()
            fence.goto(-5.5 * scale, (i - 4.5) * scale)
            fence.pendown()
            fence.goto(+5.5 * scale, (i - 4.5) * scale)
            fence.penup()
=======
    fence = t.Turtle() # 펜스 작성 객체를 생성합니다.
    fence.penup() # 객체가 시작점에 위치하지 않으므로 작성을 중지합니다.
    fence.hideturtle() # 벽면을 그릴 객체의 모습을 숨깁니다.
    fence.setposition(-5.5*scale, -5.5*scale) # 내벽의 작성을 위해 객체를 시작점으로 옮깁니다.
    fence.color("blue") # 선의 색상을 blue으로 지정합니다.
    fence.pendown() # 작성을 시작합니다.
    fence.pensize(4) # 선의 두께를 4로 지정합니다.
    for x in range(4): # 해당 반복문은 x = 0 ~ 3까지 총 4회 반복합니다.
        fence.forward(11*scale) # 한쪽 벽면을 작성합니다. 벽의 크기는 지정된 scale*11 픽셀 입니다.
        fence.left(90) # 한쪽벽의 작성이 완료되었으므로 다음벽을 작성하기 위해 방향을 90도 회전합니다. 반복을 통해 사각형 모양의 벽면이 생성됩니다.
    fence.penup() # 작성을 중지합니다.
    fence.setposition(-5.7 * scale, -5.7 * scale) # 외벽을 작성하기 위해 시작점으로 객체를 옮깁니다.
    fence.pendown() # 작성을 시작합니다.
    fence.pensize(2) # 선의 두께를 2로 변경합니다.
    for x in range(4): # 해당 반복문은 x = 0 ~ 3까지 총 4회 반복합니다.
        fence.forward(11.4 * scale) # 한쪽 벽면을 작성합니다. 벽의 크기는 지정된 scale*11.4 픽셀 입니다.
        fence.left(90) # 한쪽벽의 작성이 완료되었으므로 다음벽을 작성하기 위해 방향을 90도 회전합니다. 반복을 통해 사각형 모양의 벽면이 생성됩니다.
    if crossline: # corssline의 상태를 확인합니다. 값을 따로 지정해주지 않을 경우, 초기값은 True 이므로 해당 조건문을 실행합니다.
        fence.color("midnightBlue") # 선의 색상을 midnightBlue로 변경합니다.
        fence.pensize(1) # 선의 두께를 1로 변경합니다.
        for i in range(10): # 해당 반복문은 i = 0 ~ 9까지 총 10회 반복합니다.
            fence.penup() # 객체가 시작점에 위치하지 않으므로 작성을 중지합니다.
            fence.goto(-5.5 * scale, (i - 4.5) * scale) # 객체를 시작점으로 옮깁니다.
            fence.pendown() # 작성을 시작합니다.
            fence.goto(+5.5 * scale, (i - 4.5) * scale) # 객체를 마지막점으로 옮깁니다. 이동경로가 작성되고 있는 상태이므로 -5.5*scale ~ +5.5*scale 픽셀의 가로선이 작성됩니다.
            fence.penup() # 작성을 중지합니다.
>>>>>>> Stashed changes

        for i in range(10): # 해당 반복문은 i = 0 ~ 9까지 총 10회 반복합니다.
            fence.penup() # 객체가 시작점에 위치하지 않으므로 작성을 중지합니다.
            fence.goto((i - 4.5) * scale, -5.5 * scale) # 객체를 시작점으로 옮깁니다.
            fence.pendown() # 작성을 시작합니다.
            fence.goto((i - 4.5) * scale, +5.5 * scale) # 객체를 마지막점으로 옮깁니다. 이동경로가 작성되고 있는 상태이므로 -5.5*scale ~ +5.5*scale 픽셀의 세로선이 작성됩니다.
            fence.penup() # 작성을 중지합니다.


def texttuetle():
    texttuetle = t.Turtle()
    texttuetle.penup()
    texttuetle.hideturtle()
    return texttuetle


def target():
    # 타겟 Shape 추가
    t.addshape("images\ghost.gif")
    # 타겟 객체 생성
    target = t.Turtle()
    target.shape("images\ghost.gif")
    target.penup()
    return target


def move_right():
    if user.xcor() >= 5*scale:
        user.setx(5*scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(0)
    user.shape("images\packman_0.gif")
    user.forward(1*scale)


def move_left():
    if user.xcor() <= -5*scale:
        user.setx(-5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(180)
    user.shape("images\packman_180.gif")
    user.forward(1*scale)


def move_up():
    if user.ycor() >= 5*scale:
        user.sety(5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(90)
    user.shape("images\packman_90.gif")
    user.forward(1*scale)


def move_down():
    if user.ycor() <= -5*scale:
        user.sety(-5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(270)
    user.shape("images\packman_270.gif")
    user.forward(1*scale)


def getname():
    name = t.textinput("터틀게임", "플레이어 이름을 입력하세요")
    return name


def showscore():
    texttuetle.clear()
    texttuetle.penup()
    texttuetle.hideturtle()
    texttuetle.setposition(-6 * scale, 6 * scale)
    texttuetle.color("white")
    texttuetle.write("SCORE : " + str(tryCount), align="left", font=("Unispace", 15, "normal"))
    texttuetle.setposition(0, 6 * scale)
    texttuetle.write("PLAYER : " + player, align="center", font=("Unispace", 15, "normal"))
    texttuetle.setposition(6 * scale, 6 * scale)
    texttuetle.write("STAGE : " + str(stagecount), align="right", font=("Unispace", 15, "normal"))


def targetmove():
    x = target.xcor()
    y = target.ycor()
    # 알고리즘 구성
    # 4분면으로 나눈다 각 0~50 50~scale 씩 x y 좌표로 할당
    # 사용자가 각 사분면에 있을때의 행동이 변화한다
    # 사용자가 반대 되는 사분면에 있을경우 벽쪽으로 도망
    # 사용자가 맞은편 사분면에 있을경우 반대편 사분면으로 도망
    x_to_user = x - user.xcor() # 사용자와 x 축으로 떨어진 거리 값
    y_to_user = y - user.ycor() # 사용자와 y 축으로 떨어진 거리 값

    if x >= 5*scale: # 타겟의 x 값이 5scale을 넘을 경우
        if y >= 5*scale: # 타겟이 x y 가 모두 5scale인경우
            if abs(x_to_user) > abs(y_to_user):
                target.sety(y - scale) # x 로 떨어진 거리가 더 클경우 y 값을 감소시킨다
            else:
                target.setx(x - scale) # y 로 떨어진 거리가 더 클경우 x 값을 감소시킨다
        elif y <= -5*scale: # x > scale y  < 0
            if abs(x_to_user) > abs(y_to_user):
                target.sety(y + scale) # x 떨어진 거리가 더클경우 y 값을 감소시킨다
            else:
                 target.setx(x - scale) # y 로 떨어진 거리가 더 클경우 x 값을 증가시킨다 ( y 가 max 값임)
        else: # x 축 선상 ( 5scale ) 에 있을 경우
            # move y or move x -
            if abs(x_to_user) > abs(y_to_user): # x로 떨어진 값이 더 클경우 x 를 감소시킨다
                target.setx(x - scale)
            elif y_to_user > 0: # y 로 사용자와 양수값 ( 사용자보다 위에 있음)
                target.sety(y + scale) # y 의 양의 방향으로 도망간다
            elif y_to_user < 0: # 음수값일경우 (사용자보다 아래에 있음
                target.sety(y - scale) # y 의 음의 방향으로 도망간다
            else: # y의 축이 사용자와 같을경우
                if y > 0:
                    target.sety(y + scale)
                elif y < 0:
                    target.sety(y - scale)
    elif x <= -5*scale:
        if y >= 5*scale: # 타겟이 x 가 -5 , y 가 +5 인경우
            if abs(x_to_user) > abs(y_to_user):
                target.sety(y - scale)
            else:
                target.setx(x + scale)
            # move x or move y -
        elif y <= -5*scale: # 타겟이 x y 가 모두 -5 인경우
            if abs(x_to_user) > abs(y_to_user):
                target.sety(y + scale)
            else:
                target.setx(x + scale)
        else: # x 축 선상 ( -5scale ) 에 있을 경우
            if abs(x_to_user) > abs(y_to_user):
                target.sety(y + scale)
            elif y_to_user > 0:  # y 로 사용자와 양수값 ( 사용자보다 위에 있음)
                target.sety(y + scale)  # y 의 양의 방향으로 도망간다
            elif y_to_user < 0:  # 음수값일경우 (사용자보다 아래에 있음
                target.sety(y - scale)  # y 의 음의 방향으로 도망간다
            else: # y의 축이 사용자와 같을경우 빈공간이 많은 쪽으로 이동한다
                if y > 0:
                    target.sety(y - scale) # y 값이 양수일경우 아래쪽이 비어있어 아래로 이동
                elif y < 0:
                    target.sety(y + scale) # y값이 음수일경우 위쪽이 비어있어 위로 이동
    elif y >= 5*scale:# y 축 선상 ( 5scale ) 에 있을 경우
        # move x or move y -
        if abs(y_to_user) > abs(x_to_user):
            target.sety(y-scale)  # y로 떨어진 거리가 많으면 y 값을 줄여본다
        elif x_to_user > 0:
            target.setx(x+scale) # x 와 가까우면 x 축을 이동한다
        else:
            target.setx(x-scale) # x 와 음수로 떨어졌을경우 x 와 멀어진다
        # move y or move x -
    elif y <= -5*scale:# y 축 선상 ( -5scale ) 에 있을 경우
        if abs(y_to_user) > abs(x_to_user):
            target.sety(y + scale) # y로 떨어진 거리가 많으면 y 값을 늘려본다
        elif x_to_user > 0:
            target.setx(x+scale) # x 와 가까우면 x 축을 이동한다
        else:
            target.setx(x-scale) #x 와 음수로 떨어졌을경우 x 와 멀어진다
        # move y or move x -
    else:
        if x_to_user > 0:
            if y_to_user > 0:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x + scale)
                else:
                    target.sety(y + scale)
            else:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x + scale)
                else:
                    target.sety(y - scale)
        elif x_to_user < 0:
            if y_to_user > 0:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x - scale)
                else:
                    target.sety(y + scale)
            else:
                if abs(y_to_user) > abs(x_to_user):
                    target.setx(x - scale)
                else:
                    target.sety(y - scale)
        else:
            a = random.randint(1,5)
            if a == 1:
                target.sety(y-scale)
            elif a == 2:
                target.sety(y+scale)
            elif a == 3:
                target.setx(x-scale)
            elif a == 4:
                target.setx(x+scale)
    showscore()


def gameturn():
    global tryCount
    tryCount = 100
    oldcount = 101
    fence()
    # scoreBoard()
    user.penup()
    user.goto(-5*scale, -5*scale)
    # user.color("yellow")
    user.turtlesize(scale/20)
    # target.color("pink")
    target.speed(0)
    target.penup()
    target.goto(random.randint(-5, 5)*scale, random.randint(-5,5)*scale)
    target.turtlesize(scale/20)
    beforemoved = 101
    while True:
        user.clear()
        if (tryCount+2)%3 == 0 and beforemoved != tryCount:
            targetmove()
            time.sleep(0.1)
            targetmove()
            beforemoved = tryCount
        screen.onkeypress(move_right, "Right")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
        screen.listen()
        if user.xcor() > 5*scale:
            user.setx(5*scale)
        elif user.xcor() < -5*scale:
            user.setx(-5*scale)

        if user.ycor() > 5*scale:
            user.sety(5*scale)
        elif user.ycor() < -5*scale:
            user.sety(-5*scale)

        if oldcount != tryCount:
            showscore()
            oldcount = tryCount
        if user.distance(target) < 1 or tryCount == 0:
            user.reset()
            screen.reset()
            target.reset()
            break
    return tryCount


def gamesummary(scores):
    scores.sort(key=lambda x: x[1], reverse = True)
    print(scores)
    fence(False)
    texttuetle.clear()
    texttuetle.penup()
    texttuetle.hideturtle()
    texttuetle.color("white")
    # t.write("1st : " + scores[0][0] + " score : " + str(scores[0][1]), align="center", font=("Unispace", 15, "normal")) # 디버깅을 위해 하나만 표시
    texttuetle.setposition(-3*scale, -1.5 * scale)
    texttuetle.color("white")
    texttuetle.write("1ST : " + scores[0][0]   +
                     "\n2ND : " + scores[1][0] +
                     "\n3RD : " + scores[2][0] +
                     "\n4TH : " + scores[3][0] +
                     "\n5TH : " + scores[4][0]
                     , align="left", font=("Unispace", 15, "normal"))
    texttuetle.setposition(3*scale, -1.5 * scale)
    texttuetle.write( "SCORE : " + str(scores[0][1]) +
                     "\nSCORE : " + str(scores[1][1]) +
                     "\nSCORE : " + str(scores[2][1]) +
                     "\nSCORE : " + str(scores[3][1]) +
                     "\nSCORE : " + str(scores[4][1])
                      , align="right", font=("Unispace", 15, "normal"))
    texttuetle.color("black")
    texttuetle.setposition(0, -7 * scale)
    texttuetle.color("white")
    texttuetle.write("please go to target to restart", align="center", font=("Unispace", 15, "normal"))
    target.color("DarkOliveGreen1")
    target.turtlesize(scale / 20)
    target.speed(0)
    target.penup()
    target.goto(4 * scale, 4 * scale)
    user.turtlesize(scale / 20)
    user.goto(-4 * scale, -4 * scale)
    user.color("yellow")
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
            break


if __name__ == '__main__':
    stagecount = 0
    scale = 40
    scores = []
    user = user()
    target = target()
    screen = init()
    texttuetle = texttuetle()
    while True:
        while stagecount < 5:
            player = getname().upper()
            score = gameturn()
            scores.append([player, score])
            stagecount += 1
        gamesummary(scores)
        scores = []
        stagecount = 0