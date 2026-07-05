---
type: Jurisdiction
title: "Summit County, UT"
classification: county
fips: "49043"
state: "UT"
demographics:
  population: 42970
  population_under_18: 9946
  population_18_64: 26456
  population_65_plus: 6568
  median_household_income: 138114
  poverty_rate: 4.88
  homeownership_rate: 80.24
  unemployment_rate: 1.77
  median_home_value: 1067700
  gini_index: 0.5012
  vacancy_rate: 40.75
  race_white: 36536
  race_black: 159
  race_asian: 756
  race_native: 206
  hispanic: 4914
  bachelors_plus: 24338
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 0.6044
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 0.3956
  - to: "us/states/ut/districts/senate/20"
    rel: in-district
    area_weight: 0.7618
  - to: "us/states/ut/districts/senate/3"
    rel: in-district
    area_weight: 0.2381
  - to: "us/states/ut/districts/house/4"
    rel: in-district
    area_weight: 0.6278
  - to: "us/states/ut/districts/house/68"
    rel: in-district
    area_weight: 0.3494
  - to: "us/states/ut/districts/house/59"
    rel: in-district
    area_weight: 0.0213
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Summit County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42970 |
| Under 18 | 9946 |
| 18–64 | 26456 |
| 65+ | 6568 |
| Median household income | 138114 |
| Poverty rate | 4.88 |
| Homeownership rate | 80.24 |
| Unemployment rate | 1.77 |
| Median home value | 1067700 |
| Gini index | 0.5012 |
| Vacancy rate | 40.75 |
| White | 36536 |
| Black | 159 |
| Asian | 756 |
| Native | 206 |
| Hispanic/Latino | 4914 |
| Bachelor's or higher | 24338 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 60% (congressional)
- [UT-01](/us/states/ut/districts/01.md) — 40% (congressional)
- [UT Senate District 20](/us/states/ut/districts/senate/20.md) — 76% (state senate)
- [UT Senate District 3](/us/states/ut/districts/senate/3.md) — 24% (state senate)
- [UT House District 4](/us/states/ut/districts/house/4.md) — 63% (state house)
- [UT House District 68](/us/states/ut/districts/house/68.md) — 35% (state house)
- [UT House District 59](/us/states/ut/districts/house/59.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
