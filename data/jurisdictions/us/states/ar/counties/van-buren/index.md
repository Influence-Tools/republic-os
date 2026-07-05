---
type: Jurisdiction
title: "Van Buren County, AR"
classification: county
fips: "05141"
state: "AR"
demographics:
  population: 15998
  population_under_18: 3076
  population_18_64: 8585
  population_65_plus: 4337
  median_household_income: 50354
  poverty_rate: 19.12
  homeownership_rate: 77.88
  unemployment_rate: 3.78
  median_home_value: 135700
  gini_index: 0.4268
  vacancy_rate: 23.58
  race_white: 14811
  race_black: 68
  race_asian: 63
  race_native: 105
  hispanic: 551
  bachelors_plus: 2430
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/43"
    rel: in-district
    area_weight: 0.5448
  - to: "us/states/ar/districts/house/42"
    rel: in-district
    area_weight: 0.2485
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Van Buren County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15998 |
| Under 18 | 3076 |
| 18–64 | 8585 |
| 65+ | 4337 |
| Median household income | 50354 |
| Poverty rate | 19.12 |
| Homeownership rate | 77.88 |
| Unemployment rate | 3.78 |
| Median home value | 135700 |
| Gini index | 0.4268 |
| Vacancy rate | 23.58 |
| White | 14811 |
| Black | 68 |
| Asian | 63 |
| Native | 105 |
| Hispanic/Latino | 551 |
| Bachelor's or higher | 2430 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 24](/us/states/ar/districts/senate/24.md) — 100% (state senate)
- [AR House District 43](/us/states/ar/districts/house/43.md) — 54% (state house)
- [AR House District 42](/us/states/ar/districts/house/42.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
