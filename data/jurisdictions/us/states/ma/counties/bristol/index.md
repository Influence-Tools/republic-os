---
type: Jurisdiction
title: "Bristol County, MA"
classification: county
fips: "25005"
state: "MA"
demographics:
  population: 582270
  population_under_18: 119489
  population_18_64: 359313
  population_65_plus: 103468
  median_household_income: 85625
  poverty_rate: 11.32
  homeownership_rate: 62.29
  unemployment_rate: 5.46
  median_home_value: 451200
  gini_index: 0.4576
  vacancy_rate: 4.57
  race_white: 447540
  race_black: 25982
  race_asian: 14233
  race_native: 1323
  hispanic: 59389
  bachelors_plus: 174153
districts:
  - to: "us/states/ma/districts/04"
    rel: in-district
    area_weight: 0.545
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.2673
  - to: "us/states/ma/districts/08"
    rel: in-district
    area_weight: 0.0425
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Bristol County, MA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 582270 |
| Under 18 | 119489 |
| 18–64 | 359313 |
| 65+ | 103468 |
| Median household income | 85625 |
| Poverty rate | 11.32 |
| Homeownership rate | 62.29 |
| Unemployment rate | 5.46 |
| Median home value | 451200 |
| Gini index | 0.4576 |
| Vacancy rate | 4.57 |
| White | 447540 |
| Black | 25982 |
| Asian | 14233 |
| Native | 1323 |
| Hispanic/Latino | 59389 |
| Bachelor's or higher | 174153 |

## Districts

- [MA-04](/us/states/ma/districts/04.md) — 55% (congressional)
- [MA-09](/us/states/ma/districts/09.md) — 27% (congressional)
- [MA-08](/us/states/ma/districts/08.md) — 4% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
