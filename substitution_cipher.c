/*

�@�����Í��v���O����
�@�i�ǂݍ��ޕ����̓A���t�@�x�b�g3000�����܂Łj

 */


#include <stdio.h>
#include<stdlib.h>
#include <string.h>

void shuffle_ascii(char *input, char *output, int *tbl)
{

	/*
		ascii�R�[�h��32�`127(96��)
	*/

	int i, j, t;
	int len;

	/*�@�����������̒��� */
	len = strlen(input);

	/*�@�Í���/���� */
	for(i = 0; i < len; i++)
	{
		output[i] = tbl[input[i]];
	}

	output[len] = '\0';


}


int main(void)
{

	FILE*fp;
	FILE*fo_e;
	FILE*fo_d;
	FILE*fo_t;
	FILE*fo_it;
	FILE*fo_t_a;
	FILE*fo_it_a;
	char plain_text[3000];
	char cipher_text[3000];
	char decipher_text[3000];
	int table[256], inv_table[256];
	int t_table[256], t_inv_table[256];
	int KEY;
	int i, j, t;

	/* �����t�@�C���I�[�v�� */
	if ((fp = fopen("plaintext.txt", "r")) == NULL) { puts("file not open"); }
	if ((fo_e = fopen("cipher.txt", "w")) == NULL) { puts("er"); }
	if ((fo_d = fopen("decipher.txt", "w")) == NULL) { puts("er"); }
	if ((fo_t = fopen("subcipher_table.txt", "w")) == NULL) { puts("er"); }
	if ((fo_it = fopen("subcipher_inv_table.txt", "w")) == NULL) { puts("er"); }
	if ((fo_t_a = fopen("subcipher_table_a.txt", "w")) == NULL) { puts("er"); }
	if ((fo_it_a = fopen("subcipher_inv_table_a.txt", "w")) == NULL) { puts("er"); }


	/* �����t�@�C���̓ǂݍ��݁E�\�� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("********    Plaintext data is displayed.   **********\n");
	printf("*****************************************************\n\n\n");


	while ( fgets(plain_text, 3000, fp) != NULL)
	{
		printf("%s",plain_text);
	}

	/* �Í����̐ݒ� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("****             Input encryption key           ****\n");
	printf("****         within 10 digit integer number     ****\n");
	printf("*****************************************************\n\n\n");

	/*** �����_�������e�[�u���̍쐬�E�ۑ� ****/

	/* �����_���e�[�u���������я����l�̓��́E�ݒ� */
	scanf("%d", &KEY);

	printf("Encryption key = [%d]\n\n", KEY);

	srand(KEY);

	for(i = 32; i < 128; i++)
	{
		table[i] = i;
	}

	/* �Ώە����R�[�h�̐ݒ� */
	/*�@�X�y�[�X�A�J���}�A�s���I�h�@*/
	t_table[0] = 32;
	t_table[1] = 44;
	t_table[2] = 46;

	/*�@A-Z�@*/
	for(i = 65; i < 91; i++)
	{
		t_table[i - 62] = i;
	}

	/*�@a-z�@*/
	for(i = 97; i < 123; i++)
	{
		t_table[i - 97 + 29] = i;
	}

	/* �����_�������e�[�u���̐ݒ� */
	for(i = 0;i < 55; i++)
	{
		j = rand()%55;
		t = table[t_table[i]];
		table[t_table[i]] = table[t_table[j]];
		table[t_table[j]] = t;
	}


	/* �����_�������e�[�u���̕ۑ� */
	for(i = 32; i < 128; i++)
	{
		fprintf(fo_t,"%c, %c\n",i, table[i]);
	}

	for(i = 32; i < 128; i++)
	{
		fprintf(fo_t_a,"%c, %c\n",i, table[i]);
	}

	/* �Í��� */
	shuffle_ascii(plain_text, cipher_text, table);


	/* �Í��t�@�C���̕\���E�������� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("**********    Cipher text is displayed.   ***********\n");
	printf("*****************************************************\n\n\n");

	printf("%s",cipher_text);
	fprintf(fo_e,"%s",cipher_text);
	fflush(fo_e);

	/* �������̐ݒ� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("****             Input decryption key           ****\n");
	printf("****         within 10 digit integer number     ****\n");
	printf("*****************************************************\n\n\n");

	/*** �����_���t�����e�[�u���̍쐬�E�ۑ� ***/

	/* �����_���e�[�u���������я����l�̓��́E�ݒ� */
	scanf("%d", &KEY);

	printf("Decryption key = [%d]\n\n", KEY);

	srand(KEY);

	for(i = 32; i < 128; i++)
	{
		table[i] = i;
	}

	/* �����_�������e�[�u���̐ݒ� */
	for(i = 0;i < 55; i++)
	{
		j = rand()%55;
		t = table[t_table[i]];
		table[t_table[i]] = table[t_table[j]];
		table[t_table[j]] = t;
	}

/*
 *書き込み箇所
 *逆換字テーブルの作成
 */
  for(i = 32;i < 128; i++)
	{
		inv_table[table[i]] = i;
	}

	/* �����_�������t�e�[�u���̕ۑ� */
	for(i = 32; i < 128; i++)
	{
		fprintf(fo_it,"%c, %c\n",i, inv_table[i]);
	}

	for(i = 32; i < 128; i++)
	{
		fprintf(fo_it_a,"%d, %d\n",i, inv_table[i]);
	}

	/* ���� */
	shuffle_ascii(cipher_text, decipher_text, inv_table);

	/* �����t�@�C���̕\���E�������� */
	printf("\n\n");
	printf("*****************************************************\n");
	printf("*********    Decipher text is displayed.   **********\n");
	printf("*****************************************************\n\n\n");

	printf("%s",decipher_text);
	fprintf(fo_d,"%s",decipher_text);
	fflush(fo_d);

	printf("\n\n");

	/* �I������ */
	fclose(fp);
	fclose(fo_e);
	fclose(fo_d);
	fclose(fo_t);
	fclose(fo_it);
	fclose(fo_t_a);
	fclose(fo_it_a);


	printf("[End of substitution_cipher]\n\n");

	return 0;
}
