#include<boost/statechart/event.hpp>
#include<boost/statechart/state_machine.hpp>
#include<boost/statechart/simple_state.hpp>

#include<ctime>
#include<iostream>

namespace sc = boost::statechart;

struct IElapsedTime{
    virtual double ElapsedTime() const = 0;
};

// TODO: this is a wired design for me, pass class to super class template
struct EvStartStop : sc::event< EvStartStop > {};
struct EvReset : sc::event< EvReset > {};

struct Active;
struct StopWatch : sc::state_machine< StopWatch, Active > {
    double ElapsedTime() const {
        return state_cast< const IElapsedTime &> ().ElapsedTime();
    }
};

struct Stopped;

struct Active : sc::simple_state<Active, StopWatch, Stopped> {
    // error, doesn't have transition class template in version 106600
    // typedef sc::transition<EvReset, Active> reactions;

    Active() : elapsedTime_( 0.0 ) {}
    double ElapsedTime() const { return elapsedTime_; }
    double &ElapsedTime() { return elapsedTime_; }
private:
    double elapsedTime_;
};

// maybe, simeple_state<subclassname, parentclassname>
struct Running : IElapsedTime, sc::simple_state<Running, Active> {
    // typedef sc::transition<EvStartStop, Stopped> reactions;
    Running() : startTime_( std::time(0) ) {}
    ~Running(){
        context<Active> ().ElapsedTime() = ElapsedTime();
            // std::difftime( std::time(0), startTime_ );
    }
    virtual double ElapsedTime() const{
        return context< Active >().ElapsedTime() +
            std::difftime(std::time( 0 ), startTime_);
    }
private:
    std::time_t startTime_;
};
struct Stopped : IElapsedTime, sc::simple_state<Stopped, Active> {
    // typedef sc::transition<EvStartStop, Running> reactions;
    virtual double ElapsedTime() const{
        return context<Active>(). ElapsedTime();
    }
};

int main(){
    StopWatch myWatch;
    myWatch.initiate();
    std::cout<<myWatch.ElapsedTime()<<"\n";
    myWatch.process_event( EvStartStop() );
    std::cout<<myWatch.ElapsedTime()<<"\n";
    myWatch.process_event( EvStartStop() );
    std::cout<<myWatch.ElapsedTime()<<"\n";
    myWatch.process_event( EvStartStop() );
    std::cout<<myWatch.ElapsedTime()<<"\n";
    myWatch.process_event( EvStartStop() );
    std::cout<<myWatch.ElapsedTime()<<"\n";
    myWatch.process_event( EvReset() );
    std::cout<<myWatch.ElapsedTime()<<"\n";
    return 0;
}
