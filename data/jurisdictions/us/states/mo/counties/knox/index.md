---
type: Jurisdiction
title: "Knox County, MO"
classification: county
fips: "29103"
state: "MO"
demographics:
  population: 3756
  population_under_18: 932
  population_18_64: 2016
  population_65_plus: 808
  median_household_income: 57788
  poverty_rate: 11.9
  homeownership_rate: 85.09
  unemployment_rate: 1.08
  median_home_value: 101400
  gini_index: 0.4672
  vacancy_rate: 33.51
  race_white: 3561
  race_black: 24
  race_asian: 7
  race_native: 3
  hispanic: 11
  bachelors_plus: 539
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Knox County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3756 |
| Under 18 | 932 |
| 18–64 | 2016 |
| 65+ | 808 |
| Median household income | 57788 |
| Poverty rate | 11.9 |
| Homeownership rate | 85.09 |
| Unemployment rate | 1.08 |
| Median home value | 101400 |
| Gini index | 0.4672 |
| Vacancy rate | 33.51 |
| White | 3561 |
| Black | 24 |
| Asian | 7 |
| Native | 3 |
| Hispanic/Latino | 11 |
| Bachelor's or higher | 539 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
