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
import math
import time
import turtle as t
import random

def init():
    screen = t.Screen() # 스크린의 객체를 생성합니다.
    screen.setup(20*scale,20*scale) # 화면의 크기는 지정된 scale의 20배수 픽셀, 정사각형 형태로 설정합니다.
    screen.bgcolor("black") # 배경의 색상은 black으로 설정합니다.
    screen.tracer(2) # 즉각적인 실행(빠른 반응속도)를 위해 tracer를 2로 설정합니다.
    return screen


def user():
    # 유저 Shape 추가 (상, 하, 좌, 우, 입닫음(팩맨) 각각의 형상 추가)
    t.addshape("images\circle.gif")
    t.addshape("images\packman_0.gif")
    t.addshape("images\packman_90.gif")
    t.addshape("images\packman_180.gif")
    t.addshape("images\packman_270.gif")
    turtle = t.Turtle() # 유저의 객체를 생성합니다.
    turtle.shape("images\packman_0.gif") # 시작위치에서의 모양은 0도 모양으로 지정합니다.
    return turtle


def fence(crossline = True):
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
    if crossline: # corssline 변수의 상태를 확인합니다. 값을 따로 지정해주지 않을 경우, 초기값은 True 이므로 해당 조건문을 실행하여 게임판 내 격자무늬를 생성합니다.
        fence.color("midnightBlue") # 선의 색상을 midnightBlue로 변경합니다.
        fence.pensize(1) # 선의 두께를 1로 변경합니다.
        for i in range(10): # 해당 반복문은 i = 0 ~ 9까지 총 10회 반복합니다.
            fence.penup() # 객체가 시작점에 위치하지 않으므로 작성을 중지합니다.
            fence.goto(-5.5 * scale, (i - 4.5) * scale) # 객체를 시작점으로 옮깁니다. 객체의 x좌표는 고정되있고, y좌표는 10회의 반복동안 -4.5*scale ~ 4.5*scale 로 scale만큼 변경됩니다.
            fence.pendown() # 작성을 시작합니다.
            fence.goto(+5.5 * scale, (i - 4.5) * scale) # 객체를 마지막점으로 옮깁니다. 이동경로가 작성되고 있는 상태이므로 -5.5*scale ~ +5.5*scale의 가로선이 작성됩니다.
            fence.penup() # 작성을 중지합니다.

        for i in range(10): # 해당 반복문은 i = 0 ~ 9까지 총 10회 반복합니다.
            fence.penup() # 객체가 시작점에 위치하지 않으므로 작성을 중지합니다.
            fence.goto((i - 4.5) * scale, -5.5 * scale) # 객체를 시작점으로 옮깁니다. 객체의 y좌표는 고정되있고, x좌표는 10회의 반복동안 -4.5*scale ~ 4.5*scale 로 scale만큼 변경됩니다.
            fence.pendown() # 작성을 시작합니다.
            fence.goto((i - 4.5) * scale, +5.5 * scale) # 객체를 마지막점으로 옮깁니다. 이동경로가 작성되고 있는 상태이므로 -5.5*scale ~ +5.5*scale 픽셀의 세로선이 작성됩니다.
            fence.penup() # 작성을 중지합니다.


def texttuetle():
    texttuetle = t.Turtle() # 텍스트 작성 객체를 생성합니다.
    texttuetle.penup() # 객체의 이동경로는 표시하지 않습니다.
    texttuetle.hideturtle() # 객체의 모양을 지정하지 않습니다.
    return texttuetle


def target():
    # 타겟 Shape 추가
    t.addshape("images\ghost.gif")
    target = t.Turtle() # 타겟의 객체를 생성합니다.
    target.shape("images\ghost.gif") # 타겟의 모양을 추가한 Spape로 지정합니다.
    target.penup() # 타겟의 이동경로는 작성하지 않습니다.
    return target


