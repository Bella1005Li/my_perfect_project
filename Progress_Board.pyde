people = [
    {"name": "Alice", "progress": 35},
    {"name": "Bella", "progress": 60},
    {"name": "Sheldon", "progress": 80},
    {"name": "Bob", "progress": 45}
]

BAR_X = 200
BAR_Y_START = 120
BAR_W = 500
BAR_H = 30
BAR_GAP = 60

def setup():
    size(860, 420)
    surface.setTitle("Group Project Progress Board")
    colorMode(RGB)
    textAlign(LEFT)
    textSize(18)
    noStroke()
    background(255)
    
def draw():
    background(245)
    fill(0)
    textSize(26)
    text("Group Project Progress Board", 50, 60)
    
    for i, person in enumerate(people):
        draw_row(i, person)
        
    avg = sum(p["progress"] for p in people) / len(people)
    textSize(18)
    fill(30)
    text("Average Progress: " + str(int(avg)) + "%", 50, height - 40)
    
def draw_row(i, person):
    y = BAR_Y_START + i * BAR_GAP
    name = person["name"]
    progress = person["progress"]
    
    fill(220)
    rect(BAR_X, y, BAR_W, BAR_H, 8)
    
    c = progress_color(progress)
    fill(c)
    rect(BAR_X, y, BAR_W * progress / 100, BAR_H, 8)
    
    fill(0)
    text(name, 40, y + BAR_H - 5)
    text(str(progress) + "%", BAR_X + BAR_W + 20, y + BAR_H - 5)
    
def progress_color(p):
    red_c=color(255, 0, 0)
    yellow_c=color(255, 255, 0)
    green_c=color(0, 200, 0)
    
    if p <= 50:
        t = p / 50.0
        return lerpColor(red_c, yellow_c, t)
    else:
        t = (p - 50) / 50.0
        return lerpColor(yellow_c, green_c, t)

def mousePressed():
    i=row_index_at(mouseX, mouseY)
    if i >= 0:
        if mouseButton == LEFT:
            update_progress(i, +5)
        elif mouseButton == RIGHT:
            update_progress(i, -5)
            
def row_index_at(x, y):
    for i in range(len(people)):
        top = BAR_Y_START + i * BAR_GAP
        bottom = top + BAR_H
        if top <= y <= bottom:
            return i
    return -1

def update_progress(i, delta):
    people[i]["progress"] = constrain(people[i]["progress"] + delta, 0, 100)
