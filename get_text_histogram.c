/*
 * �e�L�X�g�t�@�C���̕p�x���z�𐶐������v���O����
 */

#include <stdio.h>
#include<stdlib.h>
#include <string.h>

void get_char_histogram(char *input, int *char_hist)
{

	/*
		ascii�R�[�h��32�`127(96��)
	*/

	int i, j, t;
	int len;

	/*�@�������̒����擾 */
	len = strlen(input);

	/* �q�X�g�O�����̏����� */
	for(i = 32; i < 128; i++)
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
	char input_text[20000];
	int char_hist[1000];

	int i;

	/* ���̓t�@�C���I�[�v�� */
	if((fp = fopen("cipher.txt", "r")) == NULL)
	{
		puts("file not open");
		exit(0);
	}

	if((fo = fopen("char_histgram.txt", "w")) == NULL)
	{
		puts("er");
		exit(0);
	}

	/* �t�@�C���̓ǂݍ��݁E�\�� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("********       Text file is displayed.     **********\n");
	printf("*****************************************************\n\n\n");

	while ( fgets(input_text, 1000, fp) != NULL)
	{
		printf("%s",input_text);
	}

	/* �e�L�X�g�̃q�X�g�O���������߂� */
	get_char_histogram(input_text, char_hist);

	/* �q�X�g�O�����̕\���E�������� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("**********    Histogram is displayed.   ***********\n");
	printf("*****************************************************\n\n\n");


	for(i = 32; i < 128; i++)
	{
		printf("[%c, %d]\n",i, char_hist[i]);
		fprintf(fo,"%d, %d\n",i, char_hist[i]);
	}


	/* �I������ */
	fclose(fp);
	fclose(fo);

	return 0;
}