def move_right():
    if user.xcor() >= 5*scale: # 유저의 x좌표 위치가 5*scale 이상일 경우,
        user.setx(5*scale) # x좌표 위치를 5*scale로 고정하고
        return # 시도횟수를 감소시키지 않으며 x좌표를 이동시키지 않고 함수를 종료합니다.
    global tryCount # trycount 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    tryCount -= 1 # 시도횟수를 1 감소시킵니다.
    user.setheading(0) # 유저의 이동방향을 0도 위치로 지정합니다.
    user.shape("images\packman_0.gif") # 유저의 모양을 0도 모양으로 지정합니다.
    global beforemove # beforemove 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    beforemove = 0 # beforemove의 값을 0으로 변경합니다. beforemove는 유저(팩맨)의 상태변경(입 열고닫음)에 사용됩니다.
    user.forward(1*scale) # 지정된 이동방향으로 scale 만큼 전진합니다.


def move_left():
    if user.xcor() <= -5*scale: # 유저의 x좌표 위치가 -5*scale 이하일 경우,
        user.setx(-5 * scale) # x좌표 위치를 -5*scale로 고정하고
        return # 시도횟수를 감소시키지 않으며 x좌표를 이동시키지 않고 함수를 종료합니다.
    global tryCount # trycount 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    tryCount -= 1 # 시도횟수를 1 감소시킵니다.
    user.setheading(180) # 유저의 이동방향을 180도 위치로 지정합니다.
    user.shape("images\packman_180.gif") # 유저의 모양을 180도 모양으로 지정합니다.
    global beforemove # beforemove 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    beforemove = 180 # beforemove의 값을 180으로 변경합니다. beforemove는 유저(팩맨)의 상태변경(입 열고닫음)에 사용됩니다.
    user.forward(1*scale) # 지정된 이동방향으로 scale 만큼 전진합니다.


def move_up():
    if user.ycor() >= 5*scale: # 유저의 y좌표 위치가 5*scale 이상일 경우,
        user.sety(5 * scale) # y좌표 위치를 5*scale로 고정하고
        return  # 시도횟수를 감소시키지 않으며 y좌표를 이동시키지 않고 함수를 종료합니다.
    global tryCount # trycount 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    tryCount -= 1 # 시도횟수를 1 감소시킵니다.
    user.setheading(90) # 유저의 이동방향을 90도 위치로 지정합니다.
    user.shape("images\packman_90.gif") # 유저의 모양을 90도 모양으로 지정합니다.
    global beforemove # beforemove 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    beforemove = 90 # beforemove의 값을 90으로 변경합니다. beforemove는 유저(팩맨)의 상태변경(입 열고닫음)에 사용됩니다.
    user.forward(1*scale) # 지정된 이동방향으로 scale 만큼 전진합니다.


def move_down():
    if user.ycor() <= -5*scale: # 유저의 y좌표 위치가 -5*scale 이하일 경우,
        user.sety(-5 * scale) # y좌표 위치를 -5*scale로 고정하고
        return  # 시도횟수를 감소시키지 않으며 y좌표를 이동시키지 않고 함수를 종료합니다.
    global tryCount # trycount 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    tryCount -= 1 # 시도횟수를 1 감소시킵니다.
    user.setheading(270) # 유저의 이동방향을 270도 위치로 지정합니다.
    user.shape("images\packman_270.gif") # 유저의 모양을 270도 모양으로 지정합니다.
    global beforemove # beforemove 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    beforemove = 270 # beforemove의 값을 270으로 변경합니다. beforemove는 유저(팩맨)의 상태변경(입 열고닫음)에 사용됩니다.
    user.forward(1*scale) # 지정된 이동방향으로 scale 만큼 전진합니다.


def getname():
    name = t.textinput("터틀게임", "플레이어 이름을 입력하세요") # 유저의 이름을 입력 받습니다.
    return name # 입력받은 이름을 return 합니다.


