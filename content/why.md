Title: Why bother studying a "hard" language like C++?
Date: 2-14-2020
Slug: why
Summary: Article for why study C++
Article_num: 1
<!-- ^^^ This is a custom metadata used to force pelican to order the articles in a certan way -->
<!-- Must be indicated within the config files. *conf.py -->


<!-- Start of article content -->

# Why Study C++?

<!-- Rendered with <p> -->
Given how much easier things are likely to seem to you in a language
like Python, why should we bother learning a "hard" language like C++?
Here are some reasons:

<!-- Rendered as <ul> and <li> -->
* "Easy" languages like Python are usually implemented in 
    "harder" languages like C++. (The main Python implementation
    is [CPython](https://en.wikipedia.org/wiki/CPython),
    written in C.) Thus, to fully understand the easy languages,
    one must undersand the hard languages!

* A language like C++ also has many practical applications:
    it is dominant in the game industry, where performance is
    crucial, and is used extensively in embedded systems
    (such as the [Mars Rover](https://youtu.be/3SdSKZFoUa8)), and in the finance industry, in real-time
    trading software.

* Studying C++ aids in grasping many fundamental programming
    concepts, such as memory allocation, pass-by-value versus
    pass-by-reference, pointers, and how types are actually
    implemented.

* C++ is a compiled language. Seperating the compile time from the run time would help you catch many errors at the compile time, so the program is less likely to crash while running. Moreover, the compiler translates the C++ code to the machine code. It tells the machine what function to call. The machine thus do not need to sacrifice the performance to figure out what function to run at the runtime. C++ also enforces the static typing. It helps you catch type mismatches sooner at comile time.

* No memory management: Unlike Java and Python, C++ does not have the garabage collector. To allocate memory on the heap, you as the programmer has to take the responsibility to delete yourself. It gives your control over the memory management system. So your program does not sacrifice the performance. However, it also comes with a price. You would possibly run into memory leak. C++ is like driving a car with a manual transimission. If you just drive a normal car, you might think it is difficult to control the car. But if you are a race car driver, you probably want it to be manual to have more control over the car to maximize the performance. 