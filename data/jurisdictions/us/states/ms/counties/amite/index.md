---
type: Jurisdiction
title: "Amite County, MS"
classification: county
fips: "28005"
state: "MS"
demographics:
  population: 12565
  population_under_18: 2542
  population_18_64: 6721
  population_65_plus: 3302
  median_household_income: 37222
  poverty_rate: 27.65
  homeownership_rate: 82.38
  unemployment_rate: 5.81
  median_home_value: 100800
  gini_index: 0.4684
  vacancy_rate: 20.36
  race_white: 7364
  race_black: 5033
  race_asian: 3
  race_native: 34
  hispanic: 10
  bachelors_plus: 1526
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/38"
    rel: in-district
    area_weight: 0.6054
  - to: "us/states/ms/districts/senate/39"
    rel: in-district
    area_weight: 0.3944
  - to: "us/states/ms/districts/house/96"
    rel: in-district
    area_weight: 0.6527
  - to: "us/states/ms/districts/house/97"
    rel: in-district
    area_weight: 0.347
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Amite County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12565 |
| Under 18 | 2542 |
| 18–64 | 6721 |
| 65+ | 3302 |
| Median household income | 37222 |
| Poverty rate | 27.65 |
| Homeownership rate | 82.38 |
| Unemployment rate | 5.81 |
| Median home value | 100800 |
| Gini index | 0.4684 |
| Vacancy rate | 20.36 |
| White | 7364 |
| Black | 5033 |
| Asian | 3 |
| Native | 34 |
| Hispanic/Latino | 10 |
| Bachelor's or higher | 1526 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 38](/us/states/ms/districts/senate/38.md) — 61% (state senate)
- [MS Senate District 39](/us/states/ms/districts/senate/39.md) — 39% (state senate)
- [MS House District 96](/us/states/ms/districts/house/96.md) — 65% (state house)
- [MS House District 97](/us/states/ms/districts/house/97.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
