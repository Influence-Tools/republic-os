---
type: Jurisdiction
title: "Winston County, MS"
classification: county
fips: "28159"
state: "MS"
demographics:
  population: 17536
  population_under_18: 3888
  population_18_64: 9847
  population_65_plus: 3801
  median_household_income: 53031
  poverty_rate: 26.86
  homeownership_rate: 73.0
  unemployment_rate: 6.72
  median_home_value: 124600
  gini_index: 0.4998
  vacancy_rate: 13.24
  race_white: 8702
  race_black: 8260
  race_asian: 18
  race_native: 208
  hispanic: 105
  bachelors_plus: 3282
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/18"
    rel: in-district
    area_weight: 0.5708
  - to: "us/states/ms/districts/senate/32"
    rel: in-district
    area_weight: 0.429
  - to: "us/states/ms/districts/house/42"
    rel: in-district
    area_weight: 0.4303
  - to: "us/states/ms/districts/house/35"
    rel: in-district
    area_weight: 0.3975
  - to: "us/states/ms/districts/house/45"
    rel: in-district
    area_weight: 0.1721
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Winston County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17536 |
| Under 18 | 3888 |
| 18–64 | 9847 |
| 65+ | 3801 |
| Median household income | 53031 |
| Poverty rate | 26.86 |
| Homeownership rate | 73.0 |
| Unemployment rate | 6.72 |
| Median home value | 124600 |
| Gini index | 0.4998 |
| Vacancy rate | 13.24 |
| White | 8702 |
| Black | 8260 |
| Asian | 18 |
| Native | 208 |
| Hispanic/Latino | 105 |
| Bachelor's or higher | 3282 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 18](/us/states/ms/districts/senate/18.md) — 57% (state senate)
- [MS Senate District 32](/us/states/ms/districts/senate/32.md) — 43% (state senate)
- [MS House District 42](/us/states/ms/districts/house/42.md) — 43% (state house)
- [MS House District 35](/us/states/ms/districts/house/35.md) — 40% (state house)
- [MS House District 45](/us/states/ms/districts/house/45.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
