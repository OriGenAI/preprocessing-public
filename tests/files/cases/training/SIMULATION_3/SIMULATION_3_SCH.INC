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
  /

COMPDAT                                -- Generated : Petrel
  RB-007 71 63 1 1 OPEN 1* 0.000954877 0.625 0.504124 0 1* Z 13.1405 /
  RB-007 71 63 3 5 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 FEB 1982 /
  /

COMPDAT                                -- Generated : Petrel
  RB-007 71 63 41 41 OPEN 1* 0.000392758 0.7083 0.195141 -1 1* Z 32.4788 /
  RB-007 71 63 3 3 SHUT 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 MAR 1982 /
  /

COMPDAT                                -- Generated : Petrel
  RB-007 71 63 1 1 OPEN 1* 0.000954877 0.625 0.504124 0 1* Z 13.1405 /
  RB-007 71 63 41 41 OPEN 1* 0.000392758 0.7083 0.195141 -1 1* Z 32.4788 /
  RB-007 71 63 3 5 OPEN 1* 0.00107229 0.625 0.566109 0 1* Z 13.1405 /
  /

DATES                                  -- Generated : Petrel
  1 APR 1982 /
  /