def showscore():
    texttuetle.clear() # 기존 작성되어 있는 내용을 초기화 합니다.
    texttuetle.penup() # 객체가 이동하는 경로를 작성하지 않습니다.
    texttuetle.hideturtle() # 객체의 모양을 지정하지 않습니다.
    texttuetle.setposition(-6 * scale, 6 * scale) # 텍스트 작성 객체를 x : -6*scale, y : 6*scale 위치로 이동 시킵니다. 해당 함수에선 게임을 진행하는 울타리 좌측상단에 위치합니다.
    texttuetle.color("white") # 텍스트의 색상을 white로 지정합니다.
    texttuetle.write("SCORE : " + str(tryCount), align="left", font=("Unispace", 15, "normal")) # 점수를 보여줍니다. 
    texttuetle.setposition(0, 6 * scale) # 텍스트 작성 객체를 x : 0, y : 6*scale 위치로 이동 시킵니다. 해당 함수에선 게임을 진행하는 울타리 중앙상단에 위치합니다.
    texttuetle.write("PLAYER : " + player, align="center", font=("Unispace", 15, "normal")) # 입력받은 이름을 보여줍니다.
    texttuetle.setposition(6 * scale, 6 * scale) # 텍스트 작성 객체를 x : 6*scale, y : 6*scale 위치로 이동 시킵니다. 해당 함수에선 게임을 진행하는 울타리 우측상단에 위치합니다.
    texttuetle.write("STAGE : " + str(stagecount), align="right", font=("Unispace", 15, "normal")) # 5번의 게임 중, 현재 몇번째 게임을 진행중인지 보여줍니다.


def targetmove():
    x = target.xcor() # 현재 타겟의 x좌표를 확인합니다.
    y = target.ycor() # 현재 타겟의 y좌표를 확인합니다.
    # 이동할 x, 이동할 y 좌표, 벽까지의 거리 를 기본으로 넣는다.
    up = [x + scale, y, abs(5*scale - (x + scale))]
    down = [x - scale, y, abs(-5*scale - (x - scale))]
    right = [x, y + scale, abs(5*scale - (y + scale))]
    left = [x, y - scale, abs(-5*scale - (y - scale))]
    allcase = [up, down, right, left]
    print(allcase)
    possablecase = []
    for case in allcase:
        casetouserx = abs(case[0]-user.xcor())
        casetousery = abs(case[1]-user.ycor())
        if abs(case[0]) <= 5*scale and abs(case[1]) <= 5*scale:
            casetouser = math.sqrt(casetouserx**2 + casetousery**2)
            case.append(casetouser)
            possablecase.append(case)
    possablecase.sort(key=lambda x: x[3], reverse = True)
    print(possablecase)
    bestcases = []
    for case in possablecase:
        if case[3] == possablecase[0][3]:
            case[0]
            bestcases.append(case)
    print(bestcases)
    bestcases.sort(key=lambda x: x[2], reverse = True)
    bestcase = bestcases[0]
    print(bestcase)
    time.sleep(0.1)
    target.setposition(bestcase[0], bestcase[1])


