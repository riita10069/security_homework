/*
 * �o�C�i���t�@�C���̕p�x���z�𐶐������v���O����
 */

#include <stdio.h>
#include<stdlib.h>
#include <string.h>
#include <stddef.h>     /* size_t    */
#include <ctype.h>      /* isprint() */

#define WIDTH   (16)

const void *dump(const void *addr, size_t bytes)
{
    const unsigned char *p = addr;
    char text[WIDTH+1];
    unsigned i = 0;

    while (i < bytes) {
        if ((i % WIDTH) == 0) {
            printf("%6d: ", i);

            memset(text, '\0', sizeof(text));
        }


        printf("%02x ", *p);

        text[i % WIDTH] = isprint(*p) ? *p : '.';

        p++; i++;


        if ((i % WIDTH) == 0) {
            printf(": %s\n", text);
        }
    }

    if ((i % WIDTH) != 0) {
        printf("%*s: %s\n", (WIDTH - (i % WIDTH)) * 3, " ", text);
    }

    return addr;
}

int getFSZ(FILE *fp)
{
  int size = 0;

  fseek( fp, 0, SEEK_END );
   size = ftell(fp);
  fseek(fp, 0, SEEK_SET );

   return size;
}

void get_binary_histogram(unsigned char *input, int *char_hist)
{

	int i, j, t;
	int len;

	/*�@�o�C�g���̒����擾 */
	len = strlen(input);

	/* �q�X�g�O�����̏����� */
	for(i = 0; i < 256; i++)
	{
		char_hist[i] = 0;
	}

  /*
	 *書き込み箇所
	 *ヒストグラムの作成
	 */
  for(i = 0; i < len; i++)
	{
		char_hist[input[i]] ++;
	}

}


int main(void)
{

	FILE*fp;
	FILE*fo;
	unsigned char input_binary[200000];
	int binary_hist[1000];
	int fsize;

	int i;

	/* ���̓t�@�C���I�[�v�� */
	if((fp = fopen("crypted", "rb")) == NULL)
	{
		puts("file not open");
		exit(0);
	}

	if((fo = fopen("binary_histgram.txt", "w")) == NULL)
	{
		puts("er");
		exit(0);
	}

	/* �ǂݍ��݃t�@�C���̃t�@�C���T�C�Y�����߂� */
	fsize = getFSZ(fp);

	/* �t�@�C���̓ǂݍ��݁E�\�� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("********       Binary file is dumped.      **********\n");
	printf("*****************************************************\n\n\n");

	fread(input_binary, sizeof(unsigned char), fsize, fp);

	dump(input_binary, fsize);

	printf("\n\n");

	/*  �o�C�i���t�@�C���̃q�X�g�O���������߂� */
	get_binary_histogram(input_binary, binary_hist);

	/* �q�X�g�O�����̕\���E�������� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("**********    Histogram is displayed.   ***********\n");
	printf("*****************************************************\n\n\n");


	for(i = 0; i < 256; i++)
	{
		printf("[%d, %d]\n",i, binary_hist[i]);
		fprintf(fo,"%d, %d\n",i, binary_hist[i]);
	}


	/* �I������ */
	fclose(fp);
	fclose(fo);

	return 0;
}
