image black = "#000" #Black Background
image white = "#ffffff" #White Background
image image_1 = "intro/media_a.jpg" #img1
image image_2 = "intro/media_b.jpg" #img2

#Transformation for image
transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

#Transformation for background
transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show image_1 at transform_logo
    $ renpy.pause(6, hard=True)

    hide image_1
    $ renpy.pause(2, hard=True)

    show image_2 at transform_logo
    $ renpy.pause(6, hard=True)

    hide image_2
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)

    $ renpy.movie_cutscene('images/intro/opening.mpg')

    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)
    return
