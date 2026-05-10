class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        if(!nums.length) return false;

        const hashSet = [];
        let i = 0;
        while(i < nums.length) {
            if(hashSet.includes(nums[i])) return true;
            hashSet.push(nums[i]);
            i++
        }
        return false;
    }
}