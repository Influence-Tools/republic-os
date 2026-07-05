---
type: Jurisdiction
title: "Pike County, IN"
classification: county
fips: "18125"
state: "IN"
demographics:
  population: 12154
  population_under_18: 2675
  population_18_64: 6865
  population_65_plus: 2614
  median_household_income: 71334
  poverty_rate: 10.68
  homeownership_rate: 86.66
  unemployment_rate: 3.17
  median_home_value: 154900
  gini_index: 0.4087
  vacancy_rate: 10.16
  race_white: 11620
  race_black: 52
  race_asian: 6
  race_native: 113
  hispanic: 138
  bachelors_plus: 1796
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/48"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/75"
    rel: in-district
    area_weight: 0.7802
  - to: "us/states/in/districts/house/63"
    rel: in-district
    area_weight: 0.2197
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Pike County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12154 |
| Under 18 | 2675 |
| 18–64 | 6865 |
| 65+ | 2614 |
| Median household income | 71334 |
| Poverty rate | 10.68 |
| Homeownership rate | 86.66 |
| Unemployment rate | 3.17 |
| Median home value | 154900 |
| Gini index | 0.4087 |
| Vacancy rate | 10.16 |
| White | 11620 |
| Black | 52 |
| Asian | 6 |
| Native | 113 |
| Hispanic/Latino | 138 |
| Bachelor's or higher | 1796 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 48](/us/states/in/districts/senate/48.md) — 100% (state senate)
- [IN House District 75](/us/states/in/districts/house/75.md) — 78% (state house)
- [IN House District 63](/us/states/in/districts/house/63.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
