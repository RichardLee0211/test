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
    double i;
    i = get_log_page_size();
    // i = get_vaddr_pagenum(2);
    return i;
}
