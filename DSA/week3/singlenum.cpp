#include<iostream>
using namespace std;
int singlenum(int nums[],int n){
    int ans=nums[0];
    for(int i=1;i<5;i++){
        ans=ans^nums[i];
    }
    return ans;
}
int main(){
    int nums[5]= {1,5,2,1,2};
    for(int i=0;i<5;i++){
        cout<<nums[i]<<" ";
    }
    cout<<endl;
     int result=singlenum(nums,5);
     cout<<result;
    return 0;
}