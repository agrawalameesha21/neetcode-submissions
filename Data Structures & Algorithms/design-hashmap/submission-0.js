class MyHashMap {
    keys = [];
    values = [];

    constructor() {}

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        // if exists, replace value
        if(this.get(key) != -1) {
            for(let i = 0; i < this.keys.length; i++) {
                if(this.keys[i] === key) {
                    this.values[i] = value;
                    break;
                }
            }
            return;
        }
        // if not, push both
        this.keys.push(key);
        this.values.push(value);
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        for(let i = 0; i < this.keys.length; i++) {
            if(this.keys[i] === key) {
                return this.values[i]
            }
        }
        return -1;
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        // if doesn't exist return
        if(this.get(key) === -1) return;

        // else swap to last and pop
        for(let i = 0; i < this.keys.length; i++) {
            if(this.keys[i] === key) {
                this.keys[i] = this.keys[this.keys.length - 1];
                this.values[i] = this.values[this.keys.length - 1];

                this.keys.pop();
                this.values.pop();
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
