#DEMO CODE MADE IN DECEMBER 2022
#CONVERT
def convert_x(WIDTH, output_width, x):
  return int(x/WIDTH * output_width)

def convert_y(HEIGHT, output_height, y):
  return int(y/HEIGHT * output_height)

def convert_point(WIDTH, HEIGHT, output_width, output_height, X):
  return (convert_x(WIDTH, output_width, X[0]), convert_y(HEIGHT, output_height, X[1]))


#####HEAD#####
from PIL import Image
from PIL import ImageColor
with open('projekt.ves', 'r+') as f:
  lines = []
  for line in f:
    lines.append(line)
head = lines[0]
head = head.split(" ")
#head = f.readline().split(" ")
if len(head) != 4:
  print("Error, wrong input")
verzia = head[1]
WIDTH = head[2]
HEIGHT = head[3]
x = input("Zadaj sirku obrazku. Ak chces zanechat povodne rozlisenie suboru stlac ENTER: ")
if x == "":
  output_width = WIDTH
  output_height = HEIGHT
else:
  output_width = round(float(x))
  output_height = int(int(HEIGHT)/int(WIDTH) * output_width)

#COLOR FOR OBJECTS
def hextorgb(clr):
  rgb = ImageColor.getcolor(clr,"RGB")
  return(rgb)

#CLEAR
for clr_line in lines:
  clr_line = clr_line.split(" ")     
  if clr_line[0] == "CLEAR":
      color = hextorgb(clr_line[1])

#COLOR FOR LINES
def hex2dec(cislo):
  vysledok = 0
  for index in range(len(cislo)):
    cifra = cislo[(index+1)*(-1)].upper()   
    if ord("A") <= ord(cifra) <= ord("F"):
      cifra = ord(cifra) - 65 + 10
    else:
      cifra = int(cifra)
    vysledok += cifra*16**index
  return vysledok

def LineColor(color):
  r = hex2dec(color[1:3])
  g = hex2dec(color[3:5])
  b = hex2dec(color[5:7])
  return (r, g, b)

print(verzia,output_width,output_height)
img = Image.new('RGB', (int(output_width), int(output_height)), color)

#############################

def linePixels(A, B):
  pixels = []
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      pixels.append((A[0], y))
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      pixels.append((x, A[1]))
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        pixels.append((x, y))
  return pixels

def line(im, A, B, color):
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      im.putpixel((A[0], y), color)
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      im.putpixel((x, A[1]), color)
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        im.putpixel((x, y), color)
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        im.putpixel((x, y), color)

#############################

def circle(im, S, r, thickness, color):
  thickness -= 1
  for x in range(0, int(r/2**(1/2)) + 1):
    y = int((r**2 - x**2)**(1/2))
    line(im, (x + S[0] - thickness, y + S[1] - thickness),(x + S[0], y + S[1]), color)
    line(im, (y + S[0] - thickness, x + S[1] - thickness), (y + S[0], x + S[1]), color)
    line(im, (y + S[0] - thickness, -x + S[1] + thickness),(y + S[0], -x + S[1]), color)
    line(im, (x + S[0] - thickness, -y + S[1] + thickness), (x + S[0], -y + S[1]), color)
    line(im, (-x + S[0] + thickness, -y + S[1] + thickness), (-x + S[0], -y + S[1]), color)
    line(im, (-y + S[0] + thickness, -x + S[1] + thickness), (-y + S[0], -x + S[1]), color)
    line(im, (-y + S[0] + thickness, x + S[1] - thickness), (-y + S[0], x + S[1]), color)
    line(im, (-x + S[0] + thickness, y + S[1] - thickness), (-x + S[0], y + S[1]), color)

