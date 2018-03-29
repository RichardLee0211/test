#include<iostream>
#include<vector>
#include<math.h>

using namespace std;
typedef unsigned long ulong;

namespace cs540{
    vector<ulong> gv;
    vector<bool> gb;
    class Primes{
        // TODO: ctor, dtor, iterator, iterator++, iterator--, begin, end, operator*
        // unsigned long
        public:
            /* data */
            ulong size;

            /* function */
            Primes(int n){
                this->size = n;
                for(int i=0; i<=n; ++i){
                    gv.push_back(i);
                    gb.push_back(true);
                }
                for(int i=2; i<=sqrt(n); ++i){
                    if(gb[i] == true){
                        for(int j=pow(i,2); j<n; j+=i){
                            gb[j] = false;
                        }
                    }
                }
                // this->printout();
            }

            /* iterator */
            struct Iterator{
                /* data */
                ulong index;

                /* method */
                Iterator(){
                    this->index = 2;
                }
                Iterator(const Iterator &it){
                    this->index = it.index;
                }
                ~Iterator(){}
                // Iterator(SkipNodeBase<Key_T, Mapped_T>*);
                Iterator& operator=(const Iterator &it){
                    this->index = it.index;
                    return *this;
                }
                Iterator& operator++(){
                    this->index++;
                    while(gb[index] == false)
                        this->index++;
                    return *this;

                }
                Iterator  operator++(int){
                    Primes::Iterator it(*this);
                    this->index++;
                    while(gb[index] == false)
                        this->index++;
                    return it;
                }
                Iterator& operator--(){
                    this->index--;
                    while(this->index != 2 && gb[index] == false)
                        this->index--;
                    return *this;
                }
                Iterator  operator--(int){
                    Primes::Iterator it(*this);
                    this->index--;
                    while(gv[index] != 2 && gb[index] == false)
                        this->index--;
                    return it;
                }
                ulong &operator*() const{
                    return gv[this->index];
                }
                ulong *operator->() const{
                    return &gv[this->index];
                }
                bool operator==(Iterator &rightIt){
                    return this->index == rightIt.index;
                }
                bool operator!=(Iterator &rightIt){
                    return this->index != rightIt.index;
                }
            };

            cs540::Primes::Iterator begin(){
                cs540::Primes::Iterator it;
                it.index = 2;
                return it;
            }

            cs540::Primes::Iterator end(){
                cs540::Primes::Iterator it;
                it.index = this->size;
                return it;
            }



            /* help function */
            void printout(){
                for(ulong i=0; i<size; i++){
                    if(gb[i])
                        cout<<gv[i]<<" ";
                }
            }



    };

}
    bool operator!=(const typename cs540::Primes::Iterator &leftIt,
            const typename cs540::Primes::Iterator &rightIt){
        return leftIt.index != rightIt.index;
    }
    bool operator==(const typename cs540::Primes::Iterator &leftIt,
            const typename cs540::Primes::Iterator &rightIt){
        return leftIt.index == rightIt.index;
    }
