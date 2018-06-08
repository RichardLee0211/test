// this is from boost_MSM_tutorial.pdf

#include<boost/statechart/event.hpp>
#include<boost/statechart/state_machine.hpp>
#include<boost/statechart/simple_state.hpp>
#include<boost/statechart/transition.hpp>

#include<iostream>
#include<ctime>

namespace sc = boost::statechart;

/*
*/
struct IElapsedTime{
    virtual double ElapsedTime() const = 0;
};

struct EvStartStop : sc::event<EvStartStop> {
    EvStartStop() { std::cout<<"do EvStartStop\n"; }
};
struct EvReset : sc::event<EvReset> {
    EvReset() { std::cout<<"do EvReset\n"; }
};

/* forward declare */
struct Active;
struct Stopped;
struct Running;

struct StopWatch : sc::state_machine<StopWatch, Active> {
    StopWatch() { std::cout<<"StopWatch Mechine ctor\n"; }
    ~StopWatch() { std::cout<<"StopWatch Mechine detor\n"; }

    /* TODO: what's this method do??
    */
    double ElapsedTime() const{
        return state_cast<const IElapsedTime &>().ElapsedTime();
    }
};

struct Active : sc::simple_state< Active, StopWatch, Stopped> {
    typedef sc::transition<EvReset, Active> reaction;
    Active() : elapsedTime_(0.0) { std::cout<<"\tAvtive enter\n"; }
    ~Active() {
        std::cout<<"\tActive exit\n";
        std::cout<<"\t\ttotal time: "<<this->elapsedTime_<<std::endl;
    }

    double ElapsedTime() const { return elapsedTime_; }
    double &ElapsedTime() { return elapsedTime_; }

private:
    double elapsedTime_;
};

struct Stopped : IElapsedTime, sc::simple_state<Stopped, Active> {
    typedef sc::transition<EvStartStop, Running> reactions;
    Stopped() { std::cout<<"\t\tStopped enter\n"; }
    ~Stopped() { std::cout<<"\t\tStopped exit\n"; }

    virtual double  ElapsedTime() const{
        return context<Active>().ElapsedTime();
    }
};
struct Running : IElapsedTime, sc::simple_state<Running, Active> {
    typedef sc::transition<EvStartStop, Stopped> reactions;
    Running() : startTime_( std::time(0) ) { std::cout<<"\t\tRuning enter\n"; }
    ~Running() {
        std::cout<<"\t\tRuning exit\n";
        std::cout<<"\t\ttime: "<<startTime_<<std::endl;
        // context<Active>().ElapsedTime() += std::difftime( std::time(0), startTime_);
        context<Active>().ElapsedTime() = ElapsedTime();
        // std::cout<<"\t\ttotal time: "<<context<Active>().ElapsedTime()<<std::endl;
    }
    virtual double ElapsedTime() const{
        return context<Active>().ElapsedTime() + std::difftime(std::time(0), this->startTime_);
    }
private:
    std::time_t startTime_;
};

int main(){
    StopWatch myWatch;
    myWatch.initiate();
    std::cout<< myWatch.ElapsedTime() <<"\n";
    myWatch.process_event( EvStartStop() );     // running ctor
    sleep(1);
    std::cout<< myWatch.ElapsedTime() <<"\n";
    myWatch.process_event( EvStartStop() );
    myWatch.process_event( EvStartStop() );     // running
    sleep(1);
    std::cout<< myWatch.ElapsedTime() <<"\n";
    myWatch.process_event( EvStartStop() );
    myWatch.process_event( EvStartStop() );     // running
    sleep(1);
    std::cout<< myWatch.ElapsedTime() <<"\n";
    myWatch.process_event( EvReset() );
    return 0;
}
// notes:
// how to record time in C++ ?: startTime_ is variable and don't change along
// the time, but std::time(0) is current time based on 1970
