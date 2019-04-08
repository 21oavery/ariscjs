(function() {
    const reg_ustatus = 0;
    const reg_uie = 1;
    const reg_utvec = 2;
    const reg_uscratch = 3;
    const reg_uepc = 4;
    const reg_ucause = 5;
    const reg_utval = 6;
    const reg_uip = 7;
    const reg_fflags = 8;
    const reg_frm = 9;
    const reg_fcsr = 10;
    const reg_cycle = 11;
    const reg_time = 12;
    const reg_instret = 13;
    const reg_hpmcounter
    let getCSRID = function(addr) {
        addr |= 0;
        switch (addr) {
            case 0x000: return "ustatus";
            case 0x004: return "uie";
            case 0x005: return "utvec";
            case 0x040: return "uscratch";
            case 0x041: return "uepc";
            case 0x042: return "ucause";
            case 0x043: return "utval";
            case 0x044: return "uip";
            case 0x001: return "fflags";
            case 0x002: return "frm";
            case 0x003:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
            case 0x000:
    let imProto = {
        "exec": function() {
            let pc = this.pc | 0;
            let ins = this.mem[pc] | 0;
            switch (ins & 3) {
                case 3:
                    switch ((ins >> 2) & 31) {
                        case 0:  // load
                        case 1:  // load-fp
                        case 2:  // custom-0
                        case 3:  // misc-mem
                        case 4:  // op-imm
                        case 5:  // auipc
                        case 6:  // op-imm-32
                        case 7:  // ???
                        case 8:  // store
                        case 9:  // store-fp
                        case 10: // custom-1
                        case 11: // amo
                        case 12: // op
                        case 13: // lui
                        case 14: // op-32
                        case 15: // ???
                        case 16: // madd
                        case 17: // msub
                        case 18: // nmsub
                        case 19: // nmadd
                        case 20: // op-fp
                      //case 21: // reserved
                        case 22: // custom-2/128
                        case 23: // ???
                        case 24: // branch
                        case 25: // jalr
                      //case 26: // reserved
                        case 27: // jal
                        case 28: // system
                      //case 29: // reserved
                        case 30: // custom-3/128
                        case 31: // ???
                        default:
                            this.throw()
                    }
        },
        "throw": function(t) {
            t |= 0;
        },
        "writeCSR": function(addr, perm, v) {
            addr |= 0;
            v |= 0;
            if (((~addr) >> 11) == 0) return false;
            if (perm >= ((addr >> 8) & 3)) {
                return false;
            }
            
    };
    let InternalMachine = function(memSize) {
        this.mem = new Uint8Array(memSize);
        this.regI = new Uint32Array(31);
        this.csrData = new Uint32Array(4096);
        this.pc = 0;
        this.ring = 0;
        this.int = null;
        this.isInt = false;
    };
    document.addEventListener("message", function(e) {
        let d = e.data;
        if (d.n == "int") {
            
    });
