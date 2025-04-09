import pygame as pg
import sys
import random
# увеличиваем глубину рекурсий
sys.setrecursionlimit(6000000)
# цвета
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
brown=(255, 64, 64, 255)
grey=(128,128,128)
olive=(128,128,0)
purple=(128,0,128)
yellow=(255,255,0)
orange=(255,160,16)
pink=(255,96,208)
yellow_green=(96,255,128)
dict_colors={1:black,2:red,3:green,4:blue,5:brown,6:grey,
             7:olive,8:purple,9:yellow,10:orange,11:pink,12:yellow_green}
# стартовые свойства кисти
brush='pensil'
color=black
fat=1
# основная функция
def run(gun,color,fat):
    # основной класс руки
    class hand():
        def __init__(self,color,fat,brush):
            self.color=color
            self.fat=fat
            self.brush=brush
        def new_color(self,color):
            self.color=color
        def col(self):
            return self.color
        def new_fat(self,fat_new):
            self.fat=fat_new
        def fats(self):
            return self.fat
        def new_brush(self,word):
            self.brush=word
        def your_brush(self):
            return self.brush    
    # создание руки
    arm=hand(color,fat,gun)
    # стартовый цвет,толщина,кисть
    color=arm.col()
    fat_0=arm.fats() 
    # размер и название экрана
    screen = pg.display.set_mode((1000, 800))
    pg.display.set_caption("Paint")
    # массивы, хранящие обьекты
    massive_pips=[]
    massive_lines=[]
    # переменная,отвечающая за возможность рисовать, работает когда мышка нажата
    draying=False
    # создание прямоугольника, сохранения рисунка
    rect_save=pg.Surface((75,60))
    rect_save.fill(olive)
    # массив квадратиков цветов
    squares=[]
    # массив меню цветов
    rectes_color=[]
    for i in range(12):
        rect=pg.Rect((50*i,0,50,50))
        rectes_color.append(rect)
    # функция создания квадратиков цветов
    def square_colors(n):
        squar=pg.Surface((50,50))
        squar.fill(dict_colors[n])
        squares.append(squar)
    # создаем квадратики
    for n in range(12):
        square_colors(n+1)
    # функция рисования квадратиков цветов
    def draw_square(n):
        squar=squares[n]
        screen.blit(squar,(50*(n),0))
    # создание меню
    rect_sign=pg.Surface((50,50))
    rect_sign.fill(grey)
    rect_clear=pg.Surface((100,60))
    rect_clear.fill(grey)
    rect_brush=pg.Surface((100,50))
    rect_brush.fill(grey)
    # создаем шрифты для текстов
    pg.font.init()
    font_style = pg.font.SysFont("bahnschrift", 30) 
    score_font = pg.font.SysFont("comicsansms", 40)
    # функция написания чисел на квадратах
    def Your_colors(nn):
        value = font_style.render(str(nn), True, white)
        screen.blit(value, [10+(nn-1)*50, 8])
    # функция отрисовки квадратов знаков
    def sign(x,y,stroka):
        value = font_style.render(stroka, True, white)
        screen.blit(value, [x, y])    
    # функция отрисовки clear
    def Your_clear():
        value = score_font.render("clear", True, white)
        screen.blit(value, [900, 8])
    # функция отрисовки save
    def Your_save():
        value = font_style.render("save", True, white)
        screen.blit(value, [825, 14])
    # функция заливки экрана
    def kras(screen,x,y,color,color_0):
        if x>1 and x<999 and y>125 and y<799: 
            if screen.get_at((x, y+1))== color_0 :
                screen.set_at((x,y+1),color)
                kras(screen,x,y+1,color,color_0)
            if screen.get_at((x, y-1))==color_0:
                screen.set_at((x,y-1),color)
                kras(screen,x,y-1,color,color_0)
            if screen.get_at((x+1, y))==color_0 :
                screen.set_at((x+1,y),color)
                kras(screen,x+1,y,color,color_0)
            if screen.get_at((x-1, y))==color_0 :
                screen.set_at((x-1,y),color)
                kras(screen,x-1,y,color,color_0)
    # функция создание спрея
    def spreying(x0,y0,color,fat_0):
        x=x0-fat_0
        y=y0-fat_0
        for i in range(2*fat_0):
            for j in range(2*fat_0):
                if random.random()>0.92:
                    screen.set_at((x,y),color)
                x+=1
            x=x0-fat_0
            y+=1   
    # белый фон экрана
    screen.fill(white)
    # вывод дисплея
    screen.blit(rect_save,(820,0))
    screen.blit(rect_sign,(700,0))
    screen.blit(rect_sign,(755,0))
    screen.blit(rect_clear,(900,0))
    for i in range(5):
        screen.blit(rect_brush,(105*i,60))
    Your_clear()
    Your_save()
    # вывод и рисования дисплея
    sign(714,8,'-')
    sign(769,8,'+')
    sign(10,70,'pencil')
    sign(113,70,'rubber')
    sign(221,70,'filling')
    sign(327,70,'spray')
    sign(438,70,'lines')
    # рисование цветных квадратиков
    for n in range(12):
        draw_square(n)
    # написание цифер на цветах
    for i in range(12):
        Your_colors(i+1)
    # основной цикл
    while True:
        # наша кисть
        brush=arm.your_brush()  
        # перебор событий
        for event in pg.event.get():
            if event.type==pg.QUIT:
                sys.exit()
            # перебор мыши
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    if event.pos[1]>130:
                        draying=True
                        # заливка области
                        if brush=='filling':
                            color_0=screen.get_at((event.pos[0],event.pos[1]))
                            kras(screen,event.pos[0],event.pos[1],color,color_0)
                    # смена режима руки
                    if 60<event.pos[1]<120:
                        if event.pos[0]<100:
                            gun=arm.new_brush('color')
                        elif 105<event.pos[0]<205:
                            gun=arm.new_brush('clear')
                        elif 210<event.pos[0]<310:
                            gun=arm.new_brush('filling')
                        elif 315<event.pos[0]<415:
                            gun=arm.new_brush('spray')
                        elif 420<event.pos[0]<520:
                            gun=arm.new_brush('lines')
                    # начать заново
                    elif event.pos[1]<60 and event.pos[0]>900:
                        run(brush,color,fat_0)
                    # смена толщины
                    elif event.pos[1]<60 and event.pos[0]>700 and event.pos[0]<750:
                        if arm.fats()>1 and arm.fats()<=14:
                            arm.new_fat(arm.fats()-1)
                            fat_0=arm.fats()
                    elif event.pos[1]<60 and event.pos[0]>755 and event.pos[0]<815:
                        if arm.fats()>=0 and arm.fats()<14:
                            arm.new_fat(arm.fats()+1)
                            fat_0=arm.fats()
                    # кнопка сохранения
                    elif event.pos[1]<60 and event.pos[0]>=820 and event.pos[0]<=895:
                        pg.image.save(screen, "C:\\Users\\nicit\\Desktop\\Точечный рисунок.bmp")
                    # смена цветов
                    for i in range(12):
                        if rectes_color[i].collidepoint(pg.mouse.get_pos()):
                            arm.new_color(dict_colors[i+1])
                            color=arm.col()
                # режим рисования линий
                if brush=='lines':
                    if event.pos[1]>125:
                        massive_lines.append(event.pos)
                        if len(massive_lines)==2:
                            pg.draw.line(screen,color,massive_lines[0],massive_lines[1],fat_0)
                            massive_lines=[]
            # отпускание мыши
            elif event.type==pg.MOUSEBUTTONUP:
                massive_pips=[]
                draying=False
        # рисование
        if draying:
            if pg.mouse.get_pos()[1]>125:
                if brush=='color':
                    massive_pips.append(pg.mouse.get_pos())
                    if len(massive_pips)>1:
                        for i in range(1,len(massive_pips)):
                            pg.draw.line(screen,color,massive_pips[i-1],massive_pips[i],fat_0)
                elif brush=='clear':
                    pg.draw.circle(screen, white,(pg.mouse.get_pos()),fat_0)
                elif brush=='spray':
                    spreying(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],color,fat_0)                   
     
        pg.display.update()
        pg.time.delay(1)  
run(brush,color,fat)