---
type: Jurisdiction
title: "Union County, KY"
classification: county
fips: "21225"
state: "KY"
demographics:
  population: 13260
  population_under_18: 2499
  population_18_64: 8130
  population_65_plus: 2631
  median_household_income: 60327
  poverty_rate: 18.44
  homeownership_rate: 70.24
  unemployment_rate: 2.69
  median_home_value: 104500
  gini_index: 0.4476
  vacancy_rate: 11.08
  race_white: 11762
  race_black: 915
  race_asian: 18
  race_native: 0
  hispanic: 232
  bachelors_plus: 1651
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/senate/4"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/12"
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

# Union County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13260 |
| Under 18 | 2499 |
| 18–64 | 8130 |
| 65+ | 2631 |
| Median household income | 60327 |
| Poverty rate | 18.44 |
| Homeownership rate | 70.24 |
| Unemployment rate | 2.69 |
| Median home value | 104500 |
| Gini index | 0.4476 |
| Vacancy rate | 11.08 |
| White | 11762 |
| Black | 915 |
| Asian | 18 |
| Native | 0 |
| Hispanic/Latino | 232 |
| Bachelor's or higher | 1651 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 4](/us/states/ky/districts/senate/4.md) — 100% (state senate)
- [KY House District 12](/us/states/ky/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
