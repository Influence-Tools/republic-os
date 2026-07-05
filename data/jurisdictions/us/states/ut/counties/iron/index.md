---
type: Jurisdiction
title: "Iron County, UT"
classification: county
fips: "49021"
state: "UT"
demographics:
  population: 62252
  population_under_18: 16889
  population_18_64: 36768
  population_65_plus: 8595
  median_household_income: 66247
  poverty_rate: 13.83
  homeownership_rate: 68.28
  unemployment_rate: 3.93
  median_home_value: 379000
  gini_index: 0.4436
  vacancy_rate: 14.41
  race_white: 54088
  race_black: 435
  race_asian: 789
  race_native: 883
  hispanic: 6534
  bachelors_plus: 15120
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/house/70"
    rel: in-district
    area_weight: 0.7183
  - to: "us/states/ut/districts/house/71"
    rel: in-district
    area_weight: 0.2815
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Iron County, UT

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62252 |
| Under 18 | 16889 |
| 18–64 | 36768 |
| 65+ | 8595 |
| Median household income | 66247 |
| Poverty rate | 13.83 |
| Homeownership rate | 68.28 |
| Unemployment rate | 3.93 |
| Median home value | 379000 |
| Gini index | 0.4436 |
| Vacancy rate | 14.41 |
| White | 54088 |
| Black | 435 |
| Asian | 789 |
| Native | 883 |
| Hispanic/Latino | 6534 |
| Bachelor's or higher | 15120 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 28](/us/states/ut/districts/senate/28.md) — 100% (state senate)
- [UT House District 70](/us/states/ut/districts/house/70.md) — 72% (state house)
- [UT House District 71](/us/states/ut/districts/house/71.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
