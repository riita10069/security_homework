/*
 *２つのバイナリーファイルの排他的論理和をファイルに書き込む
 */

#include <stdio.h>
#include<stdlib.h>
#include <string.h>

/*ファイルサイズを取得する*/
int getFSZ(FILE *fp)
{
  int size = 0;

  fseek( fp, 0, SEEK_END );
   size = ftell(fp);
  fseek(fp, 0, SEEK_SET );

   return size;
}

int main(void)
{
  FILE*fp;
  FILE*fo;
  FILE*fs;
  unsigned char input_binary1[200000],input_binary2[200000];
  int exclusive[50000];
  int fsize1;
  int fsize2;

  int i;

/*ファイルの読み込みと中身の確認*/
  if((fp = fopen("crypted", "r")) == NULL)
	{
		puts("file not open(crypted)");
		exit(0);
	}

	if((fo = fopen("crypted1", "r")) == NULL)
	{
		puts("file not open(crypted1)");
		exit(0);
	}

  if((fs = fopen("binary_exclusive.txt", "w")) == NULL)
	{
		puts("er");
		exit(0);
	}

/*ファイルサイズの取得*/
  fsize1 = getFSZ(fp);
  fsize2 = getFSZ(fo);

/*ファイルの中身の読み込み*/
  fread(input_binary1, sizeof(unsigned char), fsize1, fp);
  fread(input_binary2, sizeof(unsigned char), fsize2, fo);

/*排他的論理和をとる*/
  for(i = 0;i < fsize1; i++)
  {
    exclusive[i] = input_binary1[i] ^ input_binary2[i];
  }

/*結果のファイルへの書き込み*/
  for(i = 0;i < fsize1; i++)
  {
    printf("%d ",exclusive[i]);
    fprintf(fs,"%d ",exclusive[i]);
  }

  fclose(fp);
  fclose(fo);
  fclose(fs);

  return 0;
}
