---
type: Jurisdiction
title: "Uinta County, WY"
classification: county
fips: "56041"
state: "WY"
demographics:
  population: 20644
  population_under_18: 5629
  population_18_64: 11495
  population_65_plus: 3520
  median_household_income: 82980
  poverty_rate: 9.17
  homeownership_rate: 76.61
  unemployment_rate: 3.23
  median_home_value: 290000
  gini_index: 0.4642
  vacancy_rate: 13.31
  race_white: 18343
  race_black: 116
  race_asian: 49
  race_native: 40
  hispanic: 2087
  bachelors_plus: 3975
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wy/districts/senate/15"
    rel: in-district
    area_weight: 0.7545
  - to: "us/states/wy/districts/senate/14"
    rel: in-district
    area_weight: 0.2451
  - to: "us/states/wy/districts/house/19"
    rel: in-district
    area_weight: 0.751
  - to: "us/states/wy/districts/house/18"
    rel: in-district
    area_weight: 0.2451
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Uinta County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20644 |
| Under 18 | 5629 |
| 18–64 | 11495 |
| 65+ | 3520 |
| Median household income | 82980 |
| Poverty rate | 9.17 |
| Homeownership rate | 76.61 |
| Unemployment rate | 3.23 |
| Median home value | 290000 |
| Gini index | 0.4642 |
| Vacancy rate | 13.31 |
| White | 18343 |
| Black | 116 |
| Asian | 49 |
| Native | 40 |
| Hispanic/Latino | 2087 |
| Bachelor's or higher | 3975 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 15](/us/states/wy/districts/senate/15.md) — 75% (state senate)
- [WY Senate District 14](/us/states/wy/districts/senate/14.md) — 25% (state senate)
- [WY House District 19](/us/states/wy/districts/house/19.md) — 75% (state house)
- [WY House District 18](/us/states/wy/districts/house/18.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
