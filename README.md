# VECTOR SCRIPT 
Vector Script (VES) defines a vector graphics format which preserves elementary graphic figures defined in accordance with mathematics instead of raster graphical information. If we talk about circle centered at point S and radius R, it is the same figure as in geometry we write with the notation k(S, R). In short, we made our own drawing script. We were able to draw lines, squares, circles and etc. with X and Y coordinates. More on how VES works can be found in project attachment `Vector Script.docx`
## General
The team project was created as a final high school assignment that utilizes both frontend and backend. It was the first larger project I have worked on. Drawing functions were coded in Python, frontend part used HTML, CSS and some elements from JavaScript. The first version of the project was using Python only. It was able to read from **.ves** files and it drew the objects immediately. The Second version was run with FLASK Python Web Server. Final version used web hosting `render.com`. The Last part of the project was WordPress page. We used it for the presentation and it was uploaded on hosting `endora.cz`. The wordpress site remains lost due to being discontinued for inactivity.

The latest version can be accessed using the following link: 
`https://vesprojekt-nvgj.onrender.com/`



## Preview

**Early version of the project without GUI**
![First](https://i.imgur.com/Er48o4I.png)




**Latest version of the project **
![Second](https://i.imgur.com/qo7CQhU.png)

**Wordpress website**
![Second](https://i.imgur.com/zgQsD5J.png)

**The code used in examples**
```VES v2.2 602 402
CLEAR #6f706c
FILL_TRIANGLE 65 220 100 300 50 300 #FFFFFF
FILL_TRIANGLE 535 220 500 300 550 300 #FFFFFF
LINE 0 300 598 300 2 #000000

FILL_TRIANGLE 0 0 250 399 100 399 #000000
TRIANGLE 0 0 250 400 100 400 2 #FFFFFF
FILL_TRIANGLE 599 0 350 399 500 399 #000000
TRIANGLE 598 0 350 400 500 400 2 #FFFFFF

CIRCLE 300 350 41 1 #FFFFFF
RECT 260 340 80 60 1 #FFFFFF
FILL_CIRCLE 300 350 39 #000000
FILL_RECT 261 340 79 60 #000000
CIRCLE 300 350 34 1 #FFFFFF
CIRCLE 300 350 27 1 #FFFFFF
CIRCLE 300 350 20 1 #FFFFFF
FILL_RECT 261 340 79 60 #000000
FILL_RECT 261 340 79 1 #FFFFFF

FILL_TRIANGLE 300 300 450 0 150 0 #000000
TRIANGLE 300 300 450 1 150 1 2 #FFFFFF
FILL_TRIANGLE 75 100 75 0 150 0 #000000
FILL_TRIANGLE 525 100 525 0 450 0 #000000

FILL_RECT 0 300 150 100 #000000
FILL_RECT 450 300 150 100 #000000
FILL_RECT 150 50 300 100 #000000
RECT 150 50 300 100 2 #FFFFFF
FILL_TRIANGLE 300 279 200 100 401 100 #000000

CIRCLE 300 150 56 2 #FFFFFF
CIRCLE 300 150 48 2 #FFFFFF
CIRCLE 300 150 40 2 #FFFFFF
CIRCLE 300 150 32 2 #FFFFFF
CIRCLE 300 150 24 2 #FFFFFF
CIRCLE 300 150 16 2 #FFFFFF

TRIANGLE 300 150 150 50 450 50 1 #FFFFFF
```

## Credits
### Adam Babiar
### Boris Pekarčík
### Lucia Kačmárová
### Marek Skribčák

#### Last updated on April 29th 2023
