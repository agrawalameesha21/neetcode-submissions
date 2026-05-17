class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums: number[]): number {
        const map = new Map();
        const keys = [];
        for(let i = 0; i < nums.length; i++) {
            let value = map.get(nums[i]) || 0;
            if(value == 0) keys.push(nums[i]);
            map.set(nums[i], ++value);
        }

        let result;
        let max;
        for(let i = 0; i < keys.length; i++) {
            let value = map.get(keys[i]);
            console.log(value, keys[i]);
            if(max >= value) continue;
            max = value;
            result = keys[i];
        }

        return result;
    }
}
