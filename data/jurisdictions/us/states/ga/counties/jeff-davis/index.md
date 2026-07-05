---
type: Jurisdiction
title: "Jeff Davis County, GA"
classification: county
fips: "13161"
state: "GA"
demographics:
  population: 14924
  population_under_18: 3823
  population_18_64: 8759
  population_65_plus: 2342
  median_household_income: 40283
  poverty_rate: 21.82
  homeownership_rate: 71.32
  unemployment_rate: 6.7
  median_home_value: 118300
  gini_index: 0.4848
  vacancy_rate: 14.3
  race_white: 10151
  race_black: 1789
  race_asian: 76
  race_native: 186
  hispanic: 2095
  bachelors_plus: 1838
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/157"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Jeff Davis County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14924 |
| Under 18 | 3823 |
| 18–64 | 8759 |
| 65+ | 2342 |
| Median household income | 40283 |
| Poverty rate | 21.82 |
| Homeownership rate | 71.32 |
| Unemployment rate | 6.7 |
| Median home value | 118300 |
| Gini index | 0.4848 |
| Vacancy rate | 14.3 |
| White | 10151 |
| Black | 1789 |
| Asian | 76 |
| Native | 186 |
| Hispanic/Latino | 2095 |
| Bachelor's or higher | 1838 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 157](/us/states/ga/districts/house/157.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