def gameturn():
    global tryCount # trycount 변수의 값을 변경하기 위해 전역변수로 선언합니다.
    tryCount = 100 # trycount의 값을 100으로 선언합니다. trycount는 유저가 이동할 때 마다 1씩 감소합니다.
    oldcount = 101 # oldecount의 초기값을 선언합니다. oldcount는 trycount와 비교하여 유저가 이동할 때 마다 점수를 변경하여 보여주기 위해 사용됩니다. 
    fence() # 게임화면에 울타리를 그립니다.
    user.penup() # 유저의 이동경로는 표시하지 않습니다.
    user.goto(-5*scale, -5*scale) # 유저를 초기 시작위치인 게임판 좌측하단으로 이동합니다.
    user.turtlesize(scale/20) # 유저의 크기는 지정된 scale/20 크기로 지정합니다.
    target.speed(0) # 타겟이 이동하지 않습니다.
    target.penup() # 타겟의 이동경로를 표시하지 않습니다.
    target.goto(random.randint(-5, 5)*scale, random.randint(-5,5)*scale) # 타겟을 초기 시작위치로 이동 시킵니다. 타겟의 초기 시작 위치는 게임판 내에서 랜덤하게 지정됩니다.
    target.turtlesize(scale/20) # 타겟의 크기는 지정된 scale/20 크기로 지정합니다.
    beforemoved = 100 # beforemoved의 초기값을 선언합니다. beforemoved는 trycount와 비교하여 유저가 이동한 횟수를 비교하여 타겟을 움직이기 위해 사용됩니다.
    changedtime = time.time() # changetime의 초기값을 현재 시간으로 설정합니다. 유저의 상태가 변경된 시간을 확인하기 위해 사용됩니다.
    userstat = 1 # userstat의 초기값을 선언합니다. user() 함수로 초기선언된 모양(0도, 입벌림) 상태를 1로 지정합니다.
    while True:
        user.clear()
        if abs(changedtime - time.time()) > 0.3 and userstat == 1: # 유저가 입벌림 상태이고 상태가 변경된 지 0.3초 지났을 경우,
            user.shape("images\circle.gif") # 유저를 입닫음 상태로 변경합니다.
            changedtime = time.time() # 유저의 상태변경이 끝남을 선언합니다.
            userstat = 0 # 유저가 입닫음 상태임을 확인합니다.
        if abs(changedtime - time.time()) > 0.3 and userstat == 0: # 유저가 입닫음 상태이고 상태가 변경된 지 0.3초가 지났을 경우,
            # 유저를 입벌림 상태로 변경합니다. 현재 유저가 어느방향을 보고 있는 지에 따라 해당방향의 모양으로 변경합니다.
            if beforemove == 0:
                user.shape("images\packman_0.gif")
            elif beforemove == 90:
                user.shape("images\packman_90.gif")
            elif beforemove == 180:
                user.shape("images\packman_180.gif")
            elif beforemove == 270:
                user.shape("images\packman_270.gif")
            changedtime = time.time() # 유저의 상태변경이 끝남을 선언합니다.
            userstat = 1 # 유저가 입벌림 상태임을 확인합니다.
        if user.distance(target) < 1 or tryCount == 0: # 유저가 타겟에 도달하거나, 주어진 시도횟수(100회)를 모두 소진 했을 경우
            user.reset() # 유저를 초기화 하고
            screen.reset() # 스크린을 초기화 하고
            target.reset() # 타겟을 초기화 하고
            break # 반복문을 벗어나 함수를 종료합니다.
        if (tryCount+2)%3 == 0 and beforemoved != tryCount: # 유저가 세번째 이동을 했을경우,
            targetmove()
            targetmove() # 타겟을 2회 움직입니다.
            beforemoved = tryCount # 유저의 이동이 끝남을 선언합니다.
        screen.listen() # 이벤트를 확인합니다.
        screen.onkeypress(move_right, "Right") # 키보드 우이동키 입력 이벤트를 받았을 때, move_right()을 수행합니다.
        screen.onkeypress(move_left, "Left") # 키보드 좌이동키 입력 이벤트를 받았을 때, move_left()를 수행합니다.
        screen.onkeypress(move_up, "Up") # 키보드 상이동키 입력 이벤트를 받았을 때, move_up()을 수행합니다.
        screen.onkeypress(move_down, "Down") # 키보드 하이동키 입력 이벤트를 받았을 때, move_down()을 수행합니다.
        if user.xcor() > 5*scale: # 유저의 x좌표가 주어진 게임판 우측(5*scale)을 벗어날 경우,
            user.setx(5*scale) # 유저의 x좌표가 게임판 밖으로 벗어나지 못하게 합니다.
        elif user.xcor() < -5*scale: # 유저의 x좌표가 주어진 게임판 좌측(5*scale)을 벗어날 경우,
            user.setx(-5*scale) # 유저의 x좌표가 게임판 밖으로 벗어나지 못하게 합니다.
        if user.ycor() > 5*scale: # 유저의 y좌표가 주어진 게임판 상단(5*scale)을 벗어날 경우,
            user.sety(5*scale) # 유저의 y좌표가 게임판 밖으로 벗어나지 못하게 합니다.
        elif user.ycor() < -5*scale: # 유저의 y좌표가 주어진 게임판 하단(5*scale)을 벗어날 경우,
            user.sety(-5*scale) # 유저의 y좌표가 게임판 밖으로 벗어나지 못하게 합니다.
        if oldcount != tryCount: # 유저가 이동하여 시도횟수가 변경 될때,
            showscore() # 변경된 점수를 갱신합니다.
            oldcount = tryCount # 유저의 이동이 끝남을 선언합니다.
        if user.distance(target) < 1 or tryCount == 0: # 유저가 타겟에 도달하거나, 주어진 시도횟수(100회)를 모두 소진 했을 경우
            user.reset() # 유저를 초기화 하고
            screen.reset() # 스크린을 초기화 하고
            target.reset() # 타겟을 초기화 하고
            break # 반복문을 벗어나 함수를 종료합니다.
    return tryCount # 반복문을 벗어났을 때 최종적으로 변경된 시도횟수를 리턴합니다.


