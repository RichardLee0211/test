// 223. Rectangle Area
// https://leetcode.com/problems/rectangle-area/description/
//
#include<assert.h>

int computeArea(int A, int B, int C, int D,
        int A_, int B_, int C_, int D_) {
    assert(A<B && B<D && A_<C_ && B_<D_);
    // no overlap
    if(A_>C || C_<A || B_>D || D_<B)
        return (C-A)*(D-B) + (C_-A_)*(D_-B_);

    // overlap
    int overlapAreaA= (A_<A) ? A : A_;
    int overlapAreaC= (C_<C) ? C_: C ;
    int overlapAreaB= (B_<B) ? B : B_;
    int overlapAreaD= (D_<D) ? D_: D ;
    return (C-A)*(D-B) +
        (C_-A_)*(D_-B_) -
        (overlapAreaC-overlapAreaA)*(overlapAreaD - overlapAreaB);

}
