---
type: Jurisdiction
title: "Duval County, FL"
classification: county
fips: "12031"
state: "FL"
demographics:
  population: 1023153
  population_under_18: 253220
  population_18_64: 367532
  population_65_plus: 402401
  median_household_income: 71277
  poverty_rate: 14.15
  homeownership_rate: 58.23
  unemployment_rate: 4.48
  median_home_value: 303500
  gini_index: 0.473
  vacancy_rate: 8.71
  race_white: 521574
  race_black: 292981
  race_asian: 50482
  race_native: 2253
  hispanic: 126467
  bachelors_plus: 322765
districts:
  - to: "us/states/fl/districts/04"
    rel: in-district
    area_weight: 0.6317
  - to: "us/states/fl/districts/05"
    rel: in-district
    area_weight: 0.2935
  - to: "us/states/fl/districts/senate/4"
    rel: in-district
    area_weight: 0.6525
  - to: "us/states/fl/districts/senate/5"
    rel: in-district
    area_weight: 0.27
  - to: "us/states/fl/districts/house/15"
    rel: in-district
    area_weight: 0.4028
  - to: "us/states/fl/districts/house/17"
    rel: in-district
    area_weight: 0.1296
  - to: "us/states/fl/districts/house/12"
    rel: in-district
    area_weight: 0.1109
  - to: "us/states/fl/districts/house/13"
    rel: in-district
    area_weight: 0.105
  - to: "us/states/fl/districts/house/14"
    rel: in-district
    area_weight: 0.0888
  - to: "us/states/fl/districts/house/16"
    rel: in-district
    area_weight: 0.0855
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Duval County, FL

County jurisdiction — 96 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1023153 |
| Under 18 | 253220 |
| 18–64 | 367532 |
| 65+ | 402401 |
| Median household income | 71277 |
| Poverty rate | 14.15 |
| Homeownership rate | 58.23 |
| Unemployment rate | 4.48 |
| Median home value | 303500 |
| Gini index | 0.473 |
| Vacancy rate | 8.71 |
| White | 521574 |
| Black | 292981 |
| Asian | 50482 |
| Native | 2253 |
| Hispanic/Latino | 126467 |
| Bachelor's or higher | 322765 |

## Districts

- [FL-04](/us/states/fl/districts/04.md) — 63% (congressional)
- [FL-05](/us/states/fl/districts/05.md) — 29% (congressional)
- [FL Senate District 4](/us/states/fl/districts/senate/4.md) — 65% (state senate)
- [FL Senate District 5](/us/states/fl/districts/senate/5.md) — 27% (state senate)
- [FL House District 15](/us/states/fl/districts/house/15.md) — 40% (state house)
- [FL House District 17](/us/states/fl/districts/house/17.md) — 13% (state house)
- [FL House District 12](/us/states/fl/districts/house/12.md) — 11% (state house)
- [FL House District 13](/us/states/fl/districts/house/13.md) — 10% (state house)
- [FL House District 14](/us/states/fl/districts/house/14.md) — 9% (state house)
- [FL House District 16](/us/states/fl/districts/house/16.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
