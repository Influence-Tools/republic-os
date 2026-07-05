---
type: Jurisdiction
title: "Norton city, VA"
classification: county
fips: "51720"
state: "VA"
demographics:
  population: 3577
  population_under_18: 926
  population_18_64: 1062
  population_65_plus: 1589
  median_household_income: 41495
  poverty_rate: 26.31
  homeownership_rate: 49.97
  unemployment_rate: 3.83
  median_home_value: 110000
  gini_index: 0.4949
  vacancy_rate: 9.01
  race_white: 3275
  race_black: 79
  race_asian: 11
  race_native: 0
  hispanic: 112
  bachelors_plus: 534
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/45"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Norton city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3577 |
| Under 18 | 926 |
| 18–64 | 1062 |
| 65+ | 1589 |
| Median household income | 41495 |
| Poverty rate | 26.31 |
| Homeownership rate | 49.97 |
| Unemployment rate | 3.83 |
| Median home value | 110000 |
| Gini index | 0.4949 |
| Vacancy rate | 9.01 |
| White | 3275 |
| Black | 79 |
| Asian | 11 |
| Native | 0 |
| Hispanic/Latino | 112 |
| Bachelor's or higher | 534 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 45](/us/states/va/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
