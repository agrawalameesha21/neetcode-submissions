class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const setNum = [...new Set(nums)];
        if(setNum.length === nums.length) return false;
        return true;
    }
}
