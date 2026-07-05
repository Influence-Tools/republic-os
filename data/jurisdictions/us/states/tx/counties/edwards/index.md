---
type: Jurisdiction
title: "Edwards County, TX"
classification: county
fips: "48137"
state: "TX"
demographics:
  population: 1290
  population_under_18: 296
  population_18_64: 756
  population_65_plus: 238
  median_household_income: 40313
  poverty_rate: 31.87
  homeownership_rate: 87.87
  unemployment_rate: 0.0
  gini_index: 0.434
  vacancy_rate: 50.43
  race_white: 960
  race_black: 27
  race_asian: 0
  race_native: 2
  hispanic: 555
  bachelors_plus: 215
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Edwards County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1290 |
| Under 18 | 296 |
| 18–64 | 756 |
| 65+ | 238 |
| Median household income | 40313 |
| Poverty rate | 31.87 |
| Homeownership rate | 87.87 |
| Unemployment rate | 0.0 |
| Gini index | 0.434 |
| Vacancy rate | 50.43 |
| White | 960 |
| Black | 27 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 555 |
| Bachelor's or higher | 215 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
