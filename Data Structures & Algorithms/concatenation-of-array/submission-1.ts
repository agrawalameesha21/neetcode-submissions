class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        if(nums.length == 0) return [];
        
        const ans = [...nums];        
        nums.forEach((num, index) => {
            ans[index + nums.length] = num;
        });

        return ans;
    }
}