def gamesummary(scores):
    scores.sort(key=lambda x: x[1], reverse = True) # 다섯번의 게임동안 저장된 점수의 배열을 받아 점수순으로 정렬합니다.
    # print(scores)
    fence(False) # fence() 함수에 Flase 값을 보냅니다. 
    texttuetle.clear() # 기존 작성되어 있는 내용을 초기화 합니다.
    texttuetle.penup() # 텍스트 작성 객체의 이동경로를 표시하지 않습니다.
    texttuetle.hideturtle() # 객체의 모양을 지정하지 않습니다.
    texttuetle.color("white") # 텍스트의 색상을 white로 지정합니다.
    # t.write("1st : " + scores[0][0] + " score : " + str(scores[0][1]), align="center", font=("Unispace", 15, "normal")) # 디버깅을 위해 하나만 표시
    texttuetle.setposition(-3*scale, -1.5 * scale) # 객체를 x : -3*scale, y : -1.5 * scale 위치로 이동시킵니다. 해당 함수에선 게임판 중앙좌측에 위치합니다.
    texttuetle.write("1ST : " + scores[0][0]   +
                     "\n2ND : " + scores[1][0] +
                     "\n3RD : " + scores[2][0] +
                     "\n4TH : " + scores[3][0] +
                     "\n5TH : " + scores[4][0]
                     , align="left", font=("Unispace", 15, "normal")) # 배열에 저장된 유저이름을 보여줍니다.
    texttuetle.setposition(3*scale, -1.5 * scale) # 객체를 x : 3*scale, y : -1.5 * scale 위치로 이동시킵니다. 해당 함수에선 게임판 중앙우측에 위치합니다.
    texttuetle.write( "SCORE : " + str(scores[0][1]) +
                     "\nSCORE : " + str(scores[1][1]) +
                     "\nSCORE : " + str(scores[2][1]) +
                     "\nSCORE : " + str(scores[3][1]) +
                     "\nSCORE : " + str(scores[4][1])
                      , align="right", font=("Unispace", 15, "normal")) # 배열에 저장된 점수를 보여줍니다.
    texttuetle.setposition(0, -7 * scale) # 객체를 x : 0, y : -7 * scale 위치로 이동시킵니다. 해당 함수에선 게임을 진행하는 울타리 중앙하단에 위치합니다.
    texttuetle.write("please go to target to restart", align="center", font=("Unispace", 15, "normal")) # 게임 재시작 방법 안내문구를 보여줍니다.
    #target.speed(0) # 타겟이 이동하지 않습니다.
    #target.penup() # 타겟의 이동경로를 표시하지 않습니다.
    target.goto(4 * scale, 4 * scale) # 타겟을 x : 4 * scale, y : 4 * scale 위치로 이동시킵니다.
    user.goto(-4 * scale, -4 * scale) # 유저를 x : -4 * scale, y : -4 * scale 위치로 이동시킵니다.
    changedtime = time.time() # changetime을 현재 시간으로 설정합니다. 유저의 상태가 변경된 시간을 확인하기 위해 사용됩니다.
    userstat = 1 # userstat을 1로 설정합니다.
    while True:
        user.clear() # 유저를 초기화 합니다.
        if abs(changedtime - time.time()) > 0.3 and userstat == 1: # 유저가 입벌림 상태이고 상태가 변경된 지 0.3초 지났을 경우,
            user.shape("images\circle.gif") # 유저를 입닫음 상태로 변경합니다.
            changedtime = time.time() # 유저의 상태변경이 끝남을 선언합니다.
            userstat = 0 # 유저가 입닫음 상태임을 확인합니다.
        if abs(changedtime - time.time()) > 0.3 and userstat == 0: # 유저가 입닫음 상태이고 상태가 변경된 지 0.3초가 지났을 경우,
            # 유저를 입벌림 상태로 변경합니다. 현재 유저가 어느방향을 보고 있는 지에 따라 해당방향의 모양으로 변경합니다.
            if beforemove == 0:
                user.shape("images\packman_0.gif")
            elif beforemove == 90:
                user.shape("images\packman_90.gif")
            elif beforemove == 180:
                user.shape("images\packman_180.gif")
            elif beforemove == 270:
                user.shape("images\packman_270.gif")
            changedtime = time.time() # 유저의 상태변경이 끝남을 선언합니다.
            userstat = 1 # 유저가 입벌림 상태임을 확인합니다.
        screen.onkeypress(move_right, "Right") # 키보드 우이동키 입력 이벤트를 받았을 때, move_right()을 수행합니다.
        screen.onkeypress(move_left, "Left") # 키보드 좌이동키 입력 이벤트를 받았을 때, move_left()을 수행합니다.
        screen.onkeypress(move_up, "Up") # 키보드 상이동키 입력 이벤트를 받았을 때, move_up()을 수행합니다.
        screen.onkeypress(move_down, "Down") # 키보드 하이동키 입력 이벤트를 받았을 때, move_down()을 수행합니다.
        if user.distance(target) < 1: # 유저가 타겟에 도달 할 경우,
            user.reset() # 유저를 초기화 하고
            screen.reset() # 스크린을 초기화 하고
            target.reset() # 타겟을 초기화 하고
            break # 반복문을 벗어나 함수를 종료합니다.