def fill_circle(im, S, r, color):
  for x in range(0, int(r/2**(1/2)) + 1):
    y = int((r**2 - x**2)**(1/2))
    if 0 < x + int(S[0]) < int(WIDTH) and 0 < int(y) + int(S[1]) < int(HEIGHT):
      line(im, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
      line(im, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
      line(im, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
      line(im, (-y + S[0], x + S[1]), (-y + S[0], -x + S[1]), color)

def getY(point):
  return point[1]

#############################

def thick_line(im, A, B, thickness, color):
  pixels = linePixels(A, B)
  for X in pixels:
    fill_circle(im, X, thickness/2, color)

def triangle(im, A, B, C, thickness, color):
  thick_line(im, A, B, thickness, color)
  thick_line(im, A, C, thickness, color)
  thick_line(im, C, B, thickness, color)

def fill_triangle(im, A, B, C, color):
  V = sorted([A, B, C], key=getY)
  left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
  right = linePixels(V[0], V[2])
  Xmax = max(A[0], B[0], C[0])
  Xmin = min(A[0], B[0], C[0])
  if V[1][0] == Xmax:
    left, right = right, left

  for y in range(getY(V[0]), getY(V[2]) + 1):
    x1 = Xmax
    for X in left:
      if X[1] == y and X[0] < x1:
        x1 = X[0]
    
    x2 = Xmin
    for X in right:
      if X[1] == y and X[0] > x2:
        x2 = X[0]
    
    if x2 < 0:
      continue
    if x2 > im.width:
      x2 = im.width - 1
    if x1 < 0:
      x1 = 0
    line(im, (x1, y), (x2, y), color)

def rect(im, A, width, height, thickness, color):
  thick_line(im, A, (A[0]+ width, A[1]), thickness, color)
  thick_line(im, (A[0]+ width, A[1]), (A[0]+ width, A[1] + height), thickness, color)
  thick_line(im, A, (A[0], A[1] + height), thickness, color)
  thick_line(im, (A[0], A[1] + height), (A[0] + width, A[1] + height), thickness, color)

def fill_rect(im, A, width, height, color):
  for x in range(A[0], A[0] + width):
    for y in range(A[1], A[1] + height):
      im.putpixel((x, y), color)

#############################

counter = 0      
for rline in lines:
  counter += 1
  rline = rline.split(" ")
  
  try:
    if rline[0] == "VES" or rline[0] == "CLEAR":
      pass 
    elif rline[0] == "LINE":
      line_color = LineColor(rline[5])
      thick_line(img, (round(float(rline[1])), round(float(rline[2]))), (round(float(rline[3])), round(float(rline[4]))), round(float(rline[5])), line_color)
    elif rline[0] == "CIRCLE":
      circle_color = hextorgb(rline[5])
      circle(img, (round(float(rline[1])), round(float(rline[2]))), round(float(rline[3])), round(float(rline[4])), circle_color)
    elif rline[0] == "FILL_CIRCLE":
      fill_circle_color = hextorgb(rline[4])
      fill_circle(img, (round(float(rline[1])), round(float(rline[2]))), round(float(rline[3])), fill_circle_color)
    elif rline[0] == "FILL_TRIANGLE":
      fill_triangle_color = hextorgb(rline[7])
      fill_triangle(img, (round(float(rline[1])), round(float(rline[2]))), (round(float(rline[3])), round(float(rline[4]))), (round(float(rline[5])), round(float(rline[6]))), fill_triangle_color)
    elif rline[0] == "TRIANGLE":
      triangle_color = hextorgb(rline[8])
      triangle(img, (round(float(rline[1])), round(float(rline[2]))), (round(float(rline[3])), round(float(rline[4]))), (round(float(rline[5])), round(float(rline[6]))),round(float(rline[7])) ,triangle_color)
    elif rline[0] == "FILL_RECT":
      fill_rect_color = hextorgb(rline[5])
      fill_rect(img, (round(float(rline[1])), round(float(rline[2]))), round(float(rline[3])), round(float(rline[4])), fill_rect_color)
    elif rline[0] == "RECT":
      rect_color = hextorgb(rline[6])
      rect(img, (round(float(rline[1])), round(float(rline[2]))), round(float(rline[3])), round(float(rline[4])), round(float(rline[5])), rect_color)
    elif len(rline[0:]) >= 0 and len(rline[0:]) <= 1:
      print(f"Line {counter} is empty")
    #elif len(rline[-1]) >= 0 and len(rline[-1]) <= 1:
      #print(f"Line {counter} ignored")
    else:
      print(f"Syntax error on line {counter}: Unknown command {rline[0]}")
  except:
    print(f"Syntax error on line {counter}")

img
