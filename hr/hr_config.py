

class HR_Config():
    """Object for storing HR attributes. Any unspecified values are calculated from LTHR."""
    def __init__(self,
                 lthr,
                 vthr=None,
                 rcphr=None,
                 Z1_h=None,
                 Z2_l=None, Z2_h=None,
                 Z3_l=None, Z3_h=None,
                 Z4_l=None, Z4_h=None,
                 Z5_l=None):
        self.lthr = lthr
        self.vthr = 0.96 * lthr if vthr is None else vthr
        self.rcphr = 1.02 * lthr if rcphr is None else rcphr
        self.Z1_h = 0.80 * lthr if Z1_h is None else Z1_h
        self.Z2_l = 0.80 * lthr if Z2_l is None else Z2_l
        self.Z2_h = 0.89 * lthr if Z2_h is None else Z2_h
        self.Z3_l = 0.96 * lthr if Z3_l is None else Z3_l
        self.Z3_h = lthr if Z3_h is None else Z3_h
        self.Z4_l = 1.02 * lthr if Z4_l is None else Z4_l
        self.Z4_h = 1.06 * lthr if Z4_h is None else Z4_h
        self.Z5_l = 1.06 * lthr if Z5_l is None else Z5_l

