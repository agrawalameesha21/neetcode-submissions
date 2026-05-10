class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length !== t.length) return false;

        // sol:
        /**
         * sort both strings
         * run for loop and return false if any index doesn't match else true
         * 
         * add both string to set
         * then run for loop, keep track of each duplicate element and its occurence
         * compare it for both strings
         */

        const sSet = [...s].sort();
        const tSet = [...t].sort();

        for(let i = 0; i < s.length; i++) {
            if(sSet[i] !== tSet[i]) return false;
        }
        return true;
    }
}
