class MyHashSet {
    public set = [];
    
    constructor() {}

    /**
     * @param {number} key
     * @return {void}
     */
    add(key: number): void {
        // check if exists, if yes return
        if(this.contains(key)) return;
        
        // else add
        this.set.push(key);
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key: number): void {
        // check if exists, if no return
        if(!this.contains(key)) return;

        // if yes, traverse and replace with last element and pop
        const end = this.set.length - 1;
        for(let i = 0; i < this.set.length; i++) {
            if(this.set[i] == key) {
                if(i == end) this.set.pop();
                this.set[i] = this.set[end];
                this.set.pop();
                break;
            }
        }
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key: number): boolean {
        for(let i = 0; i < this.set.length; i++) {
            if(this.set[i] == key) {
                return true;
            }
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
