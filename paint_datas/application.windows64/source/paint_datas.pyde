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
        stroke(0)
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
            self.strkColor = 0
            stroke(self.strkColor)
            line(self.mx, self.my, self.pmx, self.pmy)
        if mousePressed and mouseButton == RIGHT:
            self.strkColor = 255
            stroke(self.strkColor)
            line(self.mx, self.my, self.pmx, self.pmy)

panel = None
strkWeight = 1
strkColor = 0
def setup():
    global panel
    panel = Panel()
    size(640, 480)
    background(255, 255, 255)
    
def draw():
    global panel
    global strkWeight
    panel = Panel(mouseX, mouseY, pmouseX, pmouseY)
    panel.setup()
    panel.draw()

def keyPressed():
    global strkWeight
    global strkColor
    if key == 'r':
        background(255)
        strkWeight = 1
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
