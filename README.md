# Tertris
Terminal-based clone of the [Tetris' NES version](https://tetris.wiki/Tetris_(NES,_Nintendo)).


## LOOK:
![Example of look - if not show look at informations/social preview.png](information/social%20preview.png)


## HOW TO USE IT ?
1. Go to the [releases page](https://github.com/VMoM/Tertris/releases)
2. Chose a release (prefer the latest)
3. Follow the guide of the release you chose


## LANGUAGE:
- User interface and code are in english.
- Comments are only in French for the time being (maybe an English version will come later).


## DISCLAIMERS
- Tertris uses the [curses library](https://en.wikipedia.org/wiki/Curses_(programming_library)) for Python 3 to print it interface, so **it can only run in Unix-based OS**.
- Tertris is still in progress, so some features (such as level counting) may not being implemented.
- Since in the Python 3's version of the curses module the class `_CursesWindow` is private, I had to declare them as objects. In result, your IDE will cry blood if you open `View.py`. 

## OTHER LINKS:
- The [official Tetris website](https://tetris.com/).
- The [Wikipedia's page of the Tetris' guideline](https://tetris.wiki/Tetris_Guideline) that I will try to follow (this is only partially the case now).
- The [curses' how to use guide](https://docs.python.org/3/howto/curses.html) I used.
- The [official GitHub page of Tertris](https://github.com/vmom/tertris).
