---
type: Jurisdiction
title: "Casey County, KY"
classification: county
fips: "21045"
state: "KY"
demographics:
  population: 15914
  population_under_18: 3665
  population_18_64: 8935
  population_65_plus: 3314
  median_household_income: 45510
  poverty_rate: 21.73
  homeownership_rate: 79.71
  unemployment_rate: 8.89
  median_home_value: 136300
  gini_index: 0.4867
  vacancy_rate: 12.64
  race_white: 15040
  race_black: 60
  race_asian: 11
  race_native: 5
  hispanic: 546
  bachelors_plus: 2058
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/senate/21"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/54"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Casey County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15914 |
| Under 18 | 3665 |
| 18–64 | 8935 |
| 65+ | 3314 |
| Median household income | 45510 |
| Poverty rate | 21.73 |
| Homeownership rate | 79.71 |
| Unemployment rate | 8.89 |
| Median home value | 136300 |
| Gini index | 0.4867 |
| Vacancy rate | 12.64 |
| White | 15040 |
| Black | 60 |
| Asian | 11 |
| Native | 5 |
| Hispanic/Latino | 546 |
| Bachelor's or higher | 2058 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 21](/us/states/ky/districts/senate/21.md) — 100% (state senate)
- [KY House District 54](/us/states/ky/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
