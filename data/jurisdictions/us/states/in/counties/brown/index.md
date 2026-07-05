---
type: Jurisdiction
title: "Brown County, IN"
classification: county
fips: "18013"
state: "IN"
demographics:
  population: 15606
  population_under_18: 2593
  population_18_64: 8859
  population_65_plus: 4154
  median_household_income: 78528
  poverty_rate: 7.78
  homeownership_rate: 86.61
  unemployment_rate: 2.15
  median_home_value: 269100
  gini_index: 0.4314
  vacancy_rate: 20.94
  race_white: 14706
  race_black: 46
  race_asian: 86
  race_native: 145
  hispanic: 304
  bachelors_plus: 4608
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/44"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/62"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Brown County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15606 |
| Under 18 | 2593 |
| 18–64 | 8859 |
| 65+ | 4154 |
| Median household income | 78528 |
| Poverty rate | 7.78 |
| Homeownership rate | 86.61 |
| Unemployment rate | 2.15 |
| Median home value | 269100 |
| Gini index | 0.4314 |
| Vacancy rate | 20.94 |
| White | 14706 |
| Black | 46 |
| Asian | 86 |
| Native | 145 |
| Hispanic/Latino | 304 |
| Bachelor's or higher | 4608 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 44](/us/states/in/districts/senate/44.md) — 100% (state senate)
- [IN House District 62](/us/states/in/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
