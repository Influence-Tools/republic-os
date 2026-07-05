---
type: Jurisdiction
title: "Stone County, MO"
classification: county
fips: "29209"
state: "MO"
demographics:
  population: 32048
  population_under_18: 5360
  population_18_64: 16433
  population_65_plus: 10255
  median_household_income: 63520
  poverty_rate: 13.92
  homeownership_rate: 83.29
  unemployment_rate: 7.06
  median_home_value: 249000
  gini_index: 0.4474
  vacancy_rate: 33.88
  race_white: 29929
  race_black: 104
  race_asian: 89
  race_native: 123
  hispanic: 936
  bachelors_plus: 8188
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/138"
    rel: in-district
    area_weight: 0.8369
  - to: "us/states/mo/districts/house/155"
    rel: in-district
    area_weight: 0.163
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Stone County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32048 |
| Under 18 | 5360 |
| 18–64 | 16433 |
| 65+ | 10255 |
| Median household income | 63520 |
| Poverty rate | 13.92 |
| Homeownership rate | 83.29 |
| Unemployment rate | 7.06 |
| Median home value | 249000 |
| Gini index | 0.4474 |
| Vacancy rate | 33.88 |
| White | 29929 |
| Black | 104 |
| Asian | 89 |
| Native | 123 |
| Hispanic/Latino | 936 |
| Bachelor's or higher | 8188 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 138](/us/states/mo/districts/house/138.md) — 84% (state house)
- [MO House District 155](/us/states/mo/districts/house/155.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
