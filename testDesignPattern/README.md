Design Pattern
================================================================================

this is from youtuber Christopher Okhravi
and the book, "header first design pattern"
C++ code available in
	url = https://github.com/yaocoder/DesignPattern

Good resource: https://github.com/JakubVojvoda/design-patterns-cpp

and the book: Design Patterns: Elements of Reusable Object-Oriented Software (1994)

motivation: I learning how to code C++ in CS540, but don't know how to do good
design of Code

### SOLID OOP principles:
https://en.wikipedia.org/wiki/SOLID

- Single responsibility principle[6]
A class should have only a single responsibility, that is, only changes to one part of the software's specification should be able to affect the specification of the class.

- Open–closed principle[7]
"Software entities ... should be open for extension, but closed for modification."

- Liskov substitution principle[8]
"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program." See also design by contract.

- Interface segregation principle[9]
"Many client-specific interfaces are better than one general-purpose interface."[4]

- Dependency inversion principle[10]
One should "depend upon abstractions, [not] concretions."[4]

Strategy pattern:
--------------------------------------------------------------------------------
problem it solve: inheritance and code reuse problem
a good reference: https://www.geeksforgeeks.org/strategy-pattern-set-1/
```from wiki
    In computer programming, the strategy pattern (also known as the policy pattern)
    is a behavioral software design pattern that enables selecting an algorithm at
    runtime. The strategy pattern
    - defines a family of algorithms,
    - encapsulates each algorithm, and
    - makes the algorithms interchangeable within that family.
```
one thing I don't like about this code is that have to setStrategy at runtime

But we could setStrategy according to data

Observer pattern
--------------------------------------------------------------------------------
from: https://www.geeksforgeeks.org/observer-pattern-set-1-introduction/
defination:
The Observer Pattern defines a one to many dependency between objects so that
one object changes state, all of its dependents are notified and updated
automatically.

I think UML is  one level higher than actual code, and how to log it

### example

singleton
--------------------------------------------------------------------------------

making concrector private

here: https://www.geeksforgeeks.org/singleton-design-pattern/
```java
    // Classical Java implementation of singleton
    // design pattern
    class Singleton
    {
        private static Singleton obj;

        // private constructor to force use of
        // getInstance() to create Singleton object
        private Singleton() {}

        public static Singleton getInstance()
        {
            if (obj==null)
                obj = new Singleton();
            return obj;
        }
    }
```

thread safe
```java
    // Thread Synchronized Java implementation of
    // singleton design pattern
    class Singleton
    {
        private static Singleton obj;

        private Singleton() {}

        // Only one thread can execute this at a time
        public static synchronized Singleton getInstance()
        {
            if (obj==null)
                obj = new Singleton();
            return obj;
        }
    }
```
... more about in that website, java thread safe

TODO: this is many discuss here
Singleton discussed in stackoverflow here:
https://stackoverflow.com/questions/1008019/c-singleton-design-pattern

TODO:
a paper talk about C++ and the Perils of Double-Checked Locking
scott Meyers and Andrei Alexandrescu, September 2004
```cpp
    // from the header file
    class Singleton{
    public:
        static Singleton* instance();
        // ...
    private:
        static Singleton* pInstance;
    };

    // from the implementation of file
    Singleton* Singleton::pInstance = 0;

    Singleton* Singleton::instance(){
        if(pInstance == 0){
            pInstance = new Singleton;
        }
        return pInstance;
    }
```

```cpp
    Singleton* Singleton::instance(){
        Lock lock; // acquire lock(params omitted for simplicity)
        if(pInstance == 0)
            pInstance = new Singleton;
        return pInstance;
    }           // release lock(via Lock destructor)
```


```cpp
    Singleton* Singleton::instance(){
        if(pInstance == 0){                 // 1st test
            Lock lock;
            if(pInstance == 0){
                pInstance = new Singleton;  // 2nd test
            }
        }
        return pInstance;
    }
```


Decorator pattern
--------------------------------------------------------------------------------
interesting but not so useful case out there

- pizza and toping scenario
- coffee and addon

Factory Pattern
--------------------------------------------------------------------------------

### Factory Method

### Abstract Factory

UI: light theme and dark theme, using abstract factory to product UI component
good UML graph

command Pattern
--------------------------------------------------------------------------------

this is very good read
https://en.wikipedia.org/wiki/Command_pattern

In each of these examples, notice how the Command pattern decouples the object that invokes the operation from the one having the knowledge to perform it.

unexcute()

batch

Adapter Pattern
--------------------------------------------------------------------------------

Facade Pattern
--------------------------------------------------------------------------------
face

Proxy Pattern
--------------------------------------------------------------------------------

Iterator Pattern
--------------------------------------------------------------------------------
don't really understand

TODO: to be continue. I got some feelings about design pattern,
reference to GoF book, and wikipedia and more code, come back later

others
--------------------------------------------------------------------------------

you don't really understand the concept unless you code it
want to draw UML in latex and markdown(the markdown standard doesn't support
drawing pictures. So insert pictures instead)

so far, I don't see the really good example, as most of them has flaws
