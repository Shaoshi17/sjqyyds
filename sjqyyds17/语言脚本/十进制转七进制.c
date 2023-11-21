#include<stdio.h>
main() {
    int num = -7;
    int a = 0, b = 0;
    if (num < 0) {
        b = 1;
        num = -num;
    }
    while (num != 0) {
        if (num >= 7) {
            a += 10;
            num -= 7;
            if (a / 10 % 10 == 7) {
                a = a - 70 + 100;
            }
        }
        else {
            a += num;
            num = 0;
        }
    }
    if (b == 1) {
        a = -a;
    }
    printf("%d", a);
}