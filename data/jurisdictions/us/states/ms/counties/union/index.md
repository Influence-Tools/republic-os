---
type: Jurisdiction
title: "Union County, MS"
classification: county
fips: "28145"
state: "MS"
demographics:
  population: 28122
  population_under_18: 7039
  population_18_64: 16421
  population_65_plus: 4662
  median_household_income: 55505
  poverty_rate: 15.14
  homeownership_rate: 74.66
  unemployment_rate: 4.45
  median_home_value: 163400
  gini_index: 0.45
  vacancy_rate: 19.6
  race_white: 21547
  race_black: 3831
  race_asian: 80
  race_native: 162
  hispanic: 1365
  bachelors_plus: 4825
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/3"
    rel: in-district
    area_weight: 0.7051
  - to: "us/states/ms/districts/senate/10"
    rel: in-district
    area_weight: 0.2948
  - to: "us/states/ms/districts/house/14"
    rel: in-district
    area_weight: 0.7631
  - to: "us/states/ms/districts/house/13"
    rel: in-district
    area_weight: 0.2367
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Union County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28122 |
| Under 18 | 7039 |
| 18–64 | 16421 |
| 65+ | 4662 |
| Median household income | 55505 |
| Poverty rate | 15.14 |
| Homeownership rate | 74.66 |
| Unemployment rate | 4.45 |
| Median home value | 163400 |
| Gini index | 0.45 |
| Vacancy rate | 19.6 |
| White | 21547 |
| Black | 3831 |
| Asian | 80 |
| Native | 162 |
| Hispanic/Latino | 1365 |
| Bachelor's or higher | 4825 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 3](/us/states/ms/districts/senate/3.md) — 71% (state senate)
- [MS Senate District 10](/us/states/ms/districts/senate/10.md) — 29% (state senate)
- [MS House District 14](/us/states/ms/districts/house/14.md) — 76% (state house)
- [MS House District 13](/us/states/ms/districts/house/13.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
