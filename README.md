# DS_TW_P1
DataScience_TeamWork_Platoon1

# [0] 교수님 지시사항 Requirement

```python
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
```

## 100*100 의 맵이 있다.

turtle 을 통해 100, 100 사이즈의 캔버스를 만들어줍니다.

## 맵에서의 움직임은 좌 우 위 아래 로 가능하다.

사용자의 키보드 입력에 따라 좌 우 위 아래로 움직이도록 만들어준다.

```python

def move_right():
    if user.xcor() >= 5*scale:
        user.setx(5*scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(0)
    user.shape("images\packman_0.gif")
    global beforemove
    beforemove = 0
    user.forward(1*scale)

def move_left():
    if user.xcor() <= -5*scale:
        user.setx(-5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(180)
    user.shape("images\packman_180.gif")
    global beforemove
    beforemove = 180
    user.forward(1*scale)

def move_up():
    if user.ycor() >= 5*scale:
        user.sety(5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(90)
    user.shape("images\packman_90.gif")
    global beforemove
    beforemove = 90
    user.forward(1*scale)

def move_down():
    if user.ycor() <= -5*scale:
        user.sety(-5 * scale)
        return
    global tryCount
    tryCount -= 1
    user.setheading(270)
    user.shape("images\packman_270.gif")
    global beforemove
    beforemove = 270
    user.forward(1*scale)

screen.listen()
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
```

## 임의로 설정된 목표

목표를 random 값으로 설정한다

```python
target.goto(random.randint(-5, 5)*scale, random.randint(-5,5)*scale)
```

### 처음 (0,0) 에 설정된 터틀을 통해서

터틀의 기본 생성위치는 0,0 이다.

```python
user.penup()
    user.goto(-5*scale, -5*scale)
```

### 터틀이 목표에 다가가는 것을 위한 게임

터틀이 목표에 도달하면 게임이 끝난다

```python
if user.distance(target) < 1 or tryCount == 0:
            time.sleep(0.3)
            user.reset()
            screen.reset()
            target.reset()
            break
```

터틀은 사용자가 직접 입력을 통해 이동

터틀의 이동은 한번에 3개의 좌 우 위 아래

### 목표는 사용자의 움직임에 맞게 최대한 잡히지 않도록 이동한다

### 목표의 이동은 한번에 2개의 좌 우 위 아래

해당 내용은 터틀 회피 알고리즘에 자세히 설명됩니다.

## 처음 이동은 목표부터 시작이며 터틀과 차례로 이동할 수 있도록 한다.

사용자가 이동시마다 trycount 를 변경 (해당 알고리즘에선 감소)하며

3이 추가 or 감소 되었을때 목표를 2회 이동시킨다

```python
				if (tryCount+2)%3 == 0 and beforemoved != tryCount:
            targetmove()
            targetmove()
            beforemoved = tryCount
        screen.listen()
        screen.onkeypress(move_right, "Right")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
```

## 이를 통해 총 5번의 게임이 이루어졌을 때

게임의 진행횟수는 5번이며 stage count 를 통해 5회를 count 한다.

```python
while True:
        while stagecount < 5:
            player = getname().upper()
            score = gameturn()
            scores.append([player, score])
            stagecount += 1
        gamesummary(scores)
        scores = []
        stagecount = 0
```

## 시도횟수와 사용자이름을 기록하여 이를 정렬하여 보여준다

5회에 도달했을경우 score 와, name 을 정렬하여 보여준다

```python
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
```

# [1] 터틀의 이동

### 1. 캔버스생성

- Turtle 모듈을 불러와(import) Screen 객체를 생성합니다.
그 후 setup함수를 사용하여 캔버스를 생성합니다.
    - 예시) screen.setup(100,100)

### 2. 키보드 입력

- 키보드 입력은 기본적으로 screen.listen으로 키보드의 입력을 대기시킵니다. 
그 다음 onkeypress 함수로 키보드를 누르고 있을 때의 이벤트를 설정합니다.

### 3. 목표 ( target) 생성

