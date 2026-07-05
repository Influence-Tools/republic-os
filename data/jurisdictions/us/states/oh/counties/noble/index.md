---
type: Jurisdiction
title: "Noble County, OH"
classification: county
fips: "39121"
state: "OH"
demographics:
  population: 14282
  population_under_18: 2712
  population_18_64: 7327
  population_65_plus: 4243
  median_household_income: 56098
  poverty_rate: 10.61
  homeownership_rate: 83.55
  unemployment_rate: 1.43
  median_home_value: 163600
  gini_index: 0.4811
  vacancy_rate: 20.33
  race_white: 13161
  race_black: 620
  race_asian: 60
  race_native: 17
  hispanic: 247
  bachelors_plus: 2345
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/95"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Noble County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14282 |
| Under 18 | 2712 |
| 18–64 | 7327 |
| 65+ | 4243 |
| Median household income | 56098 |
| Poverty rate | 10.61 |
| Homeownership rate | 83.55 |
| Unemployment rate | 1.43 |
| Median home value | 163600 |
| Gini index | 0.4811 |
| Vacancy rate | 20.33 |
| White | 13161 |
| Black | 620 |
| Asian | 60 |
| Native | 17 |
| Hispanic/Latino | 247 |
| Bachelor's or higher | 2345 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
