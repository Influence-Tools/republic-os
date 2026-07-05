---
type: Jurisdiction
title: "Waldo County, ME"
classification: county
fips: "23027"
state: "ME"
demographics:
  population: 40192
  population_under_18: 7124
  population_18_64: 22977
  population_65_plus: 10091
  median_household_income: 72782
  poverty_rate: 12.0
  homeownership_rate: 81.92
  unemployment_rate: 3.73
  median_home_value: 257700
  gini_index: 0.4331
  vacancy_rate: 21.49
  race_white: 37552
  race_black: 218
  race_asian: 205
  race_native: 79
  hispanic: 651
  bachelors_plus: 14744
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.8866
  - to: "us/states/me/districts/senate/11"
    rel: in-district
    area_weight: 0.8836
  - to: "us/states/me/districts/house/38"
    rel: in-district
    area_weight: 0.2739
  - to: "us/states/me/districts/house/40"
    rel: in-district
    area_weight: 0.2126
  - to: "us/states/me/districts/house/37"
    rel: in-district
    area_weight: 0.1464
  - to: "us/states/me/districts/house/68"
    rel: in-district
    area_weight: 0.0896
  - to: "us/states/me/districts/house/39"
    rel: in-district
    area_weight: 0.0852
  - to: "us/states/me/districts/house/62"
    rel: in-district
    area_weight: 0.0503
  - to: "us/states/me/districts/house/63"
    rel: in-district
    area_weight: 0.0257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Waldo County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40192 |
| Under 18 | 7124 |
| 18–64 | 22977 |
| 65+ | 10091 |
| Median household income | 72782 |
| Poverty rate | 12.0 |
| Homeownership rate | 81.92 |
| Unemployment rate | 3.73 |
| Median home value | 257700 |
| Gini index | 0.4331 |
| Vacancy rate | 21.49 |
| White | 37552 |
| Black | 218 |
| Asian | 205 |
| Native | 79 |
| Hispanic/Latino | 651 |
| Bachelor's or higher | 14744 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 89% (congressional)
- [ME Senate District 11](/us/states/me/districts/senate/11.md) — 88% (state senate)
- [ME House District 38](/us/states/me/districts/house/38.md) — 27% (state house)
- [ME House District 40](/us/states/me/districts/house/40.md) — 21% (state house)
- [ME House District 37](/us/states/me/districts/house/37.md) — 15% (state house)
- [ME House District 68](/us/states/me/districts/house/68.md) — 9% (state house)
- [ME House District 39](/us/states/me/districts/house/39.md) — 9% (state house)
- [ME House District 62](/us/states/me/districts/house/62.md) — 5% (state house)
- [ME House District 63](/us/states/me/districts/house/63.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
