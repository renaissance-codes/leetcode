##include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        int dlen = nums.size();
        vector<int> res(2);
        int i = 0;

        for(auto a: nums){
            int v = target-a;
            if(mp.count(v)){
                res[0] = mp[v];
                res[1] = i;
                return res;
            }else{
                mp[a] = i;
            }
            i++;
        }
        return res;
    }
};
