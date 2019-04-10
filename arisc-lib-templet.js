(function() {
    let imProto = {
        "exec": function() {
            let pc = this.pc | 0;
            let ins = this.mem[pc] | 0;
            let regI = this.regI;
            switch (ins & 3) {
                case 3:
                    switch ((ins >> 2) & 31) {
                        case {{{INS_LOAD}}}:
                        case {{{INS_LOAD_FP}}}:
                        case {{{INS_CUST_0}}}:
                        case {{{INS_MISC_MEM}}}:
                        case {{{INS_OP_IMM}}}:
                            switch ({{{INS_FUN_3 ins}}}) {
                                case {{{F3_ADDI}}}:
                                    regI[{{{INS_REG_DEST ins}}}] = regI[{{{INS_REG_SAUCE_1 ins}}}] + {{{INS_IMM_I ins}}};
                                    break;
                                case {{{F3_
                        case {{{INS_AUIPC}}}:
                        case {{{INS_OP_IMM_32}}}:
                        case {{{INS_???_7}}}:
                        case {{{INS_STORE}}}:
                        case {{{INS_STORE_FP}}}:
                        case {{{INS_CUST_1}}}:
                        case {{{INS_AMO}}}:
                        case {{{INS_OP}}}:
                        case {{{INS_LUI}}}:
                        case {{{INS_OP_32}}}:
                        case {{{INS_???_15}}}:
                        case {{{INS_MADD}}}:
                        case {{{INS_MSUB}}}:
                        case {{{INS_NMSUB}}}:
                        case {{{INS_NMADD}}}:
                        case {{{INS_OP_FP}}}:
                      //case {{{INS_RES_21}}}:
                        case {{{INS_CUST_2}}}:
                        case {{{INS_???_23}}}:
                        case {{{INS_BRANCH}}}:
                        case {{{INS_JALR}}}:
                      //case {{{INS_RES_26}}}:
                        case {{{INS_JAL}}}:
                        case {{{INS_SYSTEM}}}:
                      //case {{{INS_RES_29}}}:
                        case {{{INS_CUST_3}}}:
                        case {{{INS_???_31}}}:
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
