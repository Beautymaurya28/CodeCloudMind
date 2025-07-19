# question no 73
### sort color 1 2 and 0
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        int mid=0;
        while(Low<=high){
            if(nums[mid]==0){
                swap(nums[low],nums[mid]);
                low++;
                mid++
            }else if(nums[mid]==1){
                mid++;
            }
            else{
                swap(nums[mid],nums[high]);
                high--;
                mid++;
            }
        }
    }}; 