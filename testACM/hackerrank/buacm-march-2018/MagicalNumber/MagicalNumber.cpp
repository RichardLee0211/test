/*
 * from the hakcerrank
 * when lower digits is greater than higher digits, doesn't matter
 * otherwise, decrease the higher digits by one, and change lower digits to 9
 * TODO: how to write design document??
 */
#include<iostream>
#include<vector>
#include<cassert>

using namespace std;

// enum eDigit{ZERO=0, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE};
// eDigit type is comparable
//
struct Digit{
    int digit;

    Digit(int n){
        assert(n<10 && n>=0);
        digit = n;
    }

    friend bool operator>= (Digit &l, Digit &r){
        return l.digit >= r.digit;
    }
    Digit operator++(int){
        digit++;
        return *this;
    }
    Digit operator--(int){
        digit--;
        return *this;
    }

};

struct MagicNumber{
    vector<Digit> num;

    MagicNumber(int n){
        while(n != 0){
            int digit = n%10;
            num.push_back(Digit(digit));
            n /= 10;
        }
        if(num.size() == 1) return;
        for(int i=0; i<(int)num.size()-1; ++i){
            if(num[i]>=num[i+1]) continue;
            // decrease the number, and num[i+1] counldn't be 0
            num[i+1]--;
            for(int j=i; j>=0; --j)
                num[j] = 9;
        }
    }
    friend ostream &operator<<(ostream &os, MagicNumber& n){
        bool headingZeros = true;
        for(int i=n.num.size()-1; i>=0; --i){
            if(n.num[i].digit == 0 && headingZeros == true) continue;
            headingZeros = false;
            os<<n.num[i].digit;
        }
        if(headingZeros == true) os<<"0";
        return os;
    }
};

int main(){
    int testCaseLength = 0;
    cin>>testCaseLength;
    while(--testCaseLength>=0){
        int tmp;
        cin>>tmp;
        MagicNumber mn(tmp);
        cout<<mn<<endl;

    }
}
