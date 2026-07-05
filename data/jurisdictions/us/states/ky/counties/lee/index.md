---
type: Jurisdiction
title: "Lee County, KY"
classification: county
fips: "21129"
state: "KY"
demographics:
  population: 7339
  population_under_18: 1330
  population_18_64: 4574
  population_65_plus: 1435
  median_household_income: 37568
  poverty_rate: 27.36
  homeownership_rate: 77.73
  unemployment_rate: 4.72
  median_home_value: 83900
  gini_index: 0.4591
  vacancy_rate: 19.63
  race_white: 6889
  race_black: 223
  race_asian: 0
  race_native: 21
  hispanic: 83
  bachelors_plus: 723
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/89"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Lee County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7339 |
| Under 18 | 1330 |
| 18–64 | 4574 |
| 65+ | 1435 |
| Median household income | 37568 |
| Poverty rate | 27.36 |
| Homeownership rate | 77.73 |
| Unemployment rate | 4.72 |
| Median home value | 83900 |
| Gini index | 0.4591 |
| Vacancy rate | 19.63 |
| White | 6889 |
| Black | 223 |
| Asian | 0 |
| Native | 21 |
| Hispanic/Latino | 83 |
| Bachelor's or higher | 723 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 89](/us/states/ky/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
