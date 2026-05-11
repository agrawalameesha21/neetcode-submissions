class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const map = new Map();
        for(let i = 0; i <= nums.length; i++) {
            map.set(target - nums[i], i);
        }

        for(let j = 0; j < nums.length; j++) {
            if(map.has(nums[j]) && map.get(nums[j]) !== j) {
                return [map.get(nums[j]), j];
            }
        }
    }
}
