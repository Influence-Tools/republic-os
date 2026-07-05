---
type: Jurisdiction
title: "Copiah County, MS"
classification: county
fips: "28029"
state: "MS"
demographics:
  population: 27855
  population_under_18: 6253
  population_18_64: 16287
  population_65_plus: 5315
  median_household_income: 49089
  poverty_rate: 22.97
  homeownership_rate: 74.4
  unemployment_rate: 5.76
  median_home_value: 114100
  gini_index: 0.5418
  vacancy_rate: 19.36
  race_white: 12008
  race_black: 14080
  race_asian: 82
  race_native: 12
  hispanic: 1287
  bachelors_plus: 4807
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/ms/districts/senate/37"
    rel: in-district
    area_weight: 0.6266
  - to: "us/states/ms/districts/senate/35"
    rel: in-district
    area_weight: 0.3732
  - to: "us/states/ms/districts/house/76"
    rel: in-district
    area_weight: 0.654
  - to: "us/states/ms/districts/house/92"
    rel: in-district
    area_weight: 0.2928
  - to: "us/states/ms/districts/house/62"
    rel: in-district
    area_weight: 0.053
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Copiah County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27855 |
| Under 18 | 6253 |
| 18–64 | 16287 |
| 65+ | 5315 |
| Median household income | 49089 |
| Poverty rate | 22.97 |
| Homeownership rate | 74.4 |
| Unemployment rate | 5.76 |
| Median home value | 114100 |
| Gini index | 0.5418 |
| Vacancy rate | 19.36 |
| White | 12008 |
| Black | 14080 |
| Asian | 82 |
| Native | 12 |
| Hispanic/Latino | 1287 |
| Bachelor's or higher | 4807 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 37](/us/states/ms/districts/senate/37.md) — 63% (state senate)
- [MS Senate District 35](/us/states/ms/districts/senate/35.md) — 37% (state senate)
- [MS House District 76](/us/states/ms/districts/house/76.md) — 65% (state house)
- [MS House District 92](/us/states/ms/districts/house/92.md) — 29% (state house)
- [MS House District 62](/us/states/ms/districts/house/62.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
