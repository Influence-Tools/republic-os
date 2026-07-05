---
type: Jurisdiction
title: "Cumberland County, KY"
classification: county
fips: "21057"
state: "KY"
demographics:
  population: 5948
  population_under_18: 1312
  population_18_64: 3285
  population_65_plus: 1351
  median_household_income: 40000
  poverty_rate: 24.8
  homeownership_rate: 75.51
  unemployment_rate: 4.01
  median_home_value: 141100
  gini_index: 0.4527
  vacancy_rate: 22.74
  race_white: 5536
  race_black: 90
  race_asian: 16
  race_native: 39
  hispanic: 120
  bachelors_plus: 1152
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/21"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Cumberland County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5948 |
| Under 18 | 1312 |
| 18–64 | 3285 |
| 65+ | 1351 |
| Median household income | 40000 |
| Poverty rate | 24.8 |
| Homeownership rate | 75.51 |
| Unemployment rate | 4.01 |
| Median home value | 141100 |
| Gini index | 0.4527 |
| Vacancy rate | 22.74 |
| White | 5536 |
| Black | 90 |
| Asian | 16 |
| Native | 39 |
| Hispanic/Latino | 120 |
| Bachelor's or higher | 1152 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 15](/us/states/ky/districts/senate/15.md) — 100% (state senate)
- [KY House District 21](/us/states/ky/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
