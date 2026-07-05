---
type: Jurisdiction
title: "Fleming County, KY"
classification: county
fips: "21069"
state: "KY"
demographics:
  population: 15323
  population_under_18: 3656
  population_18_64: 8816
  population_65_plus: 2851
  median_household_income: 49307
  poverty_rate: 21.18
  homeownership_rate: 74.83
  unemployment_rate: 7.48
  median_home_value: 134700
  gini_index: 0.4422
  vacancy_rate: 13.75
  race_white: 14554
  race_black: 143
  race_asian: 120
  race_native: 0
  hispanic: 259
  bachelors_plus: 2772
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9904
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.0074
  - to: "us/states/ky/districts/senate/27"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/72"
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

# Fleming County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15323 |
| Under 18 | 3656 |
| 18–64 | 8816 |
| 65+ | 2851 |
| Median household income | 49307 |
| Poverty rate | 21.18 |
| Homeownership rate | 74.83 |
| Unemployment rate | 7.48 |
| Median home value | 134700 |
| Gini index | 0.4422 |
| Vacancy rate | 13.75 |
| White | 14554 |
| Black | 143 |
| Asian | 120 |
| Native | 0 |
| Hispanic/Latino | 259 |
| Bachelor's or higher | 2772 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 99% (congressional)
- [KY-05](/us/states/ky/districts/05.md) — 1% (congressional)
- [KY Senate District 27](/us/states/ky/districts/senate/27.md) — 100% (state senate)
- [KY House District 72](/us/states/ky/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
