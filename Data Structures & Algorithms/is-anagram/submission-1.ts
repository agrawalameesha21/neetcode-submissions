class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length !== t.length) return false;

        const sMap = new Map();
        const tMap = new Map();

        for(let i = 0; i < s.length; i++) {
            let num = sMap.get(s[i]) || 0;
            sMap.set(s[i], num + 1);

            num = tMap.get(t[i]) || 0;
            tMap.set(t[i], num + 1 );
        }

        for(let i = 0; i < s.length; i++) {
            if(sMap.get(s[i]) !== tMap.get(s[i])) return false;
        }
        return true;
    }
}
