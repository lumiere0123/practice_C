#include <stdio.h>

void foo(int a, int b);
int foo2(double a, int c);
void hello(void);

int main(void)
{
        int     x=3,
                y=5;
        double  z=5.5;
        do
        {
          hello();
          x = y * 3 + x;
          foo(x,y);
          x = y + x;
          y=foo2(z,x);
          z += .5;
          printf("x is %d, y is %d, z is %.4lf\n",x,y,z);
     } while (x < 100 && z <= 6);
     hello();
     return 0;
}

void foo(int a, int b)
{
        int d;
        d = a * 4 % 5;
        b = d * 2;
        printf("a is %d, b is %d and d is %.9d\n",a,b,d);
}

int foo2(double a, int c)
{
        a += .5;
        c -= 1;
        return a + c;
}

void hello(void)
{    int a;
     for(a=8; a < 4 + 3 * 2;a++)
     {
          printf("HELLO\n");
     }
}

