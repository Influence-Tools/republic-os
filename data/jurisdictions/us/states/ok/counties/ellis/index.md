---
type: Jurisdiction
title: "Ellis County, OK"
classification: county
fips: "40045"
state: "OK"
demographics:
  population: 3683
  population_under_18: 814
  population_18_64: 2013
  population_65_plus: 856
  median_household_income: 61016
  poverty_rate: 12.99
  homeownership_rate: 82.07
  unemployment_rate: 5.3
  median_home_value: 119100
  gini_index: 0.3996
  vacancy_rate: 30.51
  race_white: 3191
  race_black: 14
  race_asian: 31
  race_native: 49
  hispanic: 350
  bachelors_plus: 659
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Ellis County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3683 |
| Under 18 | 814 |
| 18–64 | 2013 |
| 65+ | 856 |
| Median household income | 61016 |
| Poverty rate | 12.99 |
| Homeownership rate | 82.07 |
| Unemployment rate | 5.3 |
| Median home value | 119100 |
| Gini index | 0.3996 |
| Vacancy rate | 30.51 |
| White | 3191 |
| Black | 14 |
| Asian | 31 |
| Native | 49 |
| Hispanic/Latino | 350 |
| Bachelor's or higher | 659 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
