# -*- coding: utf-8 -*-

"""
Module spirograph(万花尺).
"""
import math
import turtle

# master_R      母尺半径
# child_r       子尺半径
# distance_s    子尺孔位距圆心距离，实际应小于r，程序里可以大于r
# relative_mode  0内环齿轮，1外环齿轮
master_R = 100
child_r = 65
distance_s = 35
relative_mode = 1

# draw the circle using turtle
#    R    母尺半径
#    r    子尺半径
#    s    子尺孔位距圆心距离，实际应小于r，程序里可以大于r
# mode    0内环齿轮，1外环齿轮
def drawCircleTurtle(R, r, s, mode=0):
# move to the start of circle
    turtle.speed("fastest")
    turtle.width(1)
    turtle.pencolor('blue')
    turtle.up()
    if mode==0:
        turtle.setpos(R-r+s, 0)
    else:
        turtle.setpos(R+r+s, 0)
    turtle.down()

    #大圆小圆半径最大公约数Greatest Common Divisor(GCD)
##    gcd=0
##    for i in range(1,r,1):
##        if r%i==0:
##            if R%(r/i)==0:
##                gcd=r/i
##                break        
##    if gcd==0:
##        print('小圆无公约数')
##        return
##    else:
##        count=int(r/gcd)
##        print(count)
    
    # draw the circle
    cnt=0 #统计周数
    maxCnt=100 #设置最大周数，防止无限绘制
    for i in range(0, 360*maxCnt, 1):#1是转动最小步进度数
        #颜色设置
        if i//360%4==1:
            turtle.pencolor('red')
        elif i//360%4==2:
            turtle.pencolor('green')
        elif i//360%4==3:
            turtle.pencolor('orange')
        else:
            turtle.pencolor('blue')
        #角度转为弧度
        a = math.radians(i)
        #(x,y)子尺圆心位置
        #i是孔位相对于母尺的度数，j是孔位相对于子尺的度数
        if mode==0:            
            x=(R-r)*math.cos(a)
            y=(R-r)*math.sin(a)            
            j=(-1)*(R*i/r)
        else:
            x=(R+r)*math.cos(a)
            y=(R+r)*math.sin(a)
            j=(R*i/r)
        #角度转为弧度
        a = math.radians(j)
        #print(i,j,a)
        #(x,y)转为孔位位置
        x=x+s*math.cos(a)
        y=y+s*math.sin(a)
        turtle.setpos(x, y)
        if i%360==0:
            cnt+=1  #统计周数递增
            print(j%360)#打印孔位在子尺上的度数
            #j!=0排除初始时位置
            #如果j%360==0说明孔位回到初始位置，
            #实际随参数不同孔位不一定能正好回到原位置，
            #这里j%360<5设了一个接近值
            if j!=0 and j%360<5:                
                break
    print('共 %s 周'%cnt)
#设置画布尺寸
#turtle.screensize(1500,1500)
#设置乌龟形状“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
#turtle.shape('arrow')
#drawCircleTurtle(160, 58, 50, 1)
drawCircleTurtle(master_R, child_r, distance_s, relative_mode)
#隐藏乌龟形状
turtle.hideturtle()
#显示乌龟形状
#turtle.showturtle()
#导出eps图片文件，只能用专业软件打开，如PS
ts = turtle.getscreen()
ts.getcanvas().postscript(file="spirograph.eps")
turtle.mainloop()
