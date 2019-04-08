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
    
    "INS_REG_DEST":    "((%1 >> 6) & 0x1F)",
    "INS_REG_SAUCE_1": "((%1 >> 15) & 0x1F)",
    "INS_REG_SAUCE_2": "((%1 >> 20) & 0x1F)",
    "INS_FUN_3":       "((%1 >> 12) & 7)",
    "INS_FUN_7":       "((%1 >> 25) & 0x7F)"
}

def tokenise(s, start, end)
    if start == end:
        return []
    ret = []
    while True:
        lastPos = -1
        for i in range(start, end):
            if s[i] == " ":
                if lastPos != -1:
                    ret.add(s[lastPos:i])
                    lastPos = -1
            elif lastPos == -1:
                lastPos = i
        return ret

def getReplacement(mArgs):
    subV = const_table[mArgs[0]]
    if not subV:
        print("Warning: undefined macro: " + ts[0])
        return ""
    elif type(subV) == "<type 'str'>":
        subS = string(subV)
        pos = 0
        while True:
            sLen = len(subS)
            if sLen <= pos:
                break
            locPos = subS.find("%")
            if locPos == -1:
                break
            locEndPos = locPos + 1
            while locEndPos < 
            nLen = len(nString)
            while sPos = subS.find(nString, i)
                if sPos == -1:
                    break
                subS = subS[:sPos - 1] + ts[i] + subS[sPos + nLen:]
        return subS
    else:
        return string(subV)

v = False
with open("arisc-lib-templet.js", "r") as fIn:
    v = fIn.read()
    print(v)

s = 0
while True:
    posStart = v.find("{{", s)
    if posStart == -1:
        break
    posEnd = v.find("}}", pos + 2)
    if posEnd == -1:
        break
    ts = tokenise(s, posStart + 2, posEnd - 1)
    if len(ts) == 0:
        s = posEnd + 2
        continue
    else:

with open("arisc-lib.js", "w") as fOut:
    print(v)
    fOut.write(v)
