Title: code
Slug: code
Summary: Code page on main menu

# C++ Code Examples

The following code examples have been developed to help students studying object-oriented programming in C++. They are listed _roughly_ in the order a student will encounter these topics in learning C++ -- "roughly" because the exact order will always depend upon the student, the teacher, the textbook, and so on.

First of all, we have written a script to turn our C++ code into web pages. This first section will feature the code that has been converted (note that the formatting still needs improvement):

*   [A "Thing" class,](thing.html)  
    used to demonstrate <span class="hilight">pointers</span> and <span class="hilight">memory management</span>.
*   [A complex number class,](complex.html)  
    used to demonstrate <span class="hilight">operator over-loading</span>.
*   [A class hierarchy of images](image.html)  
    This illustrates <span class="hilight">inheritance</span>, <span class="hilight">overriding</span>, the use of the <span class="hilight">virtual</span> keyword, and a <span class="hilight">pure virtual</span> class. It also uses memory allocation and freeing.
*   [Testing out the Standard Template Library](stl.html)  
    The Standard Template Library is how C++ enables [Generic Programming](https://en.wikipedia.org/wiki/Generic_programming).
*   [Recursion examples](recursion.html)
*   [Convert into "any" base](base_conv.html)  
    This code uses <span class="hilight">recursion</span> to strip off digits one-by-one. It is called in the recursion examples code above.
*   [Functors](functors.html)  
    Shows a trivial and a more advanced use of a functor.
*   [Vector Experiments](vector_experiments.html)  
    Code that explores various aspects of the STL vector class.

* * *

And beyond this point, we have "raw" code files, although nicely formatted by GitHub:

*   [Hello World!](https://github.com/gcallah/OOP2/blob/master/code/misc/hello.cpp)  
    The paradigmatic first program to write in any language you are seeking to learn.
*   [Hello [YourName]!](https://github.com/gcallah/OOP2/blob/master/code/misc/hello_nm.cpp)  
    How to get input from the user, and then use that in your output.
*   [C++ function calls](https://github.com/gcallah/OOP2/blob/master/code/misc/funcs.cpp)  
    Explore the various ways (<span class="hilight">pass-by-value</span> and <span class="hilight">pass-by-reference</span>) we can pass values to a C++ function and get a result returned from that function.
*   [Using vectors](https://github.com/gcallah/OOP2/blob/master/code/misc/mean.cpp)  
    Entering values into a <span class="code">vector</span> then getting the mean of all values in the vector.
*   [Python loop over a vector](https://github.com/gcallah/OOP2/blob/master/code/misc/PythonListExploration.ipynb)  
    For comparison to the similar C++ loop.
*   [Creating a new type using <span class="code">struct</span>](https://github.com/gcallah/OOP2/blob/master/code/misc/complex_struct.cpp)
*   [Turning the <span class="code">struct</span> into a class.](https://github.com/gcallah/OOP2/blob/master/code/misc/complex.cpp)  
    This file is also used to demonstrate <span class="hilight">operator over-loading</span>.
*   [Implementing a class like <span class="code">vector</span> on our own.](https://github.com/gcallah/OOP2/blob/master/code/vector/my_vec.cpp)  
    Here we do more <span class="hilight">operator over-loading</span>, including the <span class="code">[]</span> operator.
*   [Passing a derived class to a function expecting the base class.](https://github.com/gcallah/OOP2/blob/master/code/mics/base_by_val.cpp)  
    Exploring <span class="hilight">polymorphism</span> and the <span class="hilight">virtual</span> keyword.
*   [Now let's make turn own <span class="code">vector</span> into a generic machine for creating vectors.](https://github.com/gcallah/OOP2/blob/master/code/vector/templ_vec.cpp)  

*   [Code for gathering weather data.](https://github.com/gcallah/OOP2/tree/master/code/weather)  
    (The numbered files are various iterations of the program.)  
    Within this program, particular classes / files address particular C++ features:  

    *   Copy control: Allocating and freeing memory.  
        <span class="hilight">Code examples:</span>  
        [image.cpp](https://github.com/gcallah/OOP2/blob/master/code/weather/image.cpp) allocates a buffer for its image, and uses <span class="hilight">copy control</span> to manage that buffer properly.
    *   Multiple compilation units.  
        <span class="hilight">Code examples:</span>  
        The entire project illustrates breaking code into <span class="hilight">separate compilation units</span>.
    *   Class heirarchies.  
        <span class="hilight">Code examples:</span>  
        Both [image.h](https://github.com/gcallah/OOP2/blob/master/code/weather/image.h) and [rawdata.h](https://github.com/gcallah/OOP2/blob/master/code/weather/rawdata.h) create a <span class="hilight">class heirarchy</span>, which uses <span class="hilight">inheritance</span>.
    *   <span class="hilight">Polymorphism</span> and <span class="hilight">virtual functions</span>.  
        <span class="hilight">Code examples:</span> <a href="">test_image.cpp</a> is designed to illustrate [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)). We can create a <span class="code">vector</span> of <span class="code">Image</span> pointers, and expect that right sub-class method to be called if we ask to <span class="code">display()</span> one of them, so long as <span class="code">display</span> is declared <span class="code">virtual</span> in the base (Image) class.
    *   How <span class="hilight">polymorphism</span> interacts with <span class="hilight">copy control</span>.  
        <span class="hilight">Code examples:</span>  
        [rawdata.h](https://github.com/gcallah/OOP2/blob/master/code/weather/rawdata.h) and [rawdata.cpp](https://github.com/gcallah/OOP2/blob/master/code/weather/rawdata.cpp) aloong with their test harness [test_rawdata.cpp](https://github.com/gcallah/OOP2/blob/master/code/weather/test_rawdata.cpp) , are built to illustrate this theme.