/*

�@�f���������v���O����

 */


#include <stdio.h>
#include<stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

void  main( )
{
	char  c[256];
	long int   n0,n;
	int   ns=2;
	long int   j, k;
	time_t timer;

	struct timeval myTime;
	struct tm *time_st;
	double s_time, e_time;

	int	N_Trials;

	/* ��������� */
	printf("\nInput integer number: "); fflush(stdout);
	gets(c); n0=atoi(c);

	/* ���s�񐔂���� */
	printf("\nInput number of trials: "); fflush(stdout);
	gets(c); N_Trials=atoi(c);

	printf("\n"); 

	/*�@���Ԃ̌v���J�n */
	gettimeofday(&myTime, NULL);
	time_st = localtime(&myTime.tv_sec);
	
	s_time = (double)time_st->tm_hour*60*60
               + (double)time_st->tm_min*60
               + (double)time_st->tm_sec
               + (double)myTime.tv_usec/1000000;


	for(k = 1; k < N_Trials; k++)
	{


		for(n = n0, ns = 2; n >= ns; ns++)
		{

			for(j = 0; n % ns == 0; j++) 
			{
				n/=ns;
			}

			if (j == 0) continue;


		}


	}

	printf("******Prime factor dcomposition is shown******\n\n"); 

	for(n = n0, ns = 2; n >= ns; ns++)
	{

		for(j = 0; n % ns == 0; j++) 
		{
			n/=ns;
		}

		if (j == 0) continue;

		printf("Prime factor:%d  Multiplier:%d\n",ns,j);

	}

	printf("\n**********************************************\n\n"); 

	/*�@���Ԃ̌v���I�� */
	gettimeofday(&myTime, NULL);
	time_st = localtime(&myTime.tv_sec);
	
	e_time = (double)time_st->tm_hour*60*60
               + (double)time_st->tm_min*60
               + (double)time_st->tm_sec
               + (double)myTime.tv_usec/1000000;



	printf("Tatal processing time: %f[sec]\n", e_time - s_time);

	printf("Time per one process: %e[sec]\n", (double)(e_time - s_time)/N_Trials);

}