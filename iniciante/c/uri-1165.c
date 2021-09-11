#include<stdio.h>

int main(){

	int i, j, isprime = 1;
	int num1, num2;

	scanf("%d", &num1);

	for(i=0; i<num1; i++){
		scanf("%d", &num2);

		if (num1 < 2)
			isprime = 0;

		else if (num1 > 2) {
			for (j = 2; j < num2; j++) {
	    		if (num2 % j == 0){
	    			isprime = 0;
	    			break;
	    		}
	 	    }
	 	}
	 	if(isprime){
			printf("%d eh primo\n", num2);
		}
		else{
			printf("%d nao eh primo\n", num2);
		}
		isprime = 1;
	}

	return 0;
}
