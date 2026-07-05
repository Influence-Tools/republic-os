---
type: Jurisdiction
title: "Lancaster County, SC"
classification: county
fips: "45057"
state: "SC"
demographics:
  population: 104475
  population_under_18: 22523
  population_18_64: 59217
  population_65_plus: 22735
  median_household_income: 78869
  poverty_rate: 11.42
  homeownership_rate: 83.26
  unemployment_rate: 4.29
  median_home_value: 329900
  gini_index: 0.4607
  vacancy_rate: 8.45
  race_white: 71819
  race_black: 20156
  race_asian: 2636
  race_native: 113
  hispanic: 7808
  bachelors_plus: 33979
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/sc/districts/senate/27"
    rel: in-district
    area_weight: 0.8584
  - to: "us/states/sc/districts/senate/16"
    rel: in-district
    area_weight: 0.0711
  - to: "us/states/sc/districts/senate/17"
    rel: in-district
    area_weight: 0.0704
  - to: "us/states/sc/districts/house/45"
    rel: in-district
    area_weight: 0.4677
  - to: "us/states/sc/districts/house/65"
    rel: in-district
    area_weight: 0.2535
  - to: "us/states/sc/districts/house/53"
    rel: in-district
    area_weight: 0.1738
  - to: "us/states/sc/districts/house/44"
    rel: in-district
    area_weight: 0.1047
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Lancaster County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104475 |
| Under 18 | 22523 |
| 18–64 | 59217 |
| 65+ | 22735 |
| Median household income | 78869 |
| Poverty rate | 11.42 |
| Homeownership rate | 83.26 |
| Unemployment rate | 4.29 |
| Median home value | 329900 |
| Gini index | 0.4607 |
| Vacancy rate | 8.45 |
| White | 71819 |
| Black | 20156 |
| Asian | 2636 |
| Native | 113 |
| Hispanic/Latino | 7808 |
| Bachelor's or higher | 33979 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 27](/us/states/sc/districts/senate/27.md) — 86% (state senate)
- [SC Senate District 16](/us/states/sc/districts/senate/16.md) — 7% (state senate)
- [SC Senate District 17](/us/states/sc/districts/senate/17.md) — 7% (state senate)
- [SC House District 45](/us/states/sc/districts/house/45.md) — 47% (state house)
- [SC House District 65](/us/states/sc/districts/house/65.md) — 25% (state house)
- [SC House District 53](/us/states/sc/districts/house/53.md) — 17% (state house)
- [SC House District 44](/us/states/sc/districts/house/44.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
