---
type: Jurisdiction
title: "Turner County, SD"
classification: county
fips: "46125"
state: "SD"
demographics:
  population: 8882
  population_under_18: 2430
  population_18_64: 2499
  population_65_plus: 3953
  median_household_income: 75771
  poverty_rate: 9.32
  homeownership_rate: 78.95
  unemployment_rate: 2.16
  median_home_value: 222900
  gini_index: 0.4
  vacancy_rate: 8.82
  race_white: 8299
  race_black: 37
  race_asian: 27
  race_native: 67
  hispanic: 314
  bachelors_plus: 2079
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/16"
    rel: in-district
    area_weight: 0.8245
  - to: "us/states/sd/districts/senate/19"
    rel: in-district
    area_weight: 0.1754
  - to: "us/states/sd/districts/house/16"
    rel: in-district
    area_weight: 0.8245
  - to: "us/states/sd/districts/house/19"
    rel: in-district
    area_weight: 0.1754
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Turner County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8882 |
| Under 18 | 2430 |
| 18–64 | 2499 |
| 65+ | 3953 |
| Median household income | 75771 |
| Poverty rate | 9.32 |
| Homeownership rate | 78.95 |
| Unemployment rate | 2.16 |
| Median home value | 222900 |
| Gini index | 0.4 |
| Vacancy rate | 8.82 |
| White | 8299 |
| Black | 37 |
| Asian | 27 |
| Native | 67 |
| Hispanic/Latino | 314 |
| Bachelor's or higher | 2079 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 16](/us/states/sd/districts/senate/16.md) — 82% (state senate)
- [SD Senate District 19](/us/states/sd/districts/senate/19.md) — 18% (state senate)
- [SD House District 16](/us/states/sd/districts/house/16.md) — 82% (state house)
- [SD House District 19](/us/states/sd/districts/house/19.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
