---
type: Jurisdiction
title: "Cotton County, OK"
classification: county
fips: "40033"
state: "OK"
demographics:
  population: 5485
  population_under_18: 1253
  population_18_64: 3136
  population_65_plus: 1096
  median_household_income: 58425
  poverty_rate: 20.47
  homeownership_rate: 80.34
  unemployment_rate: 3.48
  median_home_value: 113900
  gini_index: 0.5173
  vacancy_rate: 24.36
  race_white: 4272
  race_black: 92
  race_asian: 5
  race_native: 334
  hispanic: 424
  bachelors_plus: 1185
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ok/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ok/districts/house/63"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Cotton County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5485 |
| Under 18 | 1253 |
| 18–64 | 3136 |
| 65+ | 1096 |
| Median household income | 58425 |
| Poverty rate | 20.47 |
| Homeownership rate | 80.34 |
| Unemployment rate | 3.48 |
| Median home value | 113900 |
| Gini index | 0.5173 |
| Vacancy rate | 24.36 |
| White | 4272 |
| Black | 92 |
| Asian | 5 |
| Native | 334 |
| Hispanic/Latino | 424 |
| Bachelor's or higher | 1185 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 31](/us/states/ok/districts/senate/31.md) — 100% (state senate)
- [OK House District 63](/us/states/ok/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
