class Panel:
    def __init__(self, mx=0, my=0, pmx=0, pmy=0):
        global strkWeight
        global strkColor
        self.mx = mx
        self.my = my
        self.pmx = pmx
        self.pmy = pmy
        self.strkWeight = strkWeight
        self.strkColor = strkColor
        
    def setup(self):
        strokeWeight(1)
        
    def config(self, x, y):
        self.x, self.y = x, y
        fill(255)
        noStroke()
        rect(0, 0, width, 12)
        textSize(10)
        fill(255, 10, 155)
        text("Config: Stroke weight({0}), mouseX({1}), mouseY({2})".format(self.strkWeight, self.mx, self.my), self.x, self.y)
        textSize(9)
        fill(25, 25, 125)
        text("r=reset all | UP=increase weight | DOWN=decrease weight | LMB=white | RMB=black", self.x + width/2-30 - 22, self.y)
        
    def draw(self):
        self.config(0, 10)
        stroke(self.strkColor)
        strokeWeight(self.strkWeight)
        
        if mousePressed and mouseButton == LEFT:
            line(self.mx, self.my, self.pmx, self.pmy)
        if mousePressed and mouseButton == RIGHT:
            self.erase()
        
    def erase(self):
        self.strkColor = 255
        stroke(self.strkColor)
        line(self.mx, self.my, self.pmx, self.pmy)
    
class Button():
    def __init__(self, x, y, w, h, title, clr=color(244, 245, 232)):
        self.panel = panel
        self.bx = x
        self.by = y
        self.bWidth = w
        self.bHeight = h
        self.bStrkColor = 0
        self.bColor = clr
        self.bTitle = title
        self.halfWidth = w + (len(title) * 2.8)
           
    def draw(self):
        if self.bWidth  < self.halfWidth:
            self.bWidth  = self.halfWidth
        # else:
        #     flag = False
        stroke(0)
        strokeWeight(0)
        fill(self.bColor)
        rect(self.bx, self.by, self.bWidth, self.bHeight)
        fill(0)
        text(self.bTitle, self.bx + self.bWidth/2 - len(self.bTitle) * 2.8 + 1, self.by + self.bHeight/2 + 4)
        
    def mouseIsClicked(self):
        if mouseX > self.bx and mouseX < (self.bWidth+self.bx ) and mouseY > self.by and mouseY < (self.bHeight+self.by) and mousePressed:
            return True
        return False
    
def saveToFile(clrBtns):
    for btn in clrBtns:
        if btn.mouseIsClicked():
            save('img/screen.png')
            photo = loadImage('img/screen.png')
            photo = get(0, 41, 640, 440)
            photo.save('img/frame.png')

def changeColor(clrBtns):
    global strkColor
    for btn in clrBtns:
        if btn.mouseIsClicked():
            strkColor = btn.bColor
        
panel = None
bSave = bBlack = bGray = bRed = bOrange = bYellow = bGreen = bBlue = bViolete = None
btns = [bSave, bBlack, bGray, bRed, bOrange, bYellow, bGreen, bBlue, bViolete]
strkWeight = 1
strkColor = 1
def setup():
    global panel
    global btns
    panel = Panel()
    panel.setup()
    
    size(640, 480)
    background(255, 255, 255)
    for bInd in range(len(btns)):
        if btns[0] == None:
            btns[0] = Button(0, 20, 20, 20, "Save") 
        if btns[1] == None:
            btns[1] = Button(40, 20, 20, 20, "", color(0, 0, 0))
        if btns[2] == None:
            btns[2] = Button(60, 20, 20, 20, "", color(185, 185, 185))
        if btns[3] == None:
            btns[3] = Button(80, 20, 20, 20, "", color(255, 0, 0))
        if btns[4] == None:
            btns[4] = Button(100, 20, 20, 20, "", color(255, 132, 0))
        if btns[5] == None:
            btns[5] = Button(120, 20, 20, 20, "", color(255, 255, 0))
        if btns[6] == None:
            btns[6] = Button(140, 20, 20, 20, "", color(0, 255, 0))
        if btns[7] == None:
            btns[7] = Button(160, 20, 20, 20, "", color(0, 0, 255))
        if btns[8] == None:
            btns[8] = Button(180, 20, 20, 20, "", color(255, 0, 255))
    
    
def draw():
    global panel
    global btns
    global strkWeight
    global strkColor
    panel = Panel(mouseX, mouseY, pmouseX, pmouseY)
    
    for btn in btns:
        btn.draw()
    panel.draw()
    changeColor(btns)
    saveToFile(btns)

def keyPressed():
    global strkWeight
    global strkColor
    global panel
    if key == 'g':
        strkColor = 0
    if key == 'r':
        background(255)
        strkWeight = 0
        strkColor = 0
    if key == 's':
        save('img/screen.png')
        photo = loadImage('img/screen.png')
        photo = get(10, 12, 500, 500)
        photo.save('img/frame.png')
    if key == CODED:
        if keyCode == UP:
            if strkWeight < 45:
                strkWeight += 1
        if keyCode == DOWN:
            if strkWeight > 1:
                strkWeight -= 1
