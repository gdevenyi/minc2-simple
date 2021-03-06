#include "minc2-simple.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc,char **argv)
{
    int ret=0;
    int use_short=0;
    const char *fname_in;
    const char *fname_out;
    struct minc2_tags * tags;
    
    if(argc<3) {
        fprintf(stdout,"Usage: %s <fname_in> <fname_out>\n",argv[0]);
        return 1;
    }
    fname_in=argv[1];
    fname_out=argv[2];
    
    tags=minc2_tags_allocate0();
    
    ret|=minc2_tags_load(fname_in,tags)==MINC2_SUCCESS;
    ret|=minc2_tags_save(fname_out,tags)==MINC2_SUCCESS;
    ret|=minc2_tags_free(tags);
    
    return ret;
}
