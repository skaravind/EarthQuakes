globe = PShape

# 22.5726° N, 88.3639° E
class earthquake():
    pass

def setup():
    global r, globe, lat, lon, lines, eqs, Error
    Error = 0
    eqs = []
    r = 200
    global earth
    global PShape
    size(600,600, P3D)
    background(0)
    earth = loadImage("earth.jpg")
    noStroke()
    globe = createShape(SPHERE, r)
    globe.setTexture(earth)
    
    lines = loadStrings("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv")
    if lines == None:
        Error = 1
    else:
        for i in range(1,len(lines)):
            eq = earthquake()
            ln = lines[i].split(',')
            eq.lat = ln[1]
            eq.lon = ln[2]
            eq.magn = ln[4]
            eqs.append(eq)

angle = 0
angleY = 0
def draw():
    global angle, angleY
    background(0)
    textAlign(CENTER)
    textSize(20)
    if Error == 1:
        fill(255,0,0)
        text('No internet Connection', width/2, 50)
        noLoop()
    fill(255)
    text('WASD to move around the globe, X to refresh', width/2, 25)
    text('Height of the red box is proportional to Richter Scale', width/2, height - 25)
    translate(width/2, height/2)
    noStroke()
    lights()
    
    if keyPressed:
        pushMatrix()
        if key == 'w':
            angle-=0.02
            rotateX(angle)
            rotateY(angleY)
            shape(globe)
        if key == 'a':
            angleY+=0.02
            rotateX(angle)
            rotateY(angleY)
            shape(globe)
        if key == 's':
            angle+=0.02
            rotateX(angle)
            rotateY(angleY)
            shape(globe)
        if key == 'd':
            angleY-=0.02
            rotateX(angle)
            rotateY(angleY)
            shape(globe)
        if key == 'x':
            setup()
        popMatrix()

    rotateX(angle)
    rotateY(angleY)
    shape(globe)
        
    for i in range(len(eqs)):
        lat = eqs[i].lat
        lon = eqs[i].lon
        magn = eqs[i].magn
        lat = radians(float(lat))
        lon = radians(float(lon))
        theta = lat + PI/2
        phi = -lon + PI
        x = float(r * sin(theta) * cos(phi))
        y = float(r * cos(theta))
        z = float(r * sin(theta) * sin(phi))
        pos = PVector(x,y,z)
        xaxis = PVector(1,0,0)
        h = pow(10,float(magn))
        maxh = pow(10,8)
        minh = pow(10,4.5)
        h = map(h, minh, maxh, 1, 120)
        angleb = PVector.angleBetween(xaxis, pos)
        raxis = xaxis.cross(pos)
        pushMatrix()
        translate(x,y,z)
        rotate(angleb, raxis.x, raxis.y, raxis.z)
        fill(255,0,0,150)
        box(h,6,6)
        popMatrix()