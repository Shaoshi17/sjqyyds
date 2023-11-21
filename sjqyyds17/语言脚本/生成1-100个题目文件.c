#include <stdio.h>
main(){
    char filename[255] = "";
    char a[]="\n#include <stdio.h>\n";
    char b[]="main(){\n\n}";
    FILE *fp;
    for(int i=1;i<=100;i++){
        sprintf(filename,"题目%d.c",i);
        fp=fopen(filename,"w");
        fputs(a,fp);
        fputs(b,fp);
        fclose(fp);
    }
}