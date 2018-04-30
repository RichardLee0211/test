#include<iostream>
template< typename First, typename Rest >
struct cons
{
    typedef First first;
    typedef Rest rest;
};
struct nil {};
typedef
cons<int, cons< long, cons< std::vector<double>, nil> > > my_types;

// choose the larger of two types
template<typename T1,
    typename T2,
    bool choose1 = (sizeof(T1) > sizeof(T2)) // hands off!
    >
struct choose_larger
{
    typedef T1 type;
};
//
// specialization for the case where sizeof(T2) >= sizeof(T1)
template< typename T1, typename T2 >
struct choose_larger< T1,T2,false >
{
    typedef T2 type;
};
// get the largest of a cons-list
template< typename T > struct largest;

// specialization to peel apart the cons list
template< typename First, typename Rest >
struct largest< cons<First,Rest> >
: choose_larger< First, typename largest<Rest>::type >
{
    // type inherited from base
};

// specialization for loop termination
template< typename First >
struct largest< cons<First,nil> >
{
    typedef First type;
};

int main() {
    // print the name of the largest of my_types
    std::cout
        << typeid(largest<my_types>::type).name()
        << std::endl
        ;
}
