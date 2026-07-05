---
type: Jurisdiction
title: "Lincoln County, MO"
classification: county
fips: "29113"
state: "MO"
demographics:
  population: 63057
  population_under_18: 15810
  population_18_64: 37899
  population_65_plus: 9348
  median_household_income: 89278
  poverty_rate: 10.23
  homeownership_rate: 79.02
  unemployment_rate: 3.66
  median_home_value: 244300
  gini_index: 0.3927
  vacancy_rate: 4.09
  race_white: 58143
  race_black: 1223
  race_asian: 203
  race_native: 153
  hispanic: 1809
  bachelors_plus: 10032
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/mo/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/40"
    rel: in-district
    area_weight: 0.7166
  - to: "us/states/mo/districts/house/41"
    rel: in-district
    area_weight: 0.2831
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Lincoln County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 63057 |
| Under 18 | 15810 |
| 18–64 | 37899 |
| 65+ | 9348 |
| Median household income | 89278 |
| Poverty rate | 10.23 |
| Homeownership rate | 79.02 |
| Unemployment rate | 3.66 |
| Median home value | 244300 |
| Gini index | 0.3927 |
| Vacancy rate | 4.09 |
| White | 58143 |
| Black | 1223 |
| Asian | 203 |
| Native | 153 |
| Hispanic/Latino | 1809 |
| Bachelor's or higher | 10032 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 10](/us/states/mo/districts/senate/10.md) — 100% (state senate)
- [MO House District 40](/us/states/mo/districts/house/40.md) — 72% (state house)
- [MO House District 41](/us/states/mo/districts/house/41.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
