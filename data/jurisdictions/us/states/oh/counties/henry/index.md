---
type: Jurisdiction
title: "Henry County, OH"
classification: county
fips: "39069"
state: "OH"
demographics:
  population: 27567
  population_under_18: 6432
  population_18_64: 15643
  population_65_plus: 5492
  median_household_income: 80099
  poverty_rate: 8.75
  homeownership_rate: 82.53
  unemployment_rate: 3.87
  median_home_value: 168600
  gini_index: 0.444
  vacancy_rate: 5.33
  race_white: 24924
  race_black: 138
  race_asian: 42
  race_native: 128
  hispanic: 2280
  bachelors_plus: 4933
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/81"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Henry County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27567 |
| Under 18 | 6432 |
| 18–64 | 15643 |
| 65+ | 5492 |
| Median household income | 80099 |
| Poverty rate | 8.75 |
| Homeownership rate | 82.53 |
| Unemployment rate | 3.87 |
| Median home value | 168600 |
| Gini index | 0.444 |
| Vacancy rate | 5.33 |
| White | 24924 |
| Black | 138 |
| Asian | 42 |
| Native | 128 |
| Hispanic/Latino | 2280 |
| Bachelor's or higher | 4933 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 100% (congressional)
- [OH Senate District 1](/us/states/oh/districts/senate/1.md) — 100% (state senate)
- [OH House District 81](/us/states/oh/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
