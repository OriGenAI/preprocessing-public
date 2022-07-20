-- Generated [
-- Format      : ECLIPSE keywords (ASCII)
-- Exported by : Petrel 2020.4 Schlumberger
-- User name   : e0004673
-- Date        : Monday, December 20 2021 20:48:03
-- Project     : Modelo_Rubiales_AI.pet
-- Generated ]

RPTSCHED                               -- Generated : Petrel
  SOIL SWAT SGAS RS RV FIP WELLS /

RPTRST                                 -- Generated : Petrel
  BASIC=3 FLOWS FREQ DEN KRO KRW RVSAT PCOW /

SKIP                                   -- Generated : Petrel
--Default history strategy generated.

ENDSKIP                                -- Generated : Petrel

--Default history strategy generated.


GRUPTREE                               -- Generated : Petrel
  'GROUP 1' FIELD /
  /

DATES                                  -- Generated : Petrel
  1 JAN 1982 /
  /

WELSPECS                               -- Generated : Petrel
--'RB-007' is the simulation well name used to describe flow from 'RB-007'
--
  RB-007 'GROUP 1' 71 63 2100 OIL /
  RB-008 'GROUP 1' 71 63 200 WATER /
  /

WCONPROD
    'RB-007' 'OPEN' 'BHP' 5*  350/
/
WCONINJE
    'RB-008' WAT OPEN GRUP 50E3 4* /
/


COMPDAT                                -- Generated : Petrel
  RB-007 71 63 1 1 OPEN 1* 0.000954877 0.625 0.504124 0 1* Z 13.1405 /
  RB-007 71 63 3 3 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  RB-008 71 60 3 3 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 FEB 1982 /
  /

WCONPROD
    'RB-007' 'SHUT' 'BHP' 5*  350/
/
WCONINJE
    'RB-008' WAT SHUT GRUP 50E3 4* /
/

COMPDAT                                -- Generated : Petrel
  RB-007 71 63 1 1 OPEN 1* 0.000954877 0.625 0.504124 0 1* Z 13.1405 /
  RB-007 71 63 3 3 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 MAR 1982 /
  /

COMPDAT                                -- Generated : Petrel
  RB-007 71 63 1 1 OPEN 1* 0.000954877 0.625 0.504124 0 1* Z 13.1405 /
  RB-007 71 63 3 3 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 APR 1982 /
  /
