//sprintf

//cmd    : clear; gcc sprintf4.c && ./a.out


#include<stdio.h>
 
int main()
{
  int   a           = 1;
  float b           = 1.23;
  char  c           = 'u';
  char  string[100] = "My initial character array.";
 
  printf("%s\n", string);
 
  sprintf(string, "Integer = %d, Float = %f, Character = %c.", a, b, c);
 
  printf("%s\n", string);
 
  return 0;
}
