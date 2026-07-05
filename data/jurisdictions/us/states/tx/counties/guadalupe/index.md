---
type: Jurisdiction
title: "Guadalupe County, TX"
classification: county
fips: "48187"
state: "TX"
demographics:
  population: 183642
  population_under_18: 44233
  population_18_64: 112205
  population_65_plus: 27204
  median_household_income: 92375
  poverty_rate: 9.31
  homeownership_rate: 77.82
  unemployment_rate: 4.76
  median_home_value: 304400
  gini_index: 0.4019
  vacancy_rate: 6.13
  race_white: 101276
  race_black: 14514
  race_asian: 3140
  race_native: 983
  hispanic: 71699
  bachelors_plus: 52298
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.7863
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.2113
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.601
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 0.2322
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.1668
  - to: "us/states/tx/districts/house/44"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Guadalupe County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 183642 |
| Under 18 | 44233 |
| 18–64 | 112205 |
| 65+ | 27204 |
| Median household income | 92375 |
| Poverty rate | 9.31 |
| Homeownership rate | 77.82 |
| Unemployment rate | 4.76 |
| Median home value | 304400 |
| Gini index | 0.4019 |
| Vacancy rate | 6.13 |
| White | 101276 |
| Black | 14514 |
| Asian | 3140 |
| Native | 983 |
| Hispanic/Latino | 71699 |
| Bachelor's or higher | 52298 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 79% (congressional)
- [TX-28](/us/states/tx/districts/28.md) — 21% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 60% (state senate)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 23% (state senate)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 17% (state senate)
- [TX House District 44](/us/states/tx/districts/house/44.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
