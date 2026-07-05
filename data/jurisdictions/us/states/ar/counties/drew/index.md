---
type: Jurisdiction
title: "Drew County, AR"
classification: county
fips: "05043"
state: "AR"
demographics:
  population: 17046
  population_under_18: 3743
  population_18_64: 10196
  population_65_plus: 3107
  median_household_income: 42824
  poverty_rate: 22.4
  homeownership_rate: 63.72
  unemployment_rate: 5.89
  median_home_value: 140800
  gini_index: 0.5301
  vacancy_rate: 13.19
  race_white: 11061
  race_black: 4611
  race_asian: 129
  race_native: 0
  hispanic: 756
  bachelors_plus: 3875
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.9494
  - to: "us/states/ar/districts/senate/8"
    rel: in-district
    area_weight: 0.0506
  - to: "us/states/ar/districts/house/94"
    rel: in-district
    area_weight: 0.9301
  - to: "us/states/ar/districts/house/93"
    rel: in-district
    area_weight: 0.0697
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Drew County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17046 |
| Under 18 | 3743 |
| 18–64 | 10196 |
| 65+ | 3107 |
| Median household income | 42824 |
| Poverty rate | 22.4 |
| Homeownership rate | 63.72 |
| Unemployment rate | 5.89 |
| Median home value | 140800 |
| Gini index | 0.5301 |
| Vacancy rate | 13.19 |
| White | 11061 |
| Black | 4611 |
| Asian | 129 |
| Native | 0 |
| Hispanic/Latino | 756 |
| Bachelor's or higher | 3875 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 95% (state senate)
- [AR Senate District 8](/us/states/ar/districts/senate/8.md) — 5% (state senate)
- [AR House District 94](/us/states/ar/districts/house/94.md) — 93% (state house)
- [AR House District 93](/us/states/ar/districts/house/93.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
