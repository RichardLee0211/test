// from https://www.boost.org/doc/libs/1_67_0/libs/msm/doc/HTML/ch01.html

class player : public state_machine<player>
{
    // The list of FSM states
    enum states { Empty, Open, Stopped, Playing, Paused , initial_state = Empty };

    // transition actions
    void start_playback(play const&) { std::cout << "player::start_playback\n"; }
    void open_drawer(open_close const&) { std::cout << "player::open_drawer\n"; }
    // void store_cd_info()
    // more transition actions
    // ...
    typedef player p; // makes transition table cleaner
    struct transition_table : mpl::vector11<
            //    Start     Event        Target      Action
            //   +---------+------------+-----------+---------------------------+
            row< Stopped , play       ,  Playing  , &p::start_playback        >,
            row< Stopped , open_close ,  Open     , &p::open_drawer           >,
            //   +---------+------------+-----------+---------------------------+
            row< Open    , open_close ,  Empty    , &p::close_drawer          >,
            //   +---------+------------+-----------+---------------------------+
            row< Empty   , open_close ,  Open     , &p::open_drawer           >,
            row< Empty   , cd_detected,  Stopped  , &p::store_cd_info         >,
            //   +---------+------------+-----------+---------------------------+
            row< Playing , stop       ,  Stopped  , &p::stop_playback         >,
            row< Playing , pause      ,  Paused   , &p::pause_playback        >,
            row< Playing , open_close ,  Open     , &p::stop_and_open         >,
            //   +---------+------------+-----------+---------------------------+
            row< Paused  , play       ,  Playing  , &p::resume_playback       >,
            row< Paused  , stop       ,  Stopped  , &p::stop_playback         >,
            row< Paused  , open_close ,  Open     , &p::stop_and_open         >
            //   +---------+------------+-----------+---------------------------+
            > {};
    // Replaces the default no-transition response.
    template <class Event>
        int no_transition(int state, Event const& e)
        {
            std::cout << "no transition from state " << state << " on event " << typeid(e).name() << std::endl;
            return state;
        }
};
