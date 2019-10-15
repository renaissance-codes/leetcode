class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        int i=0;
        int j=0;
        vector<int> data;
        while(i<m || j<n){
            int x;
            if(i==m){
                x = nums2[j];
                j++;
            }else if(j==n){
                x = nums1[i];
                i++;
            }else{
                if(nums1[i]<nums2[j]){
                    x = nums1[i];
                    i++;
                }else{
                    x = nums2[j];
                    j++;
                }
            }
            data.push_back(x);
        }
        int mid = (m+n)/2;
        if((m+n)%2){
            return data[mid];
        }else{
            return (data[mid-1]+data[mid])/2.0;
        }
    }
};

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))

// 二分法解决问题
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if(m>n){
            return findMedianSortedArrays(nums2, nums1);
        }

        int maxl = 0;
        int maxr = m;
        int halfLen = (m+n+1)/2;
        while(maxl<=maxr){
            int i = (maxl+maxr)/2;
            int j = halfLen - i;

            if(i<maxr && nums2[j-1] > nums1[i]){
                maxl = i+1;
            }else if(i>maxl && nums1[i-1] > nums2[j]){
                maxr = i-1;
            }else{
                int maxLeft = 0;
                if(i==0){
                    maxLeft = nums2[j-1];
                }else if(j==0){
                    maxLeft = nums1[i-1];
                }else{
                    maxLeft = max(nums1[i-1], nums2[j-1]);
                }
                if((m+n)%2==1){
                    return maxLeft;
                }

                int minRight = 0;
                if(i==m){
                    minRight = nums2[j];
                }else if(j==n){
                    minRight = nums1[i];
                }else{
                    minRight = min(nums1[i], nums2[j]);
                }

                return (maxLeft+minRight)/2.0;
            }
        }

        return 0.0;

    }
};