---
type: Jurisdiction
title: "Clark County, AR"
classification: county
fips: "05019"
state: "AR"
demographics:
  population: 21125
  population_under_18: 4240
  population_18_64: 13415
  population_65_plus: 3470
  median_household_income: 52034
  poverty_rate: 21.55
  homeownership_rate: 64.99
  unemployment_rate: 3.81
  median_home_value: 155000
  gini_index: 0.4795
  vacancy_rate: 19.02
  race_white: 14681
  race_black: 4927
  race_asian: 171
  race_native: 19
  hispanic: 1179
  bachelors_plus: 4385
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/89"
    rel: in-district
    area_weight: 0.9184
  - to: "us/states/ar/districts/house/90"
    rel: in-district
    area_weight: 0.0814
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Clark County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21125 |
| Under 18 | 4240 |
| 18–64 | 13415 |
| 65+ | 3470 |
| Median household income | 52034 |
| Poverty rate | 21.55 |
| Homeownership rate | 64.99 |
| Unemployment rate | 3.81 |
| Median home value | 155000 |
| Gini index | 0.4795 |
| Vacancy rate | 19.02 |
| White | 14681 |
| Black | 4927 |
| Asian | 171 |
| Native | 19 |
| Hispanic/Latino | 1179 |
| Bachelor's or higher | 4385 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 100% (state senate)
- [AR House District 89](/us/states/ar/districts/house/89.md) — 92% (state house)
- [AR House District 90](/us/states/ar/districts/house/90.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
