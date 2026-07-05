---
type: Jurisdiction
title: "St. Clair County, MO"
classification: county
fips: "29185"
state: "MO"
demographics:
  population: 9587
  population_under_18: 2038
  population_18_64: 5092
  population_65_plus: 2457
  median_household_income: 53043
  poverty_rate: 14.68
  homeownership_rate: 75.98
  unemployment_rate: 3.33
  median_home_value: 157100
  gini_index: 0.4462
  vacancy_rate: 23.04
  race_white: 8960
  race_black: 77
  race_asian: 24
  race_native: 16
  hispanic: 213
  bachelors_plus: 1333
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/126"
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

# St. Clair County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9587 |
| Under 18 | 2038 |
| 18–64 | 5092 |
| 65+ | 2457 |
| Median household income | 53043 |
| Poverty rate | 14.68 |
| Homeownership rate | 75.98 |
| Unemployment rate | 3.33 |
| Median home value | 157100 |
| Gini index | 0.4462 |
| Vacancy rate | 23.04 |
| White | 8960 |
| Black | 77 |
| Asian | 24 |
| Native | 16 |
| Hispanic/Latino | 213 |
| Bachelor's or higher | 1333 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 126](/us/states/mo/districts/house/126.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
