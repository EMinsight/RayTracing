from .abcd import *
from .lens import *

class THOR_AC254_050_A(AchromatDoubletLens):
    def __init__(self):
        super(THOR_AC254_050_A,self).__init__(fa=50.2,fb=43.4, R1=33.3,R2=-22.28, R3=-291.07, 
                                    tc1=9, tc2=2.5, n1=1.6700, n2=1.7283, diameter=25.4,
                                    url='https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=120',
                                    label="THOR_AC254_045_A")

class THOR_AC254_045_A(AchromatDoubletLens):
    def __init__(self):
        super(THOR_AC254_045_A,self).__init__(fa=45.0,fb=40.2, R1=31.2, R2=-25.90, R3=-130.6, 
                                    tc1=7, tc2=2.0, n1=1.6700, n2=1.8052, diameter=25.4,
                                    url='https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=120',
                                    label="THOR_AC254_045_A")

