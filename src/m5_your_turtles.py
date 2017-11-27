"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Key.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

Ditzy = rg.SimpleTurtle('turtle')
Ditzy.pen = rg.Pen('purple', 4)
Ditzy.speed = 10

Doopy = rg.SimpleTurtle('turtle')
Doopy.pen = rg.Pen('red', 4)
Doopy.speed = 10

Doy = rg.SimpleTurtle('turtle')
Doy.pen = rg.Pen('green', 4)
Doy.speed = 10

for x in range(100):
    Ditzy.right(90)
    Ditzy.draw_square(100)
    Doopy.left(90)
    Doopy.draw_circle(100)
    Doy.forward(200)
    Doy.right(180)
    Doy.forward(200)
    Doy.left(90)
window.close_on_mouse_click()
