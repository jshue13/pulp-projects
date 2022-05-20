\* Landfill_Location_Problem *\
Minimize
Sum_of_Costs: 22 Route_L1_A + 20 Route_L1_B + 21 Route_L1_C + 18 Route_L1_D
 + 16 Route_L1_E + 19 Route_L1_F + 26 Route_L2_A + 21 Route_L2_B
 + 18 Route_L2_C + 25 Route_L2_D + 22 Route_L2_E + 20 Route_L2_F
 + 19 Route_L3_A + 21 Route_L3_B + 18 Route_L3_C + 23 Route_L3_D
 + 19 Route_L3_E + 17 Route_L3_F + 19 Route_L4_A + 25 Route_L4_B
 + 22 Route_L4_C + 23 Route_L4_D + 22 Route_L4_E + 17 Route_L4_F
 + 1000 Yes_or_No_L1 + 800 Yes_or_No_L2 + 700 Yes_or_No_L3 + 900 Yes_or_No_L4
Subject To
Linking_constraint_for_Landfill_L1: Route_L1_A + Route_L1_B + Route_L1_C
 + Route_L1_D + Route_L1_E + Route_L1_F - 9999 Yes_or_No_L1 <= 0
Linking_constraint_for_Landfill_L2: Route_L2_A + Route_L2_B + Route_L2_C
 + Route_L2_D + Route_L2_E + Route_L2_F - 9999 Yes_or_No_L2 <= 0
Linking_constraint_for_Landfill_L3: Route_L3_A + Route_L3_B + Route_L3_C
 + Route_L3_D + Route_L3_E + Route_L3_F - 9999 Yes_or_No_L3 <= 0
Linking_constraint_for_Landfill_L4: Route_L4_A + Route_L4_B + Route_L4_C
 + Route_L4_D + Route_L4_E + Route_L4_F - 9999 Yes_or_No_L4 <= 0
Sum_of_Tons_out_of_Collection_Area_A: Route_L1_A + Route_L2_A + Route_L3_A
 + Route_L4_A >= 500
Sum_of_Tons_out_of_Collection_Area_B: Route_L1_B + Route_L2_B + Route_L3_B
 + Route_L4_B >= 700
Sum_of_Tons_out_of_Collection_Area_C: Route_L1_C + Route_L2_C + Route_L3_C
 + Route_L4_C >= 1500
Sum_of_Tons_out_of_Collection_Area_D: Route_L1_D + Route_L2_D + Route_L3_D
 + Route_L4_D >= 1000
Sum_of_Tons_out_of_Collection_Area_E: Route_L1_E + Route_L2_E + Route_L3_E
 + Route_L4_E >= 1800
Sum_of_Tons_out_of_Collection_Area_F: Route_L1_F + Route_L2_F + Route_L3_F
 + Route_L4_F >= 1200
Binaries
Yes_or_No_L1
Yes_or_No_L2
Yes_or_No_L3
Yes_or_No_L4
End
