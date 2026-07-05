---
type: Jurisdiction
title: "Clay County, MS"
classification: county
fips: "28025"
state: "MS"
demographics:
  population: 18383
  population_under_18: 4145
  population_18_64: 10604
  population_65_plus: 3634
  median_household_income: 43125
  poverty_rate: 20.9
  homeownership_rate: 71.33
  unemployment_rate: 7.23
  median_home_value: 129100
  gini_index: 0.4936
  vacancy_rate: 13.78
  race_white: 6782
  race_black: 11058
  race_asian: 20
  race_native: 0
  hispanic: 36
  bachelors_plus: 3031
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/senate/16"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/house/36"
    rel: in-district
    area_weight: 0.944
  - to: "us/states/ms/districts/house/37"
    rel: in-district
    area_weight: 0.0414
  - to: "us/states/ms/districts/house/38"
    rel: in-district
    area_weight: 0.0145
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Clay County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18383 |
| Under 18 | 4145 |
| 18–64 | 10604 |
| 65+ | 3634 |
| Median household income | 43125 |
| Poverty rate | 20.9 |
| Homeownership rate | 71.33 |
| Unemployment rate | 7.23 |
| Median home value | 129100 |
| Gini index | 0.4936 |
| Vacancy rate | 13.78 |
| White | 6782 |
| Black | 11058 |
| Asian | 20 |
| Native | 0 |
| Hispanic/Latino | 36 |
| Bachelor's or higher | 3031 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 16](/us/states/ms/districts/senate/16.md) — 100% (state senate)
- [MS House District 36](/us/states/ms/districts/house/36.md) — 94% (state house)
- [MS House District 37](/us/states/ms/districts/house/37.md) — 4% (state house)
- [MS House District 38](/us/states/ms/districts/house/38.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
