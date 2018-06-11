this is from youtuber Christopher Okhravi
and the book, "header first design pattern"
C++ code available in
	url = https://github.com/yaocoder/DesignPattern

motivation: I learning how to code C++ in CS540, but don't know how to do good
design of Code

## Strategy pattern:
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

## Observer pattern
from: https://www.geeksforgeeks.org/observer-pattern-set-1-introduction/
defination:
The Observer Pattern defines a one to many dependency between objects so that
one object changes state, all of its dependents are notified and updated
automatically.

I think UML is  one level higher than actual code, and how to log it

### example

## singleton
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

Singleton discussed in stackoverflow here: TODO: this is many discuss here
https://stackoverflow.com/questions/1008019/c-singleton-design-pattern
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
TODO: how to hardware interrupt interrupt a process in xv6
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

wired stuff, when I edit a pdf file in mac and send it to Ubuntu, what edit part
is missing and print out nothing

## Decorator pattern
pizza and toping scenario

TODO: to be continue

## others
you don't really understand the concept unless you code it
want to draw UML in latex and markdown(the markdown standard doesn't support
drawing pictures. So insert pictures instead)
