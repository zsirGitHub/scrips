#----made by zsir----

BLOCK_SIZE = 512
fp = open('./NANDINFO.nni','rb')
num = 0
while True:
    content = fp.read(BLOCK_SIZE)
    if not content:
        break
    else:
        nand_id_number = int(content[0x10].encode('hex'), 16)
        for ix in range(nand_id_number):
            if ix == 0:
                print "nand id:%s" % content[0x11 + ix].encode('hex'),
            else:
                print "%s" % content[0x11 + ix].encode('hex'),

        ix = 0x40
        print "nand vendor:",
        while int(content[ix].encode('hex'), 16) != 0:
            print "%s" % content[ix],
            ix = ix + 1

        ix = 0x50
        print "nand type:",
        while int(content[ix].encode('hex'), 16) != 0:
            print "%s" % content[ix],
            ix = ix + 1
        print ""
        num = num+1
print num
