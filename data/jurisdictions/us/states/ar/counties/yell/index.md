---
type: Jurisdiction
title: "Yell County, AR"
classification: county
fips: "05149"
state: "AR"
demographics:
  population: 20134
  population_under_18: 4835
  population_18_64: 11741
  population_65_plus: 3558
  median_household_income: 55934
  poverty_rate: 15.64
  homeownership_rate: 67.55
  unemployment_rate: 3.38
  median_home_value: 143600
  gini_index: 0.4179
  vacancy_rate: 10.62
  race_white: 15775
  race_black: 308
  race_asian: 281
  race_native: 124
  hispanic: 4277
  bachelors_plus: 2639
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.9941
  - to: "us/states/ar/districts/senate/25"
    rel: in-district
    area_weight: 0.0059
  - to: "us/states/ar/districts/house/52"
    rel: in-district
    area_weight: 0.7909
  - to: "us/states/ar/districts/house/54"
    rel: in-district
    area_weight: 0.2089
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Yell County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20134 |
| Under 18 | 4835 |
| 18–64 | 11741 |
| 65+ | 3558 |
| Median household income | 55934 |
| Poverty rate | 15.64 |
| Homeownership rate | 67.55 |
| Unemployment rate | 3.38 |
| Median home value | 143600 |
| Gini index | 0.4179 |
| Vacancy rate | 10.62 |
| White | 15775 |
| Black | 308 |
| Asian | 281 |
| Native | 124 |
| Hispanic/Latino | 4277 |
| Bachelor's or higher | 2639 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 99% (state senate)
- [AR Senate District 25](/us/states/ar/districts/senate/25.md) — 1% (state senate)
- [AR House District 52](/us/states/ar/districts/house/52.md) — 79% (state house)
- [AR House District 54](/us/states/ar/districts/house/54.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
