#----made by zsir----
import sys

argc = len(sys.argv)
if argc < 2:
    print "read NANDIFO.nni and write nandinfo.txt"
    input_file = open('./NANDINFO.nni','rb')
    output_file = open('./nandinfo.txt','w')
elif argc == 2:
    print "read %s and write nandinfo.txt" % sys.argv[1]
    input_file = open(sys.argv[1],'rb')
    output_file = open('./nandinfo.txt','w')
elif argc == 3:
    print "read %s and write %s" % (sys.argv[1], sys.argv[2])
    input_file = open(sys.argv[1],'rb')
    output_file = open(sys.argv[2],'w')
else:
    print "usage: python flash_info.py"
    print "or + input_file"
    print "or + input_file + output_file"
    sys.exit()

#print sys.argv[1]

BLOCK_SIZE = 512
num = 0
while True:
    content = input_file.read(BLOCK_SIZE)
    if not content:
        break
    else:
        nand_id_number = int(content[0x10].encode('hex'), 16)
        for ix in range(nand_id_number):
            if ix == 0:
                output_file.write("nand id:")
                output_file.write(content[0x11 + ix].encode('hex'))
            elif ix == nand_id_number - 1:
                output_file.write("-")
                output_file.write(content[0x11 + ix].encode('hex'))
                output_file.write("\r\n")
            else:
                output_file.write("-")
                output_file.write(content[0x11 + ix].encode('hex'))

        ix = 0x40
        output_file.write("nand vendor:");
        while int(content[ix].encode('hex'), 16) != 0:
            output_file.write(content[ix])
            ix = ix + 1
        output_file.write("\r\n")

        ix = 0x50
        output_file.write("nand type:");
        while int(content[ix].encode('hex'), 16) != 0:
            output_file.write(content[ix])
            ix = ix + 1
        output_file.write("\r\n\r\n")
        num = num+1
#print num