- 우리가 이동시킬 거북이를 생성하는 것 처럼 목표 거북이 또한 Turtle 모듈을 이용하여 목표(Target)을 생성시킵니다.
    
    ```python
    target = t.Turtle()
    ```
    
- 이후  shape함수로 모양을 만들어 준 후 speed함수로 스피드를 지정, goto 함수로 랜덤한 좌표 위치를 생성하여 작성합니다.
    
    ```python
    target.goto(random.randint(-100,100), random.randint(-100, 100))
    ```
    

### 4. 거북이 이동

- 거북이는 생성한 거북이(예시 : turtle, t1…)의backward, forward 함수에 숫자를 인수로 주어 이동시킬 수 있습니다.
    
    ```python
    turtle.forward(100)
    ```
    

### 5. 거북이 회전

- 거북이는 이동과 비슷하게 left와 right함수에 숫자를 인수로 주어 회전시킬 수 있습니다.
    - 예시)turtle.right(30) <거북이를 오른쪽으로 30도 회전

### 6. 울타리 생성

- 거북이가 정해진 울타리 밖으로 나가지 않도록 울타리를 생성해야합니다. 생성한 거북이(예시 : turtle, t1…)의 맨 왼쪽 위부터 시작하도록 하자. 이는 중앙에서 왼쪽 위까지 선이 그려지는 것을 방지합니다.
    - turtle.penup()
- 그 다음 거북이를 -100, 100으로 setposition함수를 사용하여 왼쪽 위로 이동합니다.
    - turtle**.**setposition(-100, 100)
- 왼쪽 위로 이동하였으면 다시 선을 긋기 위하여 펜을 아래로 내립니다.
    - turtle.pendown()

# [2] 타겟 회피 알고리즘

## 알고리즘 조건

- 임의로 설정된 지역에 목표가 생성되며 플레이어가 이동을 마쳤을 시 목표는 좌, 우 아래, 위방향으로 한 번에 두 번 이동합니다.
- 타겟이 이동할 수 있는 구역은 up, down, right, left 총 4가지 입니다.
- 타겟이 이동 불가능한 구역은 맵의 가장자리 (+_5 * scale ), 사용자 입니다.

### 타겟 이동

- 목표(타겟)의 X좌표와 Y좌표를 다음 코드로 가져와 활용합니다.

```python
x = target.xcor()
y = target.ycor()
```

- 이동할 x, 이동할 y 좌표, 벽까지의 거리 를 기본으로 넣습니다.

```python
up = [x + scale, y, abs(5*scale - (x + scale))]
down = [x - scale, y, abs(-5*scale - (x - scale))]
right = [x, y + scale, abs(5*scale - (y + scale))]
left = [x, y - scale, abs(-5*scale - (y - scale))]
allcase = [up, down, right, left]
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0768df19-2fc2-4c8d-82a5-01d2d04ec787/Untitled.png)

- 모든 경우의 수 중 불가능한 경우를 제거합니다
    - x 및 y 의 좌표가 5scale 을 넘는경우 제거합니다
- 가능한 이동 좌표 에서는 사용자까지의 거리를 피타고라스의 정리를 통해 구합니다
    - 이때 사용자와 부딛힐 경우 거리는 0이 됩니다
    - 사용자까지x 거리 제곱 + 사용자까지 y 거리 제곱 의 제곱근을 구합니다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44e666a0-4936-4b66-9de1-4de788eda836/Untitled.png)
    
- 구한 값을 사용자까지 거리 순으로 정렬합니다.
    - 사용자의 거리가 0일 경우 가장 후순위로 밀리게 되어 사용자에 충돌하지 않습니다.

```python
possablecase = []
for case in allcase:
    casetouserx = abs(case[0]-user.xcor())
    casetousery = abs(case[1]-user.ycor())
    if abs(case[0]) <= 5*scale and abs(case[1]) <= 5*scale:
        casetouser = math.sqrt(casetouserx**2 + casetousery**2)
        case.append(casetouser)
        possablecase.append(case)
