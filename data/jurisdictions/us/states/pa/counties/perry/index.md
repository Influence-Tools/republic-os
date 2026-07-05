---
type: Jurisdiction
title: "Perry County, PA"
classification: county
fips: "42099"
state: "PA"
demographics:
  population: 46239
  population_under_18: 9699
  population_18_64: 27064
  population_65_plus: 9476
  median_household_income: 79444
  poverty_rate: 7.99
  homeownership_rate: 81.83
  unemployment_rate: 3.13
  median_home_value: 236400
  gini_index: 0.4039
  vacancy_rate: 8.73
  race_white: 43464
  race_black: 369
  race_asian: 145
  race_native: 29
  hispanic: 1164
  bachelors_plus: 8873
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/pa/districts/senate/34"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/86"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Perry County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46239 |
| Under 18 | 9699 |
| 18–64 | 27064 |
| 65+ | 9476 |
| Median household income | 79444 |
| Poverty rate | 7.99 |
| Homeownership rate | 81.83 |
| Unemployment rate | 3.13 |
| Median home value | 236400 |
| Gini index | 0.4039 |
| Vacancy rate | 8.73 |
| White | 43464 |
| Black | 369 |
| Asian | 145 |
| Native | 29 |
| Hispanic/Latino | 1164 |
| Bachelor's or higher | 8873 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 34](/us/states/pa/districts/senate/34.md) — 100% (state senate)
- [PA House District 86](/us/states/pa/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
