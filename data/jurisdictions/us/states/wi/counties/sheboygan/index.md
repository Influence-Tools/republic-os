---
type: Jurisdiction
title: "Sheboygan County, WI"
classification: county
fips: "55117"
state: "WI"
demographics:
  population: 117991
  population_under_18: 25396
  population_18_64: 69470
  population_65_plus: 23125
  median_household_income: 73094
  poverty_rate: 8.54
  homeownership_rate: 71.48
  unemployment_rate: 2.74
  median_home_value: 232700
  gini_index: 0.4143
  vacancy_rate: 6.3
  race_white: 98331
  race_black: 2547
  race_asian: 6812
  race_native: 229
  hispanic: 9148
  bachelors_plus: 30481
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.4073
  - to: "us/states/wi/districts/senate/9"
    rel: in-district
    area_weight: 0.3161
  - to: "us/states/wi/districts/senate/20"
    rel: in-district
    area_weight: 0.091
  - to: "us/states/wi/districts/house/27"
    rel: in-district
    area_weight: 0.2618
  - to: "us/states/wi/districts/house/59"
    rel: in-district
    area_weight: 0.091
  - to: "us/states/wi/districts/house/26"
    rel: in-district
    area_weight: 0.0346
  - to: "us/states/wi/districts/house/25"
    rel: in-district
    area_weight: 0.0198
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Sheboygan County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 117991 |
| Under 18 | 25396 |
| 18–64 | 69470 |
| 65+ | 23125 |
| Median household income | 73094 |
| Poverty rate | 8.54 |
| Homeownership rate | 71.48 |
| Unemployment rate | 2.74 |
| Median home value | 232700 |
| Gini index | 0.4143 |
| Vacancy rate | 6.3 |
| White | 98331 |
| Black | 2547 |
| Asian | 6812 |
| Native | 229 |
| Hispanic/Latino | 9148 |
| Bachelor's or higher | 30481 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 41% (congressional)
- [WI Senate District 9](/us/states/wi/districts/senate/9.md) — 32% (state senate)
- [WI Senate District 20](/us/states/wi/districts/senate/20.md) — 9% (state senate)
- [WI House District 27](/us/states/wi/districts/house/27.md) — 26% (state house)
- [WI House District 59](/us/states/wi/districts/house/59.md) — 9% (state house)
- [WI House District 26](/us/states/wi/districts/house/26.md) — 3% (state house)
- [WI House District 25](/us/states/wi/districts/house/25.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
