import sys

const_table = {
    "MASK_FULL": "{{{MATH - {{{MATH << 1 %1}}} 1}}}",
    "MASK":      "{{{MATH ^ {{{MASK_FULL %1}}} {{{MASK_FULL {{{MATH - %2 1}}} }}} }}}"

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
    
    "FRM_REG_DEST":    "(((%1) >> 6) & 0x1F)",
    "FRM_REG_SAUCE_1": "(((%1) >> 15) & 0x1F)",
    "FRM_REG_SAUCE_2": "(((%1) >> 20) & 0x1F)",
    "FRM_FUN_3":       "(((%1) >> 12) & 7)",
    "FRM_FUN_7":       "(((%1) >> 25) & 0x7F)",
    "FRM_IMM_I":       "((%1) >> 20)",
    "FRM_IMM_S":       "((((%1) >> 7) & 0x1F) | (((%1) >> 20) & 0xfd0)",
    "FRM_IMM_B":       "((((%1) >> 7) & 0x2E) | (((%1) >> 20) & 0x7d0) | (((%1) << 4) & 0x400) | (((%1) >> 19) & 0x800))",
    "FRM_IMM_U":       "((%1) & 0xfffff800)",
    "FRM_IMM_J":       "(((%1) & 800) | () | () | ())"
}

is3 = sys.version_info[0] == 3
def checkIsString(v):
    if is3:
        return isinstance(v, str)
    else:
        return isinstance(v, basestring)

def tokenise(s, start, end):
    if start == end:
        return []
    ret = []
    while True:
        lastPos = -1
        for i in range(start, end):
            if s[i] == " ":
                if lastPos != -1:
                    ret.append(s[lastPos:i])
                    lastPos = -1
            elif lastPos == -1:
                lastPos = i
        if lastPos != -1:
            ret.append(s[lastPos:end + 1])
        return ret

def getReplacement(mArgs):
    subV = const_table[mArgs[0]]
    if not subV:
        print("Warning: undefined macro: " + ts[0])
        return ""
    elif checkIsString(subV):
        if subV == "MATH":
            s = {
                ">>": lambda: str(int(mArgs.get(1, 0)) >> int(mArgs.get(2, 0))),
                "<<": lambda: str(int(mArgs.get(1, 0)) << int(mArgs.get(2, 0))),
                "&": lambda: str(int(mArgs.get(1, 0)) & int(mArgs.get(2, 0))),
                "|": lambda: str(int(mArgs.get(1, 0)) | int(mArgs.get(2, 0))),
                "^": lambda: str(int(mArgs.get(1, 0)) ^ int(mArgs.get(2, 0))),
                "+": lambda: str(int(mArgs.get(1, 0)) + int(mArgs.get(2, 0))),
                "-": lambda: str(int(mArgs.get(1, 0)) - int(mArgs.get(2, 0))),
                "*": lambda: str(int(mArgs.get(1, 0)) * int(mArgs.get(2, 0))),
                "/": lambda: str(int(mArgs.get(1, 0)) / int(mArgs.get(2, 0)))
            }
            return s.get(mArgs[0], lambda: "")()
        else:
            subS = str(subV)
            pos = 0
            while True:
                sLen = len(subS)
                if sLen <= pos:
                    break
                locPos = subS.find("%", pos)
                if locPos == -1:
                    break
                locEndPos = locPos + 1
                while True:
                    if (locEndPos >= sLen) or (not subS[locEndPos].isdigit()):
                        break
                    locEndPos += 1
                n = int(subS[locPos + 1:locEndPos])
                subS = subS[:locPos] + mArgs[n] + subS[locEndPos:]
                pos = locPos
            return subS
    else:
        return str(subV)

def replace(data):
    pos = 0
    rLen = 0
    replacePos = []
    while True:
        if rLen == 0:
            sLen = len(data)
            if sLen <= pos:
                break
            locPos = data.find("{{{", pos)
            if locPos == -1:
                break
            pos = locPos
            replacePos.append(locPos)
            rLen = 1
        e = replacePos[rLen - 1]
        locEndPos = data.find("}}}", e + 3)
        if locEndPos == -1:
            break
        locNextPos = data.find("{{{", e + 3)
        if (locNextPos != -1) and (locNextPos < locEndPos):
            replacePos.append(locNextPos)
            rLen += 1
            continue
        data = data[:e] + getReplacement(tokenise(data, e + 3, locEndPos - 1)) + data[locEndPos + 3:]
        rLen -= 1
        replacePos[rLen] = None
    return data

with open("arisc-lib-templet.js", "r") as fIn:
    v = fIn.read()
    with open("arisc-lib.js", "w") as fOut:
        v = replace(v)
        fOut.write(v)
