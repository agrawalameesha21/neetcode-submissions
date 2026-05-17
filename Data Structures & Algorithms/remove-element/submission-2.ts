class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums: number[], val: number): number {
        let k = 0;
        let pointer = nums.length-1;

        if(nums.length == 0) return 0;

        for(let i = 0; i < nums.length; i++) {
            if(i > pointer) break; 
            if(nums[i] === val) {   
                while(nums[pointer] == val && i < pointer){
                    pointer--;
                }

                if(pointer == i) continue;
                nums[i] = nums[pointer];
                nums[pointer] = val;
                pointer--;
                k++;
            } else k++;
        }

        return k;
    }
}
