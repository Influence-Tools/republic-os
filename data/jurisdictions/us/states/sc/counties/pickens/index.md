---
type: Jurisdiction
title: "Pickens County, SC"
classification: county
fips: "45077"
state: "SC"
demographics:
  population: 134629
  population_under_18: 25021
  population_18_64: 86282
  population_65_plus: 23326
  median_household_income: 61064
  poverty_rate: 17.17
  homeownership_rate: 70.9
  unemployment_rate: 3.63
  median_home_value: 231900
  gini_index: 0.4933
  vacancy_rate: 10.67
  race_white: 113363
  race_black: 7765
  race_asian: 2209
  race_native: 312
  hispanic: 7236
  bachelors_plus: 35080
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9974
  - to: "us/states/sc/districts/senate/2"
    rel: in-district
    area_weight: 0.9122
  - to: "us/states/sc/districts/senate/1"
    rel: in-district
    area_weight: 0.0873
  - to: "us/states/sc/districts/house/4"
    rel: in-district
    area_weight: 0.4962
  - to: "us/states/sc/districts/house/1"
    rel: in-district
    area_weight: 0.2086
  - to: "us/states/sc/districts/house/3"
    rel: in-district
    area_weight: 0.1778
  - to: "us/states/sc/districts/house/5"
    rel: in-district
    area_weight: 0.1039
  - to: "us/states/sc/districts/house/10"
    rel: in-district
    area_weight: 0.0119
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Pickens County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 134629 |
| Under 18 | 25021 |
| 18–64 | 86282 |
| 65+ | 23326 |
| Median household income | 61064 |
| Poverty rate | 17.17 |
| Homeownership rate | 70.9 |
| Unemployment rate | 3.63 |
| Median home value | 231900 |
| Gini index | 0.4933 |
| Vacancy rate | 10.67 |
| White | 113363 |
| Black | 7765 |
| Asian | 2209 |
| Native | 312 |
| Hispanic/Latino | 7236 |
| Bachelor's or higher | 35080 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 2](/us/states/sc/districts/senate/2.md) — 91% (state senate)
- [SC Senate District 1](/us/states/sc/districts/senate/1.md) — 9% (state senate)
- [SC House District 4](/us/states/sc/districts/house/4.md) — 50% (state house)
- [SC House District 1](/us/states/sc/districts/house/1.md) — 21% (state house)
- [SC House District 3](/us/states/sc/districts/house/3.md) — 18% (state house)
- [SC House District 5](/us/states/sc/districts/house/5.md) — 10% (state house)
- [SC House District 10](/us/states/sc/districts/house/10.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
