---
type: Jurisdiction
title: "Monroe County, PA"
classification: county
fips: "42089"
state: "PA"
demographics:
  population: 167515
  population_under_18: 32041
  population_18_64: 102693
  population_65_plus: 32781
  median_household_income: 83565
  poverty_rate: 10.68
  homeownership_rate: 80.23
  unemployment_rate: 6.9
  median_home_value: 267600
  gini_index: 0.4277
  vacancy_rate: 23.11
  race_white: 106651
  race_black: 23309
  race_asian: 4388
  race_native: 366
  hispanic: 30408
  bachelors_plus: 45422
districts:
  - to: "us/states/pa/districts/08"
    rel: in-district
    area_weight: 0.8846
  - to: "us/states/pa/districts/07"
    rel: in-district
    area_weight: 0.1152
  - to: "us/states/pa/districts/senate/40"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/house/176"
    rel: in-district
    area_weight: 0.4466
  - to: "us/states/pa/districts/house/115"
    rel: in-district
    area_weight: 0.4319
  - to: "us/states/pa/districts/house/189"
    rel: in-district
    area_weight: 0.1211
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Monroe County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 167515 |
| Under 18 | 32041 |
| 18–64 | 102693 |
| 65+ | 32781 |
| Median household income | 83565 |
| Poverty rate | 10.68 |
| Homeownership rate | 80.23 |
| Unemployment rate | 6.9 |
| Median home value | 267600 |
| Gini index | 0.4277 |
| Vacancy rate | 23.11 |
| White | 106651 |
| Black | 23309 |
| Asian | 4388 |
| Native | 366 |
| Hispanic/Latino | 30408 |
| Bachelor's or higher | 45422 |

## Districts

- [PA-08](/us/states/pa/districts/08.md) — 88% (congressional)
- [PA-07](/us/states/pa/districts/07.md) — 12% (congressional)
- [PA Senate District 40](/us/states/pa/districts/senate/40.md) — 100% (state senate)
- [PA House District 176](/us/states/pa/districts/house/176.md) — 45% (state house)
- [PA House District 115](/us/states/pa/districts/house/115.md) — 43% (state house)
- [PA House District 189](/us/states/pa/districts/house/189.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
