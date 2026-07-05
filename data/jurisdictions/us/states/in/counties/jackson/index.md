---
type: Jurisdiction
title: "Jackson County, IN"
classification: county
fips: "18071"
state: "IN"
demographics:
  population: 46660
  population_under_18: 12051
  population_18_64: 27067
  population_65_plus: 7542
  median_household_income: 70262
  poverty_rate: 12.29
  homeownership_rate: 73.17
  unemployment_rate: 2.64
  median_home_value: 178300
  gini_index: 0.4033
  vacancy_rate: 6.27
  race_white: 37337
  race_black: 276
  race_asian: 1043
  race_native: 1005
  hispanic: 6707
  bachelors_plus: 8074
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/44"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/house/69"
    rel: in-district
    area_weight: 0.6678
  - to: "us/states/in/districts/house/62"
    rel: in-district
    area_weight: 0.2505
  - to: "us/states/in/districts/house/65"
    rel: in-district
    area_weight: 0.0816
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Jackson County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46660 |
| Under 18 | 12051 |
| 18–64 | 27067 |
| 65+ | 7542 |
| Median household income | 70262 |
| Poverty rate | 12.29 |
| Homeownership rate | 73.17 |
| Unemployment rate | 2.64 |
| Median home value | 178300 |
| Gini index | 0.4033 |
| Vacancy rate | 6.27 |
| White | 37337 |
| Black | 276 |
| Asian | 1043 |
| Native | 1005 |
| Hispanic/Latino | 6707 |
| Bachelor's or higher | 8074 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 44](/us/states/in/districts/senate/44.md) — 100% (state senate)
- [IN House District 69](/us/states/in/districts/house/69.md) — 67% (state house)
- [IN House District 62](/us/states/in/districts/house/62.md) — 25% (state house)
- [IN House District 65](/us/states/in/districts/house/65.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
