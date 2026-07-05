---
type: Jurisdiction
title: "Pondera County, MT"
classification: county
fips: "30073"
state: "MT"
demographics:
  population: 6035
  population_under_18: 1434
  population_18_64: 3282
  population_65_plus: 1319
  median_household_income: 52338
  poverty_rate: 21.94
  homeownership_rate: 67.72
  unemployment_rate: 5.83
  median_home_value: 206100
  gini_index: 0.4384
  vacancy_rate: 17.65
  race_white: 4788
  race_black: 1
  race_asian: 60
  race_native: 910
  hispanic: 154
  bachelors_plus: 1026
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.5171
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.4829
  - to: "us/states/mt/districts/senate/9"
    rel: in-district
    area_weight: 0.8273
  - to: "us/states/mt/districts/senate/8"
    rel: in-district
    area_weight: 0.1727
  - to: "us/states/mt/districts/house/18"
    rel: in-district
    area_weight: 0.8272
  - to: "us/states/mt/districts/house/15"
    rel: in-district
    area_weight: 0.1727
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Pondera County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6035 |
| Under 18 | 1434 |
| 18–64 | 3282 |
| 65+ | 1319 |
| Median household income | 52338 |
| Poverty rate | 21.94 |
| Homeownership rate | 67.72 |
| Unemployment rate | 5.83 |
| Median home value | 206100 |
| Gini index | 0.4384 |
| Vacancy rate | 17.65 |
| White | 4788 |
| Black | 1 |
| Asian | 60 |
| Native | 910 |
| Hispanic/Latino | 154 |
| Bachelor's or higher | 1026 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 52% (congressional)
- [MT-01](/us/states/mt/districts/01.md) — 48% (congressional)
- [MT Senate District 9](/us/states/mt/districts/senate/9.md) — 83% (state senate)
- [MT Senate District 8](/us/states/mt/districts/senate/8.md) — 17% (state senate)
- [MT House District 18](/us/states/mt/districts/house/18.md) — 83% (state house)
- [MT House District 15](/us/states/mt/districts/house/15.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
