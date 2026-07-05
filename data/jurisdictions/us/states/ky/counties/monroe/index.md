---
type: Jurisdiction
title: "Monroe County, KY"
classification: county
fips: "21171"
state: "KY"
demographics:
  population: 11269
  population_under_18: 2753
  population_18_64: 6412
  population_65_plus: 2104
  median_household_income: 51280
  poverty_rate: 22.1
  homeownership_rate: 70.89
  unemployment_rate: 4.03
  median_home_value: 115900
  gini_index: 0.4428
  vacancy_rate: 12.01
  race_white: 10323
  race_black: 243
  race_asian: 0
  race_native: 8
  hispanic: 522
  bachelors_plus: 1928
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/senate/16"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/21"
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

# Monroe County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11269 |
| Under 18 | 2753 |
| 18–64 | 6412 |
| 65+ | 2104 |
| Median household income | 51280 |
| Poverty rate | 22.1 |
| Homeownership rate | 70.89 |
| Unemployment rate | 4.03 |
| Median home value | 115900 |
| Gini index | 0.4428 |
| Vacancy rate | 12.01 |
| White | 10323 |
| Black | 243 |
| Asian | 0 |
| Native | 8 |
| Hispanic/Latino | 522 |
| Bachelor's or higher | 1928 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 16](/us/states/ky/districts/senate/16.md) — 100% (state senate)
- [KY House District 21](/us/states/ky/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
