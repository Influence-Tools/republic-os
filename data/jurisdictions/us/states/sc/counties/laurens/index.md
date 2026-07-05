---
type: Jurisdiction
title: "Laurens County, SC"
classification: county
fips: "45059"
state: "SC"
demographics:
  population: 68666
  population_under_18: 14980
  population_18_64: 40530
  population_65_plus: 13156
  median_household_income: 57623
  poverty_rate: 18.13
  homeownership_rate: 71.48
  unemployment_rate: 4.49
  median_home_value: 170600
  gini_index: 0.4302
  vacancy_rate: 15.82
  race_white: 46545
  race_black: 15761
  race_asian: 422
  race_native: 471
  hispanic: 4614
  bachelors_plus: 11154
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/sc/districts/senate/9"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sc/districts/house/14"
    rel: in-district
    area_weight: 0.616
  - to: "us/states/sc/districts/house/42"
    rel: in-district
    area_weight: 0.209
  - to: "us/states/sc/districts/house/16"
    rel: in-district
    area_weight: 0.0804
  - to: "us/states/sc/districts/house/11"
    rel: in-district
    area_weight: 0.0625
  - to: "us/states/sc/districts/house/13"
    rel: in-district
    area_weight: 0.0319
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Laurens County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68666 |
| Under 18 | 14980 |
| 18–64 | 40530 |
| 65+ | 13156 |
| Median household income | 57623 |
| Poverty rate | 18.13 |
| Homeownership rate | 71.48 |
| Unemployment rate | 4.49 |
| Median home value | 170600 |
| Gini index | 0.4302 |
| Vacancy rate | 15.82 |
| White | 46545 |
| Black | 15761 |
| Asian | 422 |
| Native | 471 |
| Hispanic/Latino | 4614 |
| Bachelor's or higher | 11154 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 9](/us/states/sc/districts/senate/9.md) — 100% (state senate)
- [SC House District 14](/us/states/sc/districts/house/14.md) — 62% (state house)
- [SC House District 42](/us/states/sc/districts/house/42.md) — 21% (state house)
- [SC House District 16](/us/states/sc/districts/house/16.md) — 8% (state house)
- [SC House District 11](/us/states/sc/districts/house/11.md) — 6% (state house)
- [SC House District 13](/us/states/sc/districts/house/13.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