possablecase.sort(key=lambda x: x[3], reverse = True)
```

- 0순위 case 의 사용자와의 거리와 같은 값이 발생할 수 있어 해당 값을 분류해줍니다
    - 아래의 코드에서는 bestcases 로 해당 값을 넣어줍니다.
    - 해당 항목중 벽과의 거리가 먼 항목을 bestcase 로 지정합니다.
    - 아래의 그림과 같은경우 벽에서 먼 왼쪽을 선택하게 됩니다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/845837df-ed42-4282-957d-12f869af0785/Untitled.png)
        
    - 이로써 아래의 사진과 같이 코너에 몰렸을 경우에도 사용자로부터 회피할 수 있도록 합니다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4aa737c0-320d-4cbb-b36b-c360c5f28a50/Untitled.png)
    

```python
for case in possablecase:
    if case[3] == possablecase[0][3]:
        case[0]
        bestcases.append(case)
print(bestcases)
bestcases.sort(key=lambda x: x[2], reverse = True)
bestcase = bestcases[0]
```

- 이후 bestcase의 좌표로 이동시킵니다.

```python
target.setposition(bestcase[0], bestcase[1])
```

# [3] User Interface

## 1. 플레이어 (터틀)

사용자는 상 하 좌 우 모양이 있으며, 입을 벌리고 닫는 동작을 반복합니다.

이떄 onkeypress scan 을 위해 무한 반복되는 구간이 있어 아래의 동작을 수행합니다.

1.  해당 동작이 수행하는 시점의 시간을 확인
2.  0.3 초 마다 지정된 모양으로 변경 ( 원↔진행방향으로 입벌리기)

```python
while True:
        user.clear()
        if abs(changedtime - time.time()) > 0.3 and userstat == 1:
            user.shape("images\circle.gif")
            changedtime = time.time()
            userstat = 0
        if abs(changedtime - time.time()) > 0.3 and userstat == 0:
            if beforemove == 0:
                user.shape("images\packman_0.gif")
            elif beforemove == 90:
                user.shape("images\packman_90.gif")
            elif beforemove == 180:
                user.shape("images\packman_180.gif")
            elif beforemove == 270:
                user.shape("images\packman_270.gif")
            changedtime = time.time()
            userstat = 1
        screen.onkeypress(move_right, "Right")
        screen.onkeypress(move_left, "Left")
        screen.onkeypress(move_up, "Up")
        screen.onkeypress(move_down, "Down")
```

## 2. 타겟 ( 유령 )

유령 모양 테마를 씌워줍니다.

```python
def target():
    # 타겟 Shape 추가
    t.addshape("images\ghost.gif")
    # 타겟 객체 생성
    target = t.Turtle()
    target.shape("images\ghost.gif")
    target.penup()
    return target
```

## 3. 배경

테마에 맞는 검은색 배경을 적용합니다.

```python
def init():
    screen = t.Screen() # 스크린 객체 생성
    screen.setup(16*scale,16*scale) # 화면의 크기는 지정된 scale 의 16배수 픽셀로 설정합니다.
    screen.bgcolor("black") # 배경을 검은색으로 지정합니다.
    screen.tracer(2) # 즉각적인 실행 (빠른 반응속도) 를 위해 tracer 을(를) 2로 지정합니다.
    return screen
```

## 4. 글꼴

Unispace 글꼴을 적용하며 폰트 사이즈를 15픽셀로 적용합니다.

해당 폰트는 윈도우11 이상에서 기본으로 제공합니다.

```python
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
    texttuetle.write("STAGE : " + str(stagecount + 1), align="right", font=("Unispace", 15, "normal"))
```

## 5. 울타리 ( 테마에 따른 파란 색상 사용 )

팩멘 테마에 맞는 파란 2줄의 울타리가 필요하므로, 터틀을 통해 작성해줍니다.

```python
def fence(crossline = True):
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
    fence.penup()
    fence.hideturtle()
    fence.setposition(-5.7 * scale, -5.7 * scale)
    fence.color("blue")
    fence.pendown()
    fence.pensize(2)
    for x in range(4):
        fence.forward(11.4 * scale)
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

        for i in range(10):
            fence.penup()
            fence.goto((i - 4.5) * scale, -5.5 * scale)
            fence.pendown()
            fence.goto((i - 4.5) * scale, +5.5 * scale)
            fence.penup()
```
