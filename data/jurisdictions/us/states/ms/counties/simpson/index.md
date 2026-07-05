---
type: Jurisdiction
title: "Simpson County, MS"
classification: county
fips: "28127"
state: "MS"
demographics:
  population: 25691
  population_under_18: 5946
  population_18_64: 14828
  population_65_plus: 4917
  median_household_income: 56381
  poverty_rate: 20.04
  homeownership_rate: 81.41
  unemployment_rate: 4.35
  median_home_value: 122200
  gini_index: 0.4411
  vacancy_rate: 18.39
  race_white: 15701
  race_black: 9134
  race_asian: 49
  race_native: 41
  hispanic: 443
  bachelors_plus: 4043
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ms/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/77"
    rel: in-district
    area_weight: 0.675
  - to: "us/states/ms/districts/house/91"
    rel: in-district
    area_weight: 0.2525
  - to: "us/states/ms/districts/house/90"
    rel: in-district
    area_weight: 0.0587
  - to: "us/states/ms/districts/house/62"
    rel: in-district
    area_weight: 0.0136
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Simpson County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25691 |
| Under 18 | 5946 |
| 18–64 | 14828 |
| 65+ | 4917 |
| Median household income | 56381 |
| Poverty rate | 20.04 |
| Homeownership rate | 81.41 |
| Unemployment rate | 4.35 |
| Median home value | 122200 |
| Gini index | 0.4411 |
| Vacancy rate | 18.39 |
| White | 15701 |
| Black | 9134 |
| Asian | 49 |
| Native | 41 |
| Hispanic/Latino | 443 |
| Bachelor's or higher | 4043 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 35](/us/states/ms/districts/senate/35.md) — 100% (state senate)
- [MS House District 77](/us/states/ms/districts/house/77.md) — 68% (state house)
- [MS House District 91](/us/states/ms/districts/house/91.md) — 25% (state house)
- [MS House District 90](/us/states/ms/districts/house/90.md) — 6% (state house)
- [MS House District 62](/us/states/ms/districts/house/62.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
