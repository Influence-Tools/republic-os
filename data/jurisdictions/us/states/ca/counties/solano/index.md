---
type: Jurisdiction
title: "Solano County, CA"
classification: county
fips: "06095"
state: "CA"
demographics:
  population: 451918
  population_under_18: 98830
  population_18_64: 274350
  population_65_plus: 78738
  median_household_income: 100401
  poverty_rate: 9.99
  homeownership_rate: 63.02
  unemployment_rate: 6.46
  median_home_value: 617700
  gini_index: 0.4292
  vacancy_rate: 4.36
  race_white: 176960
  race_black: 57384
  race_asian: 73617
  race_native: 4002
  hispanic: 133953
  bachelors_plus: 119335
districts:
  - to: "us/states/ca/districts/04"
    rel: in-district
    area_weight: 0.5398
  - to: "us/states/ca/districts/08"
    rel: in-district
    area_weight: 0.4227
  - to: "us/states/ca/districts/07"
    rel: in-district
    area_weight: 0.0193
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.9822
  - to: "us/states/ca/districts/house/11"
    rel: in-district
    area_weight: 0.9819
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Solano County, CA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 451918 |
| Under 18 | 98830 |
| 18–64 | 274350 |
| 65+ | 78738 |
| Median household income | 100401 |
| Poverty rate | 9.99 |
| Homeownership rate | 63.02 |
| Unemployment rate | 6.46 |
| Median home value | 617700 |
| Gini index | 0.4292 |
| Vacancy rate | 4.36 |
| White | 176960 |
| Black | 57384 |
| Asian | 73617 |
| Native | 4002 |
| Hispanic/Latino | 133953 |
| Bachelor's or higher | 119335 |

## Districts

- [CA-04](/us/states/ca/districts/04.md) — 54% (congressional)
- [CA-08](/us/states/ca/districts/08.md) — 42% (congressional)
- [CA-07](/us/states/ca/districts/07.md) — 2% (congressional)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 98% (state senate)
- [CA House District 11](/us/states/ca/districts/house/11.md) — 98% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
