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
    
    def zone(self):
        fill(77)
        noStroke()
        rect(0, 0, 192, 480)
        rect(448, 0, 192, 480)
        rect(192, 0, 448, 112)
        rect(192, 368, 448, 112)
        
    def draw(self):
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
    def __init__(self, x, y, w, h, title, func, clr=color(244, 245, 232)):
        self.panel = panel
        self.bx = x
        self.by = y
        self.bWidth = w
        self.bHeight = h
        self.bTitle = title
        self.bFunc = func
        self.bColor = clr
        self.bStrkColor = 0
        self.halfWidth = w + (len(title) * 2.8)
           
    def draw(self):
        if self.bWidth  < self.halfWidth:
            self.bWidth  = self.halfWidth
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

class Interface():
    def __init__(self):
        bSave = bBlack = bGray = bRed = bOrange = bYellow = bGreen = bBlue = bViolete = None
        self.btns = [bSave, bBlack, bGray, bRed, bOrange, bYellow, bGreen, bBlue, bViolete]
        self.func = {"SF":self.saveToFile, "CC":self.changeColor}
        for bInd in range(len(self.btns)):
            if self.btns[0] == None:
                self.btns[0] = Button(0, 20, 20, 20, "Save", "SF") 
            if self.btns[1] == None:
                self.btns[1] = Button(40, 20, 20, 20, "", "CC", color(0, 0, 0))
            if self.btns[2] == None:
                self.btns[2] = Button(60, 20, 20, 20, "", "CC", color(185, 185, 185))
            if self.btns[3] == None:
                self.btns[3] = Button(80, 20, 20, 20, "", "CC", color(255, 0, 0))
            if self.btns[4] == None:
                self.btns[4] = Button(100, 20, 20, 20, "", "CC", color(255, 132, 0))
            if self.btns[5] == None:
                self.btns[5] = Button(120, 20, 20, 20, "", "CC", color(255, 255, 0))
            if self.btns[6] == None:
                self.btns[6] = Button(140, 20, 20, 20, "", "CC", color(0, 255, 0))
            if self.btns[7] == None:
                self.btns[7] = Button(160, 20, 20, 20, "", "CC", color(0, 0, 255))
            if self.btns[8] == None:
                self.btns[8] = Button(180, 20, 20, 20, "", "CC", color(255, 0, 255))
    def draw(self):
        for btn in self.btns:
            btn.draw()
            self.func[btn.bFunc](btn)
        self.config(0, 10)
        
    def whiteToBlack(self, img):
        inverted_img = createImage(img.width, img.height, RGB)
        for x in range(img.width):
            for y in range(img.height):
                i = ((y * img.width)+x); 
                if img.pixels[i] == color(255, 255, 255):
                    inverted_img.pixels[i] = color(0, 0, 0)
                elif img.pixels[i] == color(0, 0, 0):
                    inverted_img.pixels[i] = color(255, 255, 255)
        return inverted_img
            
    def saveToFile(self, btn):
        if btn != None:
            if btn.mouseIsClicked():
                save('img/screen.png')
                photo = loadImage('img/screen.png')
                photo = get(192, 112, 256, 256)
                photo.filter(THRESHOLD, 0.3)
                photo = self.whiteToBlack(photo)
                photo.save('img/frame.png')
        else:
            return None

    def changeColor(self, btn):
        global strkColor
        if btn != None:
            if btn.mouseIsClicked():
                strkColor = btn.bColor
        else:
            return None
    
    def config(self, x, y):
        self.x, self.y = x, y
        fill(255)
        noStroke()
        rect(0, 0, width, 12)
        textSize(10)
        fill(255, 10, 155)
        text("Config: Stroke weight({0}), mouseX({1}), mouseY({2})".format(strkWeight, pmouseX, pmouseY), self.x, self.y)
        textSize(9)
        fill(25, 25, 125)
        text("r=reset all | UP=increase weight | DOWN=decrease weight | LMB=black | RMB=white", self.x + width/2-30 - 22, self.y)

interface = None
panel = None
strkWeight = 1
strkColor = 1

def setup():
    global panel
    global interface
    panel = Panel()
    panel.setup()
    interface = Interface()
    size(640, 480)
    background(255, 255, 255)
    
def draw():
    global panel
    global interface
    global strkWeight
    global strkColor
    panel = Panel(mouseX, mouseY, pmouseX, pmouseY)
    panel.draw()
    panel.zone()
    interface.draw()

def keyPressed():
    global strkWeight
    global strkColor
    global panel
    if key == 'r' or key == 'R':
        background(255)
        strkWeight = 1
        strkColor = 0
    if key == CODED:
        if keyCode == UP:
            if strkWeight < 45:
                strkWeight += 1
        if keyCode == DOWN:
            if strkWeight > 0:
                strkWeight -= 1
                
def mouseWheel(event): 
    global strkWeight
    e = event.getCount()
    if strkWeight >= 45:
        strkWeight -= 1 
    elif strkWeight <= 1:
        strkWeight += 1
    elif  45 > strkWeight >= 1:
        strkWeight -= event.getCount()
