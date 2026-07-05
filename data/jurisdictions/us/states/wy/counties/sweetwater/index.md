---
type: Jurisdiction
title: "Sweetwater County, WY"
classification: county
fips: "56037"
state: "WY"
demographics:
  population: 41542
  population_under_18: 10377
  population_18_64: 25034
  population_65_plus: 6131
  median_household_income: 75034
  poverty_rate: 12.86
  homeownership_rate: 74.56
  unemployment_rate: 5.59
  median_home_value: 251400
  gini_index: 0.4485
  vacancy_rate: 9.26
  race_white: 33545
  race_black: 566
  race_asian: 197
  race_native: 226
  hispanic: 6991
  bachelors_plus: 7463
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/11"
    rel: in-district
    area_weight: 0.802
  - to: "us/states/wy/districts/senate/14"
    rel: in-district
    area_weight: 0.1939
  - to: "us/states/wy/districts/house/47"
    rel: in-district
    area_weight: 0.7987
  - to: "us/states/wy/districts/house/18"
    rel: in-district
    area_weight: 0.1939
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Sweetwater County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41542 |
| Under 18 | 10377 |
| 18–64 | 25034 |
| 65+ | 6131 |
| Median household income | 75034 |
| Poverty rate | 12.86 |
| Homeownership rate | 74.56 |
| Unemployment rate | 5.59 |
| Median home value | 251400 |
| Gini index | 0.4485 |
| Vacancy rate | 9.26 |
| White | 33545 |
| Black | 566 |
| Asian | 197 |
| Native | 226 |
| Hispanic/Latino | 6991 |
| Bachelor's or higher | 7463 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 11](/us/states/wy/districts/senate/11.md) — 80% (state senate)
- [WY Senate District 14](/us/states/wy/districts/senate/14.md) — 19% (state senate)
- [WY House District 47](/us/states/wy/districts/house/47.md) — 80% (state house)
- [WY House District 18](/us/states/wy/districts/house/18.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
