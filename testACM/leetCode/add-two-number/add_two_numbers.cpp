#include"add_two_numbers.h"
#include<cstdlib>
#include<iostream>

class Solution {
public:
    /**
     * failed because convert to uint64_t couldn't handle large number, e.g. 10^61
     */
    ListNode* addTwoNumbers_failed(ListNode* l1, ListNode* l2) {
        // uint64_t i = UINT64_MAX;
        uint64_t i1=0, i2=0, iRes=0; // store number presenting in Lists
        ListNode* tmp = NULL; // interate for list
        int64_t cnt = 0; // order number for calculate i1 and i2
        ListNode* pRes = NULL;

        tmp = l1; cnt = 1;
        while (tmp != NULL){
            i1 += tmp->val*cnt;
            cnt *= 10;
            tmp = tmp->next;
        }

        tmp = l2; cnt = 1;
        while (tmp != NULL){
            i2 += tmp->val*cnt;
            cnt *= 10;
            tmp = tmp->next;
        }

        iRes = i1+i2;
        if(iRes == 0){
            return new ListNode(0);
        }
        while (iRes != 0){
            if (tmp==NULL){ // begin case
                tmp = new ListNode(iRes%10);
                pRes = tmp;
            }else{
                ListNode* tmp2 = new ListNode(iRes%10);
                tmp->next = tmp2;
                tmp = tmp2;
            }
            iRes /= 10;
        }

        return pRes;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *tmp=NULL, *tmpNew=NULL,  // tmp and tmpNew used for result list
                 *tmp1=NULL, *tmp2=NULL, // tmp1 and tmp2 used for travel through l1 and l2
                 *pRes=NULL; // pRes used for return
        uint64_t cnt1=0, cnt2=0, max=0;  // cnt1 and cnt2 for the number of node in list, max is the max number of them
        int bitRes=0; // result of two bits add, range from 0 to 18
        bool fOverflow = false; // if bitRes overflow, set true

        tmp = l1;
        while(tmp!=NULL){
            ++cnt1;
            tmp = tmp->next;
        }

        tmp = l2;
        while(tmp != NULL){
            ++cnt2;
            tmp = tmp->next;
        }

        max = cnt1>cnt2? cnt1 : cnt2;

        // handle the first bit add
        bitRes = l1->val + l2->val;
        pRes = new ListNode( bitRes%10 );
        fOverflow = (bitRes/10 == 1) ? true : false;

        // handle rest bits add
        tmp = pRes; tmp1 = l1->next; tmp2 = l2->next;
        for(uint64_t i = 1; i<max; ++i){
                bitRes = (tmp1 != NULL ? tmp1->val : 0) +
                    (tmp2 != NULL ? tmp2->val : 0) +
                    (fOverflow==true ? 1 : 0) ;
                tmpNew = new ListNode(bitRes%10);
                tmp->next = tmpNew;
                tmp1 = (tmp1 != NULL) ? tmp1->next : NULL;
                tmp2 = (tmp2 != NULL) ? tmp2->next : NULL;
                tmp = tmpNew; tmpNew = NULL;
                fOverflow = (bitRes/10 == 1) ? true : false;
        }

        // handle the last overflow
        if(fOverflow == true){
            tmpNew = new ListNode(1);
            tmp->next = tmpNew;
        }

        return pRes;
    }
};

int printList(ListNode* header){
    ListNode* tmp = header;
    while(tmp != NULL){
        std::cout<<tmp->val<<",";
        tmp = tmp->next;
    }
    std::cout<<"\n";
    return 0;
}

int main(){
    // ListNode* l1 = new ListNode(2);
    // l1->next = new ListNode(4);
    // l1->next->next = new ListNode(3);
    //
    // ListNode* l2 = new ListNode(5);
    // l2->next = new ListNode(6);
    // l2->next->next = new ListNode(4);
    //
    // int i1[] = {9};
    // int i2[] = {1, 9, 9, 9, 9, 9, 9, 9, 9, 9};


    int i1[] = {2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9};
    int i2[] = {5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9};
    int cnt1 = (int)sizeof(i1)/sizeof(int);
    int cnt2 = (int)sizeof(i2)/sizeof(int);
    ListNode* l1=new ListNode(i1[0]), *l2 = new ListNode(i2[0]);
    ListNode* tmp = NULL, *tmp2 = NULL;

    if (cnt1 > 1){
        tmp = l1;
        for (int i=1; i<cnt1; i++){
            tmp2 = new ListNode(i1[i]);
            tmp->next = tmp2;
            tmp = tmp2;
        }
    }

    if (cnt2 > 1){
        tmp = l2;
        for (int i=1; i<cnt2; i++){
            tmp2 = new ListNode(i2[i]);
            tmp->next = tmp2;
            tmp = tmp2;
        }
    }

    printList(l1);
    printList(l2);

    Solution* solu1 = new Solution();
    ListNode* pRes = solu1->addTwoNumbers(l1, l2);

    printList(pRes);

    return 0;
}
