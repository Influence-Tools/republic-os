---
type: Jurisdiction
title: "Walsh County, ND"
classification: county
fips: "38099"
state: "ND"
demographics:
  population: 10396
  population_under_18: 2435
  population_18_64: 5685
  population_65_plus: 2276
  median_household_income: 71944
  poverty_rate: 11.22
  homeownership_rate: 76.05
  unemployment_rate: 1.97
  median_home_value: 132700
  gini_index: 0.3946
  vacancy_rate: 15.12
  race_white: 8657
  race_black: 85
  race_asian: 94
  race_native: 134
  hispanic: 1363
  bachelors_plus: 1810
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/nd/districts/senate/19"
    rel: in-district
    area_weight: 0.8349
  - to: "us/states/nd/districts/senate/20"
    rel: in-district
    area_weight: 0.1649
  - to: "us/states/nd/districts/house/19"
    rel: in-district
    area_weight: 0.8349
  - to: "us/states/nd/districts/house/20"
    rel: in-district
    area_weight: 0.1649
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Walsh County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10396 |
| Under 18 | 2435 |
| 18–64 | 5685 |
| 65+ | 2276 |
| Median household income | 71944 |
| Poverty rate | 11.22 |
| Homeownership rate | 76.05 |
| Unemployment rate | 1.97 |
| Median home value | 132700 |
| Gini index | 0.3946 |
| Vacancy rate | 15.12 |
| White | 8657 |
| Black | 85 |
| Asian | 94 |
| Native | 134 |
| Hispanic/Latino | 1363 |
| Bachelor's or higher | 1810 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 19](/us/states/nd/districts/senate/19.md) — 83% (state senate)
- [ND Senate District 20](/us/states/nd/districts/senate/20.md) — 16% (state senate)
- [ND House District 19](/us/states/nd/districts/house/19.md) — 83% (state house)
- [ND House District 20](/us/states/nd/districts/house/20.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
