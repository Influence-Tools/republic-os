---
type: Jurisdiction
title: "Webster County, MS"
classification: county
fips: "28155"
state: "MS"
demographics:
  population: 9972
  population_under_18: 2440
  population_18_64: 5722
  population_65_plus: 1810
  median_household_income: 58789
  poverty_rate: 16.36
  homeownership_rate: 76.06
  unemployment_rate: 6.63
  median_home_value: 120100
  gini_index: 0.4292
  vacancy_rate: 20.36
  race_white: 7816
  race_black: 1861
  race_asian: 29
  race_native: 6
  hispanic: 193
  bachelors_plus: 1995
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/23"
    rel: in-district
    area_weight: 0.3906
  - to: "us/states/ms/districts/house/35"
    rel: in-district
    area_weight: 0.3233
  - to: "us/states/ms/districts/house/46"
    rel: in-district
    area_weight: 0.2861
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Webster County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9972 |
| Under 18 | 2440 |
| 18–64 | 5722 |
| 65+ | 1810 |
| Median household income | 58789 |
| Poverty rate | 16.36 |
| Homeownership rate | 76.06 |
| Unemployment rate | 6.63 |
| Median home value | 120100 |
| Gini index | 0.4292 |
| Vacancy rate | 20.36 |
| White | 7816 |
| Black | 1861 |
| Asian | 29 |
| Native | 6 |
| Hispanic/Latino | 193 |
| Bachelor's or higher | 1995 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 15](/us/states/ms/districts/senate/15.md) — 100% (state senate)
- [MS House District 23](/us/states/ms/districts/house/23.md) — 39% (state house)
- [MS House District 35](/us/states/ms/districts/house/35.md) — 32% (state house)
- [MS House District 46](/us/states/ms/districts/house/46.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
