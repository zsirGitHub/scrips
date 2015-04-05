/**
 * made by zsir
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    FILE *fp_read, *fp_write;
    char read_buffer[512];
    int nand_id_number;
    int file_size;
    int ix,jx;


    fp_read = fopen("./NANDINFO.nni", "r");
    if(fp_read == NULL)
    {
        return 1;
    }

    fp_write = fopen("./nandinfo.txt", "w+");
    if(fp_write == NULL)
    {
        printf("fopen fail!\n");
        return 1;
    }

    fseek(fp_read, 0, SEEK_END);
    file_size = ftell(fp_read);
    printf("file_size:%d\r\n", file_size);
    for(jx = 0; (jx + 1) * BLOCK_SIZE <= file_size; jx++)
    {
        fseek(fp_read, jx * BLOCK_SIZE, SEEK_SET);
        fread(&read_buffer, BLOCK_SIZE, 1, fp_read);
        nand_id_number = read_buffer[16];

        fprintf(fp_write, "%s", "nand id: ");

        for(ix = 0; ix < nand_id_number; ix++)
        {
            if(ix != nand_id_number - 1)
            {
                fprintf(fp_write, "0x%02x", read_buffer[17 + ix] & 0x000000ff);
                fprintf(fp_write, "%s", "-");
            }
            else
            {
                fprintf(fp_write, "%02x", read_buffer[17 + ix] & 0x000000ff);
            }
        }

        fprintf(fp_write, "%s", "\r\n");
        fprintf(fp_write, "%s", "nand厂家: ");
        fprintf(fp_write, "%s", &read_buffer[0x40]);

        fprintf(fp_write, "%s", "\r\n");
        fprintf(fp_write, "%s", "nand型号: ");
        fprintf(fp_write, "%s\r\n\r\n", &read_buffer[0x50]);
    }
    fclose(fp_read);
    fclose(fp_write);

    return 0;
}
