---
type: Jurisdiction
title: "Lowndes County, MS"
classification: county
fips: "28087"
state: "MS"
demographics:
  population: 57838
  population_under_18: 13745
  population_18_64: 34064
  population_65_plus: 10029
  median_household_income: 53812
  poverty_rate: 17.26
  homeownership_rate: 61.28
  unemployment_rate: 6.33
  median_home_value: 164100
  gini_index: 0.4763
  vacancy_rate: 15.32
  race_white: 28509
  race_black: 25301
  race_asian: 631
  race_native: 139
  hispanic: 1329
  bachelors_plus: 14520
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/senate/17"
    rel: in-district
    area_weight: 0.9426
  - to: "us/states/ms/districts/senate/16"
    rel: in-district
    area_weight: 0.0573
  - to: "us/states/ms/districts/house/37"
    rel: in-district
    area_weight: 0.4653
  - to: "us/states/ms/districts/house/42"
    rel: in-district
    area_weight: 0.2741
  - to: "us/states/ms/districts/house/39"
    rel: in-district
    area_weight: 0.1513
  - to: "us/states/ms/districts/house/41"
    rel: in-district
    area_weight: 0.072
  - to: "us/states/ms/districts/house/38"
    rel: in-district
    area_weight: 0.037
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lowndes County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57838 |
| Under 18 | 13745 |
| 18–64 | 34064 |
| 65+ | 10029 |
| Median household income | 53812 |
| Poverty rate | 17.26 |
| Homeownership rate | 61.28 |
| Unemployment rate | 6.33 |
| Median home value | 164100 |
| Gini index | 0.4763 |
| Vacancy rate | 15.32 |
| White | 28509 |
| Black | 25301 |
| Asian | 631 |
| Native | 139 |
| Hispanic/Latino | 1329 |
| Bachelor's or higher | 14520 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 17](/us/states/ms/districts/senate/17.md) — 94% (state senate)
- [MS Senate District 16](/us/states/ms/districts/senate/16.md) — 6% (state senate)
- [MS House District 37](/us/states/ms/districts/house/37.md) — 47% (state house)
- [MS House District 42](/us/states/ms/districts/house/42.md) — 27% (state house)
- [MS House District 39](/us/states/ms/districts/house/39.md) — 15% (state house)
- [MS House District 41](/us/states/ms/districts/house/41.md) — 7% (state house)
- [MS House District 38](/us/states/ms/districts/house/38.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