if __name__ == '__main__': # 메인함수
    stagecount = 0 # stagecount 변수를 선언합니다.
    beforemove = 0 # beforemove 변수를 선언합니다.
    scale = 40 # scale 변수를 선언합니다. 값 변경 시, display되는 게임의 크기가 달라집니다.
    scores = [] # 유저이름과 점수를 저장 할 배열을 선언합니다.
    user = user() # 유저 객체 선언 함수를 실행합니다.
    target = target() # 타겟 객체 선언 함수를 실행합니다.
    screen = init() # 스크린 객체 선언 함수를 실행합니다.
    texttuetle = texttuetle() # 텍스트 작성 객체 선언 함수를 실행합니다.
    while True:
        while stagecount < 5: # 총 다섯번의 게임이 이루어 지도록 반복문을 실행합니다.
            player = getname().upper() # 유저의 이름을 저장합니다. 유저의 이름은 항상 대문자로 입력됩니다.
            score = gameturn() # 게임을 실행하고 리턴받은 시도횟수를 저장 합니다.
            scores.append([player, score]) # 선언된 배열에 유저이름과 점수를 저장합니다.
            stagecount += 1 # 한번의 게임이 끝났음을 선언합니다.
        gamesummary(scores) # 다섯번의 게임동안 저장한 유저이름과 점수를 gamesummary() 함수로 보냅니다.
        scores = [] # 저장된 유저이름과 점수를 초기화 합니다.
        stagecount = 0 # 다섯번의 게임이 끝나고 값을 초기화합니다.