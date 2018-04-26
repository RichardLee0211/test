#include<boost/version.hpp>

#include<boost/statechart/state_machine.hpp>
#include<boost/statechart/simple_state.hpp>

#include<iostream>

namespace sc = boost::statechart;

struct Greeting;

struct Machine : sc::state_machine< Machine, Greeting > {};

struct Greeting : sc::simple_state< Greeting, Machine> {
    Greeting() { std::cout<<"Hello World!\n"; } // entry
    ~Greeting() { std::cout<<"Bye Bye World~\n"; } // exit
};

int main(){
    std::cout<<BOOST_VERSION<<std::endl; // output 106600
    Machine myMachine;
    myMachine.initiate();
    return 0;
}
