#include<cstdio>
#include<vector>
#include<algorithm>

#include<stdlib.h>
class Node{
    int target;
    Node* lp;
    Node* rp;
};

void foo(int target, const std::vector<int> &C){
    int i;
    for(i=0; i<int(C.size()); i++){
        if(C[i]>target)
            break;

        if(C[i] == target || target%C[i] ==0 ){
            printf("TRUE\n");
            exit(0);
        }
        foo(target-C[i], C);
    }
    return ;
}


int main(){
    int N;
    int target;
    scanf("%d %d", &N, &target);

    std::vector<int> C; C.reserve(N);
    int tmp;
    for(int i=0; i<N; i++){
        scanf("%d", &tmp);
        C[i] = tmp;
    }

    std::sort(C.begin(), C.end());
    int delta;
    for(int i=0; i<N-1; i++){
        delta = C[i+1] - C[i];
        C.push_back(delta);
    }

    std::unique(C.begin(), C.end());
    std::sort(C.begin(), C.end());

    if(*(C.end()-1) == 1){
        printf("TRUE\n");
        return 0;
    }

    if(C[0]>target){
        printf("FALSE\n");
        return 0;
    }

    foo(target, C);

    printf("FALSE\n");

}
