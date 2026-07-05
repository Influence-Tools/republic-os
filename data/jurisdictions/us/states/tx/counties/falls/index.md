---
type: Jurisdiction
title: "Falls County, TX"
classification: county
fips: "48145"
state: "TX"
demographics:
  population: 17291
  population_under_18: 3627
  population_18_64: 10323
  population_65_plus: 3341
  median_household_income: 57247
  poverty_rate: 14.71
  homeownership_rate: 76.47
  unemployment_rate: 5.96
  median_home_value: 110900
  gini_index: 0.483
  vacancy_rate: 14.85
  race_white: 10009
  race_black: 3230
  race_asian: 961
  race_native: 69
  hispanic: 4324
  bachelors_plus: 3076
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/13"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Falls County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17291 |
| Under 18 | 3627 |
| 18–64 | 10323 |
| 65+ | 3341 |
| Median household income | 57247 |
| Poverty rate | 14.71 |
| Homeownership rate | 76.47 |
| Unemployment rate | 5.96 |
| Median home value | 110900 |
| Gini index | 0.483 |
| Vacancy rate | 14.85 |
| White | 10009 |
| Black | 3230 |
| Asian | 961 |
| Native | 69 |
| Hispanic/Latino | 4324 |
| Bachelor's or higher | 3076 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
