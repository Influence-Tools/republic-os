---
type: Jurisdiction
title: "Reynolds County, MO"
classification: county
fips: "29179"
state: "MO"
demographics:
  population: 6010
  population_under_18: 1141
  population_18_64: 3445
  population_65_plus: 1424
  median_household_income: 45028
  poverty_rate: 17.32
  homeownership_rate: 79.83
  unemployment_rate: 10.91
  median_home_value: 151700
  gini_index: 0.4412
  vacancy_rate: 32.53
  race_white: 5503
  race_black: 89
  race_asian: 14
  race_native: 14
  hispanic: 104
  bachelors_plus: 831
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Reynolds County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6010 |
| Under 18 | 1141 |
| 18–64 | 3445 |
| 65+ | 1424 |
| Median household income | 45028 |
| Poverty rate | 17.32 |
| Homeownership rate | 79.83 |
| Unemployment rate | 10.91 |
| Median home value | 151700 |
| Gini index | 0.4412 |
| Vacancy rate | 32.53 |
| White | 5503 |
| Black | 89 |
| Asian | 14 |
| Native | 14 |
| Hispanic/Latino | 104 |
| Bachelor's or higher | 831 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
