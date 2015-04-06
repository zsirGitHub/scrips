#----made by zsir----

BLOCK_SIZE = 512
input_file = open('./NANDINFO.nni','rb')
output_file = open('./nandinfo.txt','w')
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
print num
