import io

const_table = {
    "INS_LOAD":      0,
    "INS_LOAD_FP":   1,
    "INS_CUST_0":    2,
    "INS_MISC_MEM":  3,
    "INS_OP_IMM":    4,
    "INS_AUIPC":     5,
    "INS_OP_IMM_32": 6,
    "INS_???_7":     7,
    "INS_STORE":     8,
    "INS_STORE_FP":  9,
    "INS_CUST_1":   10,
    "INS_AMO":      11,
    "INS_OP":       12,
    "INS_LUI":      13,
    "INS_OP_32":    14,
    "INS_???_15":   15,
    "INS_MADD":     16,
    "INS_MSUB":     17,
    "INS_NMSUB":    18,
    "INS_NMADD":    19,
    "INS_OP_FP":    20,
    "INS_RES_21":   21,
    "INS_CUST_2":   22,
    "INS_???_23":   23,
    "INS_BRANCH":   24,
    "INS_JALR":     25,
    "INS_RES_26":   26,
    "INS_JAL":      27,
    "INS_SYSTEM":   28,
    "INS_RES_29":   29,
    "INS_CUST_3":   30,
    "INS_???_31":   31,
    
    "INS_REG_DEST":    "((ins >> 6) & 0x1F)",
    "INS_REG_SAUCE_1": "((ins >> 15) & 0x1F)",
    "INS_REG_SAUCE_2": "((ins >> 20) & 0x1F)",
    "INS_FUN_3":       "((ins >> 12) & 7)",
    "INS_FUN_7":       "((ins >> 25) & 0x7F)"
}

fIn = open("arisc-first.js", "r", encoding="utf-8")
