colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 1.0

p_move = 1.0

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

def init():
    p = []
    y = len(colors[0])
    x = len(colors)
    total_cells = x*y
    for i in range(x):
        p.append([])
        for j in range(y):
            p[i].append(1.0/total_cells)
    return p

def sense(p, Z):
    total=0.0
    q=[]
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[0])):
            hit = (Z == colors[i][j])
            current = p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right))
            q[i].append(current)
            total+=current
    for i in range(len(p)):
        for j in range(len(p[0])):
            q[i][j] = q[i][j] / total
    return q

def move(p, U):
    q=[]
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[0])):
            s = p_move * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[0])]
            s = s + ((1 - p_move) * p[i][j])
            q[i].append(s)
    return q

p = init()
for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])


#Your probability array must be printed 
#with the following code.

show(p)


