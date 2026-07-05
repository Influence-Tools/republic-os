---
type: Jurisdiction
title: "Grant County, WV"
classification: county
fips: "54023"
state: "WV"
demographics:
  population: 10983
  population_under_18: 2156
  population_18_64: 6055
  population_65_plus: 2772
  median_household_income: 62361
  poverty_rate: 13.26
  homeownership_rate: 81.08
  unemployment_rate: 3.28
  median_home_value: 175100
  gini_index: 0.4345
  vacancy_rate: 22.52
  race_white: 10547
  race_black: 185
  race_asian: 19
  race_native: 0
  hispanic: 79
  bachelors_plus: 1545
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/wv/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/house/85"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Grant County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10983 |
| Under 18 | 2156 |
| 18–64 | 6055 |
| 65+ | 2772 |
| Median household income | 62361 |
| Poverty rate | 13.26 |
| Homeownership rate | 81.08 |
| Unemployment rate | 3.28 |
| Median home value | 175100 |
| Gini index | 0.4345 |
| Vacancy rate | 22.52 |
| White | 10547 |
| Black | 185 |
| Asian | 19 |
| Native | 0 |
| Hispanic/Latino | 79 |
| Bachelor's or higher | 1545 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 14](/us/states/wv/districts/senate/14.md) — 100% (state senate)
- [WV House District 85](/us/states/wv/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
