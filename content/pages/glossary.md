Title: glossary
Slug: glossary
Summary: glossary for the site

# C++ Glossary

Here are some important OOP/C++ terms:

<!-- We can mix markdown and html. Which allows for additional fine tuning -->

*   <a name="abstractclass"><span class="hilight">abstract class</span>:</a> a class with at least one [pure virtual method](#purevirtual) is called abstract, meaning it cannot be instantiated.
*   <a name="assignmentoperator"><span class="hilight">assignment operator</span>:</a> overriding the assignment operator for a class changes what <span class="code">=</span> does when used with members of that class.
*   <a name="baseclass"><span class="hilight">base class</span>:</a> a class that another class inherits from.
*   <a name="big3"><span class="hilight">big 3</span>:</a> the main three elements of copy control: the assignment operator, the copy constructor, and the destructor.
*   <a name="class"><span class="hilight">class</span>:</a> a C++ construct that can hold both data values and functions (called _methods_). It differs from a _struct_ in that the members of a struct are public by default, while members of a class are private by default. In practice, coders most often use <span class="code">struct</span> when they don't intend to write any methods.
*   <a name="compile"><span class="hilight">compile</span>:</a> turning source code into machine code.
*   <a name="constructor"><span class="hilight">constructor</span>:</a> the class method that initializes an object of that class.
*   <a name="copyconstructor"><span class="hilight">copy constructor</span>:</a> the class method that initializes an object of that class _when it is being copied from another instance of that class_.
*   <a name="delegation"><span class="hilight">delegation</span>:</a> giving programming tasks to the lowest-level object that can handle them. For example, if your <span class="code">Department</span> class needs to print <span class="code">Employee</span> objects, it delegates the task to the <span class="code">Employee</span> class, rather than containing code to print them itself.
*   <a name="derivedclass"><span class="hilight">derived class</span>:</a> a class that inherits from another class.
*   <a name="destructor"><span class="hilight">destructor</span>:</a> the class method that cleans up all dynamically allocated resources for an object of that class.
*   <a name="dynamicbinding"><span class="hilight">dynamic binding</span>:</a> means that the language being used decides what method should be called in a particular case at runtime, rather than at compile time. (See [polymorphism](#polymorphism).)
*   <a name="exception"><span class="hilight">exception</span>:</a> a C++ error-handling technique that enables non-local transfers of control.
*   <a name="explicit"><span class="hilight">explicit</span>:</a> a C++ keyword that turns off implicit use of some type conversion.
*   <a name="function"><span class="hilight">function</span>:</a> A "chunk" of executable code that is (typically) given a name and can be invoked (_called_) from many places.
*   <a name="functionprototype"><span class="hilight">function prototype</span>:</a> code that just shows the return type, parameter types, and <span class="code">const</span> status of a function, but does not include the body of the function (what it actually does).
*   <a name="functor"><span class="hilight">functor</span>:</a> an object designed to work like a function. In C++, this is achieved by overloading the <span class="code">()</span> operator.
*   <a name="genericprogramming"><span class="hilight">generic programming</span>:</a> focuses on the creation of data structures and algorithms that can work with many different types. In C++, generic programming is supported by [templates](#template).
*   <a name="heap"><span class="hilight">heap</span>:</a> the area of memory under the direct control of the application. Python manages the heap for the programmer, while C++ gives the programmer direct control over heap allocation.
*   <a name="keyword"><span class="hilight">keyword</span>:</a> one of a number of reserved strings in a language, that can't be used to name functions or variables. In C++, keywords include things like <span class="code">if</span>, <span class="code">while</span>, <span class="code">for</span>, <span class="code">const</span>, <span class="code">virtual</span>, and many more.
*   <a name="lambda"><span class="hilight">lambda</span>:</a> an anonymous function, also called a lexical closure.
*   <a name="linker"><span class="hilight">linker</span>:</a> The program that pulls together several compiled files into a single, executable file.
*   <a name="log_file"><span class="hilight">log file</span>:</a> A place where a program with no interactive user can note errors or other actions taking place.
*   <a name="LSP"><span class="hilight">LSP (Liskov Substitution Principle)</span>:</a> One should be able to substitute an instance of a derived class wherever an instance of a base class is called for.
*   <a name="memo-ization"><span class="hilight">memo-ization</span>:</a> storing results in some data structure rather than calculating them again and again.
*   <a name="multipleinheritance"><span class="hilight">multiple inheritance</span>:</a> when a derived class inherits from more than one base class.
*   <a name="nan"><span class="hilight">NaN</span>:</a> a floating point value meaning the result of some calculation is "Not a Number": see [NaN](https://en.wikipedia.org/wiki/NaN).
*   <a name="overloading"><span class="hilight">overloading</span>:</a> to create more than one function or operator with the same name, but a different type signature. For instance, <span class="code">+</span> can add two integers, but it can also add two doubles or two strings.
*   <a name="overriding"><span class="hilight">overriding</span>:</a> is to create a method in a derived class that replaces the behavior of a method with the same name and arguments in its parent class.
*   <a name="passbyreference"><span class="hilight">pass-by-reference</span>:</a> a way of passing an argument to a function that gives the function direct access to the object being passed.
*   <a name="passbyvalue"><span class="hilight">pass-by-value</span>:</a> passing an argument to a function by copying the object used and handing the funciton only a copy of its value, not access to the original object.
*   <a name="pointer"><span class="hilight">pointer</span>:</a> a variable that holds a memory address. In C++, pointers are typed.
*   <a name="polymorphism"><span class="hilight">polymorphism</span>:</a> also called "dynamic binding." Polymorphism describes the ability, present in some languages, to accept a pointer or reference to a base-type object, and yet successfully invoke the proper method in a derived-class object being referenced. In C++, polymorphism can be turned on by using the reserved word <span class="code">virtual</span> on a method in a class.
*   <a name="preprocessor"><span class="hilight">preprocessor</span>:</a> the program that runs before the compiler and handles <span class="code">#include</span> and <span class="code">#define</span> directives.
*   <a name="purevirtual"><span class="hilight">pure virtual method</span>:</a> a method with the "body" <span class="code">= 0</span>, used to indicate that only descendants that supply that method can actually be created.
*   <a name="rangedforloop"><span class="hilight">ranged for loop</span>:</a> similar to Python's for-each loop. It iterates through each element of a collection without any explicit indexing.
*   <a name="reference"><span class="hilight">reference</span>:</a> a "smarter" pointer-like object that is de-referenced each time it is used.  
    [More on C++ references](https://en.wikipedia.org/wiki/Reference_(C%2B%2B)).
*   <a name="slicing"><span class="hilight">slicing</span>:</a> what occurs when an instance of derived class B is assigned to a variable of base class A. The data members of B that are not in A get "sliced" off.
*   <a name="stack"><span class="hilight">stack</span>:</a> the area of memory managed by the run-time system. New "stack frames" are pushed onto the stack each time a new function call is made, and they include space for the function's parameters, local variables, and its return value.
*   <a name="staticbinding"><span class="hilight">static binding</span>:</a> decides what method should be called in a particular case when compiling, rather than at runtime.
*   <a name="statictyping"><span class="hilight">static typing</span>:</a> the assignment of a type to a variable once, at compile time, rather than _dynamically_, at run time.
*   <a name="stl"><span class="hilight">Standard Template Library (STL)</span>:</a> A collection of templatized collections and algorithms that come with every C++ implementation.
*   <a name="string"><span class="hilight">string</span>:</a> The C++ type that holds text.
*   <a name="struct"><span class="hilight">struct</span>:</a> A C++ construct that can hold both data values and functions (called _methods_). It differs from a _class_ in that the members of a struct are public by default. In practice, coders most often use <span class="code">struct</span> when they don't intend to write any methods.
*   <a name="structured_programming"><span class="hilight">structured programming</span>:</a> a programming concept that suggests the clarity and reliability of programs can be enhanced by relying on control-flow managers such as _if_ statements and _while_ loops.
*   <a name="template"><span class="hilight">template</span>:</a> a machine that produces classes or functions when passed a concrete type. It enables C++ support for [generic programming](#genericprogramming).
*   <a name="vector"><span class="hilight">vector</span>:</a> in C++, a class in the _Standard Template Library_ that allows random, constant-time access to a collection of items of some specific type, and holds those items in a determinate order.
*   <a name="virtual"><span class="hilight">virtual</span>:</a> in C++, this keyword turns on [polymorphism](#polymorphism) .