class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]) {
        var i = 0;
        var processedNums = [];
        while (i < nums.length)
        {
            if (processedNums.includes(nums[i])) {
                return true
            }
            else {
                processedNums.push(nums[i]);
            }
            i++;
        }
        return false;
    }
}
