import struct
import sugar_yespower

b = [2,0,0,0,210,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,46,22,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,140,3,0,0,88,0,0,0,66,3,0,0,
    2,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,
    3,49,50,51,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
    0,0,0,3,49,50,51,3,0,0,0,2,4,0,0,0,0,0,0,0,3,52,53,54,4,0,0,0,0,0,0,0,3,52,53,54,5,0,
    0,0,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,
    0,3,49,50,51,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    2,0,0,0,3,49,50,51,3,0,0,0,2,4,0,0,0,0,0,0,0,3,52,53,54,4,0,0,0,0,0,0,0,3,52,53,54,5,
    0,0,0]

b =''.join([chr(x) for x in b])[:80]

print repr(b[68:72])
print struct.unpack("<I", b[68:72])

print "%r" % sugar_yespower.getPoWHash("a"*80)
print "%r" % sugar_yespower.getPoWHash(b)
