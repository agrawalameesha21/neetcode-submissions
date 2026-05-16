class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const strMaps = new Map();
        const sortedStrings = [];
        const result = [];
        const keys = [];

        for(let i = 0; i < strs.length; i++) {
            sortedStrings.push(strs[i].split("").sort().join(""));
            const strArr: [] = strMaps.get(sortedStrings[i]);
            if(!strArr || strArr.length == 0) {
                strMaps.set(sortedStrings[i], [strs[i]]);
                keys.push(sortedStrings[i]);
            } else {
                const newArr = [...strArr, strs[i]];
                strMaps.set(sortedStrings[i], newArr);
            }
        }

        for(let i = 0; i < keys.length; i++) {
            result.push(strMaps.get(keys[i]));
        }
        return result;
        
    }
}
