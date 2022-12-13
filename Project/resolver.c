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