typedef struct _my{
    int i;
    double j;
}my;

int helper(const my& i){
    return i.i;
}

int helper2(my const & i){
    return i.i;
}

int main(){
}
