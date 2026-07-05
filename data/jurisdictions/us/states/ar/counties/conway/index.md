---
type: Jurisdiction
title: "Conway County, AR"
classification: county
fips: "05029"
state: "AR"
demographics:
  population: 21054
  population_under_18: 4758
  population_18_64: 12138
  population_65_plus: 4158
  median_household_income: 54187
  poverty_rate: 19.71
  homeownership_rate: 74.08
  unemployment_rate: 6.41
  median_home_value: 154100
  gini_index: 0.4398
  vacancy_rate: 14.68
  race_white: 17024
  race_black: 2428
  race_asian: 54
  race_native: 90
  hispanic: 1000
  bachelors_plus: 3778
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ar/districts/senate/25"
    rel: in-district
    area_weight: 0.8909
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.1089
  - to: "us/states/ar/districts/house/43"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Conway County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21054 |
| Under 18 | 4758 |
| 18–64 | 12138 |
| 65+ | 4158 |
| Median household income | 54187 |
| Poverty rate | 19.71 |
| Homeownership rate | 74.08 |
| Unemployment rate | 6.41 |
| Median home value | 154100 |
| Gini index | 0.4398 |
| Vacancy rate | 14.68 |
| White | 17024 |
| Black | 2428 |
| Asian | 54 |
| Native | 90 |
| Hispanic/Latino | 1000 |
| Bachelor's or higher | 3778 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 25](/us/states/ar/districts/senate/25.md) — 89% (state senate)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 11% (state senate)
- [AR House District 43](/us/states/ar/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
