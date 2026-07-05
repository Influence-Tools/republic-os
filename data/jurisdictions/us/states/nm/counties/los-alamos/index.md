---
type: Jurisdiction
title: "Los Alamos County, NM"
classification: county
fips: "35028"
state: "NM"
demographics:
  population: 19435
  population_under_18: 4278
  population_18_64: 11584
  population_65_plus: 3573
  median_household_income: 147139
  poverty_rate: 3.53
  homeownership_rate: 74.83
  unemployment_rate: 0.62
  median_home_value: 495800
  gini_index: 0.3821
  vacancy_rate: 5.35
  race_white: 14526
  race_black: 168
  race_asian: 962
  race_native: 253
  hispanic: 3501
  bachelors_plus: 15994
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/5"
    rel: in-district
    area_weight: 0.5712
  - to: "us/states/nm/districts/senate/6"
    rel: in-district
    area_weight: 0.4283
  - to: "us/states/nm/districts/house/43"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Los Alamos County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19435 |
| Under 18 | 4278 |
| 18–64 | 11584 |
| 65+ | 3573 |
| Median household income | 147139 |
| Poverty rate | 3.53 |
| Homeownership rate | 74.83 |
| Unemployment rate | 0.62 |
| Median home value | 495800 |
| Gini index | 0.3821 |
| Vacancy rate | 5.35 |
| White | 14526 |
| Black | 168 |
| Asian | 962 |
| Native | 253 |
| Hispanic/Latino | 3501 |
| Bachelor's or higher | 15994 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 5](/us/states/nm/districts/senate/5.md) — 57% (state senate)
- [NM Senate District 6](/us/states/nm/districts/senate/6.md) — 43% (state senate)
- [NM House District 43](/us/states/nm/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
