---
type: Jurisdiction
title: "Austin County, TX"
classification: county
fips: "48015"
state: "TX"
demographics:
  population: 31170
  population_under_18: 7302
  population_18_64: 17312
  population_65_plus: 6556
  median_household_income: 75789
  poverty_rate: 11.95
  homeownership_rate: 76.51
  unemployment_rate: 4.35
  median_home_value: 296900
  gini_index: 0.4393
  vacancy_rate: 15.3
  race_white: 20766
  race_black: 2463
  race_asian: 257
  race_native: 115
  hispanic: 8661
  bachelors_plus: 6815
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/85"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Austin County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31170 |
| Under 18 | 7302 |
| 18–64 | 17312 |
| 65+ | 6556 |
| Median household income | 75789 |
| Poverty rate | 11.95 |
| Homeownership rate | 76.51 |
| Unemployment rate | 4.35 |
| Median home value | 296900 |
| Gini index | 0.4393 |
| Vacancy rate | 15.3 |
| White | 20766 |
| Black | 2463 |
| Asian | 257 |
| Native | 115 |
| Hispanic/Latino | 8661 |
| Bachelor's or higher | 6815 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 85](/us/states/tx/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
