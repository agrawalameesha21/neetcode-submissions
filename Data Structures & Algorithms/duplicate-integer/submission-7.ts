class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        var hashSet = [];
        var i = 0;
        while(i < nums.length) {
            if(hashSet.includes(nums[i])) {
                return true;
            } else hashSet.push(nums[i]);
            i++
        }
        return false;
    }
}