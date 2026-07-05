---
type: Jurisdiction
title: "Jefferson County, MS"
classification: county
fips: "28063"
state: "MS"
demographics:
  population: 7068
  population_under_18: 1455
  population_18_64: 4186
  population_65_plus: 1427
  median_household_income: 38305
  poverty_rate: 32.49
  homeownership_rate: 82.92
  unemployment_rate: 1.84
  median_home_value: 81300
  gini_index: 0.4878
  vacancy_rate: 26.43
  race_white: 929
  race_black: 5857
  race_asian: 35
  race_native: 5
  hispanic: 143
  bachelors_plus: 921
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/ms/districts/senate/37"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/house/85"
    rel: in-district
    area_weight: 0.5588
  - to: "us/states/ms/districts/house/94"
    rel: in-district
    area_weight: 0.4409
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Jefferson County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7068 |
| Under 18 | 1455 |
| 18–64 | 4186 |
| 65+ | 1427 |
| Median household income | 38305 |
| Poverty rate | 32.49 |
| Homeownership rate | 82.92 |
| Unemployment rate | 1.84 |
| Median home value | 81300 |
| Gini index | 0.4878 |
| Vacancy rate | 26.43 |
| White | 929 |
| Black | 5857 |
| Asian | 35 |
| Native | 5 |
| Hispanic/Latino | 143 |
| Bachelor's or higher | 921 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 37](/us/states/ms/districts/senate/37.md) — 100% (state senate)
- [MS House District 85](/us/states/ms/districts/house/85.md) — 56% (state house)
- [MS House District 94](/us/states/ms/districts/house/94.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
