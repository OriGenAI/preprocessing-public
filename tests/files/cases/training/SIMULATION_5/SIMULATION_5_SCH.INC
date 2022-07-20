-- Generated [
-- Format      : ECLIPSE keywords (ASCII)
-- Exported by : Petrel 2019.2 Schlumberger
-- User name   : cgronister
-- Date        : Wednesday, June 03 2020 22:20:14
-- Project     : STAMPEDE_MODEL_2020_Pv2019.pet
-- Generated ]

WHISTCTL
 ORAT /

RPTSCHED
  FIP /

RPTRST
  BASIC=3 FREQ=1 /

EXTRAPMS
  3 /

SKIP                                   -- Generated : Petrel
--Default history strategy generated.

ENDSKIP                                -- Generated : Petrel

WELSPECS                               -- Generated : Petrel
  I2 INJ 183 48 28748.0290932156 WATER /
  A1 A_W 137 50 29823.8712343609 OIL /
  /

COMPDAT                                -- Generated : Petrel
  I2 183 48 1 1 SHUT 1* 0 0.625 25.3131 1.4 1* Z 30.8929 /
  I2 183 48 2 2 OPEN 1* 0 0.625 25.1463 1.4 1* Z 31.0249 /
  I2 183 48 3 3 SHUT 1* 0 0.625 34.6928 1.4 1* Z 33.1064 /
  A1 137 50 1 1 OPEN 1* 0.955203 0.625 349.903 -2 1* Z 30.9084 /
  A1 137 50 2 2 OPEN 1* 0.843615 0.625 308.996 -2 1* Z 30.9005 /
  A1 137 50 3 3 SHUT 1* 0.0691437 0.625 25.3232 -2 1* Z 30.8926 /
  /

COMPLUMP                               -- Generated : Petrel
  I2 183 48 1 1 1 /
  I2 183 48 2 2 2 /
  I2 183 48 3 3 2 /
  A1 137 50 1 1 3 /
  A1 137 50 2 2 3 /
  A1 137 50 3 3 4 /
  /

GRUPTREE                               -- Generated : Petrel
  A_W FIELD /
  B_W FIELD /
  INJ FIELD /
  MON FIELD /
  /

WCONHIST                               -- Generated : Petrel
  A1L STOP ORAT 6* 15465 /
  A1U STOP ORAT 6* 0 /
  A2L STOP ORAT 6* 15290.4 /
  A2U STOP ORAT 6* 15600 /
  A3L STOP ORAT 6* 0 /
  A3U STOP ORAT 6* 0 /
  B1L STOP ORAT 6* 15032.9 /
  B1U STOP ORAT 6* 15876.1 /
  B2L STOP ORAT 6* 15397 /
  B2U STOP ORAT 6* 15628.2 /
  B3L STOP ORAT 6* 0 /
  B3U STOP ORAT 6* 0 /
  B4L STOP ORAT 5* 1 /
  B4U STOP ORAT 5* 1 /
  I2L STOP ORAT 6* 0 /
  I2U STOP ORAT 6* 0 /
  I3L STOP ORAT 6* 0 /
  I3U STOP ORAT 6* 0 /
  I4L STOP ORAT 6* 0 /
  I4U STOP ORAT 6* 0 /
  A1 SHUT LRAT 0 0 0 1* 0 0 15465 0 /
  A2 SHUT LRAT 0 0 0 1* 0 1511.12 0 0 /
  A3 SHUT LRAT 0 0 0 1* 0 0 0 0 /
  B1 SHUT LRAT 0 0 0 1* 0 2175.22 0 0 /
  B2 SHUT LRAT 0 0 0 1* 0 1535.1 0 0 /
  B3 SHUT LRAT 0 0 0 1* 0 0 0 0 /
  B4 SHUT LRAT 0 0 0 1* 0 0 0 0 /
  /

WCONINJH                               -- Generated : Petrel
  I2 WATER SHUT 0 0 0 5* RATE /
  I3 WATER SHUT 0 0 0 5* RATE /
  I4 WATER SHUT 0 0 0 5* RATE /
  /

WELTARG                                -- Generated : Petrel
  I2 BHP 23000 /
  I3 BHP 23000 /
  I4 BHP 23000 /
  A1 BHP 6000 /
  A3 BHP 6000 /
  B3 BHP 6000 /
  B4 BHP 6000 /
  A2 BHP 6000 /
  B2 BHP 6000 /
  B1 BHP 6000 /
  A1U BHP 6000 /
  A2U BHP 6000 /
  A3U BHP 6000 /
  B1U BHP 6000 /
  B2U BHP 6000 /
  B3U BHP 6000 /
  I2U BHP 6000 /
  I3U BHP 6000 /
  I4U BHP 6000 /
  B4U BHP 6000 /
  A1L BHP 6000 /
  A2L BHP 6000 /
  A3L BHP 6000 /
  B1L BHP 6000 /
  B2L BHP 6000 /
  B3L BHP 6000 /
  I2L BHP 6000 /
  I3L BHP 6000 /
  I4L BHP 6000 /
  B4L BHP 6000 /
  /

WPIMULT
A1 7.6504518 1* 1* 1* 2 2 /
A1 9.3741129 1* 1* 1* 3 3 /
A2 3.4165559 1* 1* 1* 2 2 /
A2 3.1965153 1* 1* 1* 3 3 /
A3 5.8895769 1* 1* 1* 1 1 /
A3 3.0655677 1* 1* 1* 3 3 /
B1 2.4485512 1* 1* 1* 1 1 /
B1 9.9038854 1* 1* 1* 2 2 /
B2 8.3401253 1* 1* 1* 2 2 /
B2 5.237797 1* 1* 1* 3 3 /
B3 9.4686926 1* 1* 1* 2 2 /
B3 6.3446047 1* 1* 1* 3 3 /
B4 3.6435788 1* 1* 1* 2 2 /
B4 3.365444 1* 1* 1* 3 3 /
--
I2 0.93530174 1* 1* 1* 1 1 /
I2 4.0955037 1* 1* 1* 3 3 /
I3 9.1276326 1* 1* 1* 1 1 /
I3 6.6453149 1* 1* 1* 2 2 /
I4 4.4566798 1* 1* 1* 2 2 /
I4 1.59194 1* 1* 1* 3 3 /
/




DATES             
2 JAN 2018 /          
/    

WELOPEN             
 A1  OPEN 1* 1* 1* 1* 1* /   
/ 

WELOPEN             
 I2  OPEN 1* 1* 1* 1 2 /   
/   

DATES             
3 JAN 2018 /          
/    

WELOPEN             
 I2  SHUT 1* 1* 1* 1 1 /  
 I2  SHUT 183 48 3 1* 1* / 
/   

DATES             
4 JAN 2018 /          
/    

WELOPEN             
 A1  OPEN 1* 1* 1* 3 3 /   
 A1  OPEN 1* 1* 1* 4 4 /   
/   