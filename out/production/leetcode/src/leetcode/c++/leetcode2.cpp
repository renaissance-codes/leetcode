struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == NULL){
            return l2;
        }
        int p=0;
        ListNode* lv = l1;
        while(p | l2!=NULL ){

            int l2v = 0;
            if(l2 != NULL){
                l2v = l2->val;
            }
            int val = l1->val + l2v + p;
            l1->val = val%10;
            p = val/10;

            if(l2 != NULL){
                l2 = l2->next;
            }
            if(l1->next == NULL & (p | l2!=NULL)){
                ListNode* nl1 = new ListNode(0);
                l1->next = nl1;
            }
            l1 = l1->next;

        }
        return lv;
    }
};

class Solution2 {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* lv = new ListNode(0);
        ListNode* pv = lv;
        int p=0;

        while(p | l2!=NULL | l1!=NULL){
            int l1v = l1==NULL?0:l1->val;
            int l2v = l2==NULL?0:l2->val;

            int val = l1v + l2v + p;
            p = val/10;

            l1 = l1==NULL?l1:l1->next;
            l2 = l2==NULL?l2:l2->next;
            lv->next = new ListNode(val%10);
            lv = lv->next;

        }
        lv = NULL;
        return pv->next;
    }
};
