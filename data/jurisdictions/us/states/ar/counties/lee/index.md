---
type: Jurisdiction
title: "Lee County, AR"
classification: county
fips: "05077"
state: "AR"
demographics:
  population: 8359
  population_under_18: 1581
  population_18_64: 5071
  population_65_plus: 1707
  median_household_income: 34375
  poverty_rate: 39.44
  homeownership_rate: 58.96
  unemployment_rate: 19.1
  median_home_value: 75300
  gini_index: 0.6137
  vacancy_rate: 27.18
  race_white: 3409
  race_black: 4573
  race_asian: 0
  race_native: 0
  hispanic: 263
  bachelors_plus: 549
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ar/districts/senate/9"
    rel: in-district
    area_weight: 0.5494
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.4503
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Lee County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8359 |
| Under 18 | 1581 |
| 18–64 | 5071 |
| 65+ | 1707 |
| Median household income | 34375 |
| Poverty rate | 39.44 |
| Homeownership rate | 58.96 |
| Unemployment rate | 19.1 |
| Median home value | 75300 |
| Gini index | 0.6137 |
| Vacancy rate | 27.18 |
| White | 3409 |
| Black | 4573 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 263 |
| Bachelor's or higher | 549 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 9](/us/states/ar/districts/senate/9.md) — 55% (state senate)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 45% (state senate)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
