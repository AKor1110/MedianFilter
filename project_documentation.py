'''
--------------------------------------------------------------------------------
Author: Andy Kor
Date: 2/1/17
Program Purpose: Create a median filter using Python library PIL.
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
    In this function, I initialized several variables that correspond to 
    dimensions of the pictures. This way, any list of files that is passed
    through the class is generalized and easy to reuse.
--------------------------------------------------------------------------------
    
~~~The ImagesRGB Function~~~
--------------------------------------------------------------------------------
    Primarily, I created a list with all coordintes possible, then I opened and 
    loaded all the files. I couldn't really make this very modular, so I 
    hardcoded it instead where I have an idea of the length of the list, and 
    that the images are sorted. This leaves room for ambiguity as well as some 
    knowledge of what is happening. I use list comprehension to put a list of 
    lists of RGB values where each sublist represents a pixel, and each sublist 
    contains 9 RGB tuples, representative of each image. I then return the 
    big list.
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

~~~Outisde Of The Class~~~
--------------------------------------------------------------------------------
    Outisde of the class, I used a for loop to get all of the files in the 
    current directory and appended them all in a list to be used in the class
    call. This assumes that all files are "png" and the name begins with a 
    number. I call the class through the variable "Filter," then call the
    instance of the class "MakePicture," which utilizes the other functions and
    results in the final picture.
--------------------------------------------------------------------------------
'''