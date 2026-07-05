---
type: Jurisdiction
title: "Leake County, MS"
classification: county
fips: "28079"
state: "MS"
demographics:
  population: 21319
  population_under_18: 4986
  population_18_64: 12461
  population_65_plus: 3872
  median_household_income: 50728
  poverty_rate: 20.52
  homeownership_rate: 76.75
  unemployment_rate: 6.22
  median_home_value: 116800
  gini_index: 0.4606
  vacancy_rate: 18.33
  race_white: 9853
  race_black: 8307
  race_asian: 51
  race_native: 1327
  hispanic: 1403
  bachelors_plus: 3160
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ms/districts/senate/18"
    rel: in-district
    area_weight: 0.8513
  - to: "us/states/ms/districts/senate/21"
    rel: in-district
    area_weight: 0.1486
  - to: "us/states/ms/districts/house/27"
    rel: in-district
    area_weight: 0.4833
  - to: "us/states/ms/districts/house/48"
    rel: in-district
    area_weight: 0.3865
  - to: "us/states/ms/districts/house/78"
    rel: in-district
    area_weight: 0.0977
  - to: "us/states/ms/districts/house/44"
    rel: in-district
    area_weight: 0.0325
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Leake County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21319 |
| Under 18 | 4986 |
| 18–64 | 12461 |
| 65+ | 3872 |
| Median household income | 50728 |
| Poverty rate | 20.52 |
| Homeownership rate | 76.75 |
| Unemployment rate | 6.22 |
| Median home value | 116800 |
| Gini index | 0.4606 |
| Vacancy rate | 18.33 |
| White | 9853 |
| Black | 8307 |
| Asian | 51 |
| Native | 1327 |
| Hispanic/Latino | 1403 |
| Bachelor's or higher | 3160 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 18](/us/states/ms/districts/senate/18.md) — 85% (state senate)
- [MS Senate District 21](/us/states/ms/districts/senate/21.md) — 15% (state senate)
- [MS House District 27](/us/states/ms/districts/house/27.md) — 48% (state house)
- [MS House District 48](/us/states/ms/districts/house/48.md) — 39% (state house)
- [MS House District 78](/us/states/ms/districts/house/78.md) — 10% (state house)
- [MS House District 44](/us/states/ms/districts/house/44.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
