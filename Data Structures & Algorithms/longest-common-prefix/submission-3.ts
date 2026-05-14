
class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs: string[]): string {
        const strSet = [...new Set(strs)];
        if(strSet.length == 1) return strs[0];

        let prefix = "";
        for(let i=0; i< strs[0].length; i++) {
            let char = strs[0][i];
            let isSame = true;
            console.log(char, i, prefix);
            for(let j=1; j < strs.length; j++) {
                if( char !== strs[j][i]) {
                    isSame = false;
                    // console.log(char, strs[j][i], isSame);
                    break;
                }
            }

            if(!isSame) break;
            // console.log(prefix);
            prefix += char;
        }

        return prefix;
    }
}
