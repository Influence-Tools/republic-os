---
type: Jurisdiction
title: "Wilson County, TX"
classification: county
fips: "48493"
state: "TX"
demographics:
  population: 52781
  population_under_18: 12395
  population_18_64: 31347
  population_65_plus: 9039
  median_household_income: 94565
  poverty_rate: 11.31
  homeownership_rate: 84.75
  unemployment_rate: 3.57
  median_home_value: 321300
  gini_index: 0.4267
  vacancy_rate: 6.65
  race_white: 35805
  race_black: 1041
  race_asian: 336
  race_native: 263
  hispanic: 21077
  bachelors_plus: 12279
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
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

# Wilson County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52781 |
| Under 18 | 12395 |
| 18–64 | 31347 |
| 65+ | 9039 |
| Median household income | 94565 |
| Poverty rate | 11.31 |
| Homeownership rate | 84.75 |
| Unemployment rate | 3.57 |
| Median home value | 321300 |
| Gini index | 0.4267 |
| Vacancy rate | 6.65 |
| White | 35805 |
| Black | 1041 |
| Asian | 336 |
| Native | 263 |
| Hispanic/Latino | 21077 |
| Bachelor's or higher | 12279 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
