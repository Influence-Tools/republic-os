---
type: Jurisdiction
title: "Sumter County, AL"
classification: county
fips: "01119"
state: "AL"
demographics:
  population: 11878
  population_under_18: 3741
  population_18_64: 3348
  population_65_plus: 4789
  median_household_income: 33310
  poverty_rate: 26.46
  homeownership_rate: 66.85
  unemployment_rate: 12.11
  median_home_value: 82600
  gini_index: 0.5
  vacancy_rate: 24.12
  race_white: 3097
  race_black: 8097
  race_asian: 32
  race_native: 13
  hispanic: 87
  bachelors_plus: 1992
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/71"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Sumter County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11878 |
| Under 18 | 3741 |
| 18–64 | 3348 |
| 65+ | 4789 |
| Median household income | 33310 |
| Poverty rate | 26.46 |
| Homeownership rate | 66.85 |
| Unemployment rate | 12.11 |
| Median home value | 82600 |
| Gini index | 0.5 |
| Vacancy rate | 24.12 |
| White | 3097 |
| Black | 8097 |
| Asian | 32 |
| Native | 13 |
| Hispanic/Latino | 87 |
| Bachelor's or higher | 1992 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 100% (state senate)
- [AL House District 71](/us/states/al/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
