// #include<math.h>

#include"macros.h"

#if 0
 get_vaddr_pagenum(int addr){
    return VADDR_PAGENUM(addr);
}
#endif

double get_log_page_size(){
    return LOG_PAGE_SIZE;
}

int main(){
    int test = 0x07;
    CLEAR_BIT(test, USED);
    int test2 = !(BIT_MASK(USED)); // test2 = 0
    return test2;
}
