---
type: Jurisdiction
title: "Oregon County, MO"
classification: county
fips: "29149"
state: "MO"
demographics:
  population: 8673
  population_under_18: 2008
  population_18_64: 4672
  population_65_plus: 1993
  median_household_income: 43069
  poverty_rate: 23.59
  homeownership_rate: 74.94
  unemployment_rate: 5.24
  median_home_value: 113300
  gini_index: 0.4481
  vacancy_rate: 21.78
  race_white: 8061
  race_black: 7
  race_asian: 52
  race_native: 15
  hispanic: 132
  bachelors_plus: 1154
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Oregon County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8673 |
| Under 18 | 2008 |
| 18–64 | 4672 |
| 65+ | 1993 |
| Median household income | 43069 |
| Poverty rate | 23.59 |
| Homeownership rate | 74.94 |
| Unemployment rate | 5.24 |
| Median home value | 113300 |
| Gini index | 0.4481 |
| Vacancy rate | 21.78 |
| White | 8061 |
| Black | 7 |
| Asian | 52 |
| Native | 15 |
| Hispanic/Latino | 132 |
| Bachelor's or higher | 1154 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
