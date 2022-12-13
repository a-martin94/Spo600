#include <sys/auxv.h>
#include <stdio.h>

void adjust_channels(unsigned char *image, int x_size, int y_size,float red_factor, float green_factor, float blue_factor) __attribute__(( ifunc("magic_resolver") ));


#pragma GCC target "arch=armv8-a+sve2"

/*
adjust_channels :: adjust red/green/blue colour channels in an image

The function returns an adjusted image in the original location.

Copyright (C)2022 Seneca College of Applied Arts and Technology
Written by Chris Tyler
Distributed under the terms of the GNU GPL v2

*/


#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// ----------------------------------------------------------------- Naive implementation in C

#include <sys/param.h>



void adjust_channels_sve2(unsigned char *image, int x_size, int y_size,float red_factor, float green_factor, float blue_factor){
        
/*
        The image is stored in memory as pixels of 3 bytes, representing red/green/blue values.
        Each of these values is multiplied by the corresponding adjustment factor, with 
        saturation, and then stored back to the original memory location.
        
        This simple implementation causes int to float to int conversions.
        
*/

        for (int i = 0; i < x_size * y_size * 3; i += 3) {
                image[i]   = MIN((float)image[i]   * red_factor,   255);
                image[i+1] = MIN((float)image[i+1] * blue_factor,  255);
                image[i+2] = MIN((float)image[i+2] * green_factor, 255);
        }
}




#pragma GCC target "arch=armv8-a+sve"

/*
adjust_channels :: adjust red/green/blue colour channels in an image

The function returns an adjusted image in the original location.

Copyright (C)2022 Seneca College of Applied Arts and Technology
Written by Chris Tyler
Distributed under the terms of the GNU GPL v2

*/


#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// ----------------------------------------------------------------- Naive implementation in C

#include <sys/param.h>



void adjust_channels_sve(unsigned char *image, int x_size, int y_size,float red_factor, float green_factor, float blue_factor){
        
/*
        The image is stored in memory as pixels of 3 bytes, representing red/green/blue values.
        Each of these values is multiplied by the corresponding adjustment factor, with 
        saturation, and then stored back to the original memory location.
        
        This simple implementation causes int to float to int conversions.
        
*/

        for (int i = 0; i < x_size * y_size * 3; i += 3) {
                image[i]   = MIN((float)image[i]   * red_factor,   255);
                image[i+1] = MIN((float)image[i+1] * blue_factor,  255);
                image[i+2] = MIN((float)image[i+2] * green_factor, 255);
        }
}




#pragma GCC target "arch=armv8-a"

/*
adjust_channels :: adjust red/green/blue colour channels in an image

The function returns an adjusted image in the original location.

Copyright (C)2022 Seneca College of Applied Arts and Technology
Written by Chris Tyler
Distributed under the terms of the GNU GPL v2

*/


#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// ----------------------------------------------------------------- Naive implementation in C

#include <sys/param.h>



void adjust_channels_asimd(unsigned char *image, int x_size, int y_size,float red_factor, float green_factor, float blue_factor){
        
/*
        The image is stored in memory as pixels of 3 bytes, representing red/green/blue values.
        Each of these values is multiplied by the corresponding adjustment factor, with 
        saturation, and then stored back to the original memory location.
        
        This simple implementation causes int to float to int conversions.
        
*/

        for (int i = 0; i < x_size * y_size * 3; i += 3) {
                image[i]   = MIN((float)image[i]   * red_factor,   255);
                image[i+1] = MIN((float)image[i+1] * blue_factor,  255);
                image[i+2] = MIN((float)image[i+2] * green_factor, 255);
        }
}



static void (*magic_resolver(void)) {
        long hwcaps  = getauxval(AT_HWCAP);
        long hwcaps2 = getauxval(AT_HWCAP2);

        printf("\n### Resolver function - selecting the implementation to use for  foo()\n");
        if (hwcaps2 & HWCAP2_SVE2) {
                return adjust_channels_sve2;
        } else if (hwcaps & HWCAP_SVE) {
                return adjust_channels_sve;
        } else {
                return adjust_channels_asimd;
        }
};