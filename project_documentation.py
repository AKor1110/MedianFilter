'''
--------------------------------------------------------------------------------
Author: Andy Kor
Date: 2/1/17
Program Purpose: Create a median filter using Python library PIL.
--------------------------------------------------------------------------------

~~~The Complexity~~~
--------------------------------------------------------------------------------
    There are two different files that are optimized in different ways.
    project_1.py is O(n^2) and runs in around 4 seconds, and is made at this
    complexity for the convenience of easy to read code and comprehensibility.
    project_1.1.py is O(n) and runs in around .05 seconds, and is made like this
    simply for the speed of the program.
--------------------------------------------------------------------------------

~~~The Class~~~
--------------------------------------------------------------------------------
    I made the class so that the program could be a little more coherent and
    dynamic. Typically, classes are made so that changes could be made easily
    without being too tedious. In my case, I did it just to practice coding
    modularly.
--------------------------------------------------------------------------------
    
~~~The Init Function~~~
--------------------------------------------------------------------------------
    In this function, I hardcoded the picture file names, just to deal with
    "ambiguity." I put all the file names in a list and took indices of that 
    list to be used accordingly. This function also stores two variables that
    store width and height concerning the picture dimensions.
--------------------------------------------------------------------------------

~~~The Pixels Function~~~
--------------------------------------------------------------------------------
    This creates a list of all pixel coordinates using the width and height 
    from the picture data and stored it all in a list. This sums up to almost
    300,000 items in the list.
--------------------------------------------------------------------------------
    
~~~The ImagesRGB Function~~~
--------------------------------------------------------------------------------
    Primarily, I called the Pixels function to use the list of coordinates.
    I then initialized an empty list called "rgb," where all the rgb value of
    each pixel of each picture is stored in a nested list. I then opened all the
    picture files and converted its data into rgb values instead of coordinates.
    I then looped through all the coordinates of each picture, and stored the
    rgb values at that pixel of each picture into a list. Finally, I returned
    the list of rgb values.
--------------------------------------------------------------------------------

~~~The PixelAverage Function~~~
--------------------------------------------------------------------------------
    First, I called the ImagesRGB function so that I can use the list of rgb
    values. Then I initialized an empty list called "rgb_average" which will be
    used to store all median rgb values for every pixel. I have a nested for
    loop that first loops through all lists of rgb values, then loops through
    each tuple in the list.  Each sublist corresponds to the pixel coordinates.
    In the first loop, I initialized 3 lists: r,g, and b, which will all be 
    reset after the tuples in each list are evaluated. In the second loop,
    I append each value of each tuple into seperate lists. The lists are then
    sorted, and I grab the "median" of each list and create a tuple from each
    list into the rgb_average list. I then return the list to be used.
--------------------------------------------------------------------------------

~~~The MakePicture Function~~~
--------------------------------------------------------------------------------
    In this function, I called the PixelAverage function, then initialized a
    new image, using PIL's Image class.  I then put all the rgb data into the 
    empty image, because the rgb data was evaluated by row, it all works out
    fine.  I then save the image as a new file. Voila! It is done.
--------------------------------------------------------------------------------

'''