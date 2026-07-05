---
type: Jurisdiction
title: "Menominee County, WI"
classification: county
fips: "55078"
state: "WI"
demographics:
  population: 4252
  population_under_18: 1289
  population_18_64: 2250
  population_65_plus: 713
  median_household_income: 62108
  poverty_rate: 21.75
  homeownership_rate: 75.52
  unemployment_rate: 10.01
  median_home_value: 110200
  gini_index: 0.4255
  vacancy_rate: 35.73
  race_white: 567
  race_black: 35
  race_asian: 2
  race_native: 3504
  hispanic: 216
  bachelors_plus: 613
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/6"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Menominee County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4252 |
| Under 18 | 1289 |
| 18–64 | 2250 |
| 65+ | 713 |
| Median household income | 62108 |
| Poverty rate | 21.75 |
| Homeownership rate | 75.52 |
| Unemployment rate | 10.01 |
| Median home value | 110200 |
| Gini index | 0.4255 |
| Vacancy rate | 35.73 |
| White | 567 |
| Black | 35 |
| Asian | 2 |
| Native | 3504 |
| Hispanic/Latino | 216 |
| Bachelor's or higher | 613 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 100% (congressional)
- [WI Senate District 2](/us/states/wi/districts/senate/2.md) — 100% (state senate)
- [WI House District 6](/us/states/wi/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
