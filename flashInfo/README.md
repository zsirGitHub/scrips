功能:
    将NANDINFO.nni(16进制文件)中的nand flash的信息解析出来,以字符形式存储到nandinfo.txt中,以便阅读.
描述:
    解析的信息有：nand id, nand 厂家, nand 类型.
    解析规则：
        1. 每512个字节存储一种flash的信息.
        2. 第16个字节描述id用几位描述.
            例byte: 16=5 17=92 18=F1 19=80 20=95 21=40 22=50 则id为: 92-F1-80-95-40
        3. 第64个字节为厂家信息字符串，以0结尾.
        4. 第80个字节为flash类型信息字符串，以0结尾.
        5. 2,3,4条字节为每512字节中的相对偏移.
说明:
    flash_info.c为c语言版本.
        gcc flash_info.c -o flashinfo
        ./flashinfo
    flash_info.py为python版本.
        python flash_info.py
