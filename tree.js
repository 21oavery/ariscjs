Int32Tree = (function() {
    let itproto = {
        "addElement": function(k, v) {
            k |= 0;
            let vsep = [v >> 28, (v >> 24) & 0xFF, (v >> 20) & 0xFF, (v >> 16) & 0xFF, (v >> 12) & 0xFF, (v >> 8) & 0xFF, (v >> 4) & 0xFF, v & 0xFF];
            let d = this.data;
            for (let i = 0; i < 7; i++) {
                v >>= 4;
                let t = v & 0xF;
                let t2 = d[t];
                if (t2 == null) {
                    t2 = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];
                    d[t] = t2;
                }
            }
            if (v == null) {
                if (d[vsep[7]] != null) this.cnt--;
            } else {
                if (d[vsep[7]] == null) this.cnt++;
            }
            d[vsep[7]] = v;
        },
        "getElement": function(k) {
            k |= 0;
            let vsep = [v >> 28, (v >> 24) & 0xFF, (v >> 20) & 0xFF, (v >> 16) & 0xFF, (v >> 12) & 0xFF, (v >> 8) & 0xFF, (v >> 4) & 0xFF, v & 0xFF];
            let d = this.data;
            for (let i = 0; i < 7; i++) {
                d = d[vsep[i]];
                if (d == null) return 0;
            }
            return d[vsep[7]] | 0;
        }
    }
    let Int32Tree = function() {
        this.data = [];
        this.cnt = 0;
    }
    return Int32Tree;
})();
