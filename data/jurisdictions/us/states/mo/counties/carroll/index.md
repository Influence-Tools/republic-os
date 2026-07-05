---
type: Jurisdiction
title: "Carroll County, MO"
classification: county
fips: "29033"
state: "MO"
demographics:
  population: 8411
  population_under_18: 1842
  population_18_64: 4690
  population_65_plus: 1879
  median_household_income: 62154
  poverty_rate: 13.7
  homeownership_rate: 71.92
  unemployment_rate: 4.31
  median_home_value: 117500
  gini_index: 0.4502
  vacancy_rate: 19.61
  race_white: 7895
  race_black: 145
  race_asian: 13
  race_native: 0
  hispanic: 187
  bachelors_plus: 1584
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/7"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Carroll County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8411 |
| Under 18 | 1842 |
| 18–64 | 4690 |
| 65+ | 1879 |
| Median household income | 62154 |
| Poverty rate | 13.7 |
| Homeownership rate | 71.92 |
| Unemployment rate | 4.31 |
| Median home value | 117500 |
| Gini index | 0.4502 |
| Vacancy rate | 19.61 |
| White | 7895 |
| Black | 145 |
| Asian | 13 |
| Native | 0 |
| Hispanic/Latino | 187 |
| Bachelor's or higher | 1584 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 7](/us/states/mo/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
