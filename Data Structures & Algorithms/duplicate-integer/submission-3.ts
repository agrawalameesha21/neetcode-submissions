class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        if(!nums.length) return false;

        const hashSet = [];
        for(let i = 0; i < nums.length; i++) {
            if(hashSet.includes(nums[i])) return true;
            hashSet.push(nums[i]);
        }
        return false;
    }
}