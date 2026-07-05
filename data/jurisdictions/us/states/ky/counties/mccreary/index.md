---
type: Jurisdiction
title: "McCreary County, KY"
classification: county
fips: "21147"
state: "KY"
demographics:
  population: 16867
  population_under_18: 3672
  population_18_64: 10458
  population_65_plus: 2737
  median_household_income: 33750
  poverty_rate: 38.86
  homeownership_rate: 74.24
  unemployment_rate: 4.17
  median_home_value: 85300
  gini_index: 0.4899
  vacancy_rate: 15.3
  race_white: 15183
  race_black: 1069
  race_asian: 9
  race_native: 25
  hispanic: 375
  bachelors_plus: 1432
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/52"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# McCreary County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16867 |
| Under 18 | 3672 |
| 18–64 | 10458 |
| 65+ | 2737 |
| Median household income | 33750 |
| Poverty rate | 38.86 |
| Homeownership rate | 74.24 |
| Unemployment rate | 4.17 |
| Median home value | 85300 |
| Gini index | 0.4899 |
| Vacancy rate | 15.3 |
| White | 15183 |
| Black | 1069 |
| Asian | 9 |
| Native | 25 |
| Hispanic/Latino | 375 |
| Bachelor's or higher | 1432 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 25](/us/states/ky/districts/senate/25.md) — 100% (state senate)
- [KY House District 52](/us/states/ky/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
