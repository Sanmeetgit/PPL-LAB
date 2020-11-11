#include <stdio.h>
void A(void){
int *ret;
char buffer [8] ;
//printf("hello");
ret =( int*)buffer;
ret = ret + 6;
*ret = *ret + 7;          //use 7 to skip 1 lines; 19 to skip 2 lines, use 31 to skip 3 lines, use 65 to skip 4 lines 
}
int main(){
int x = 0;
A();
x=1;
printf("statement 1\n");
printf("statement 2\n");
printf("statement 3\n");
printf ("%d\n", x) ;
return 0;
}
