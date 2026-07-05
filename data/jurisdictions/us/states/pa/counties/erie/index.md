---
type: Jurisdiction
title: "Erie County, PA"
classification: county
fips: "42049"
state: "PA"
demographics:
  population: 269052
  population_under_18: 55689
  population_18_64: 160284
  population_65_plus: 53079
  median_household_income: 63354
  poverty_rate: 14.97
  homeownership_rate: 68.07
  unemployment_rate: 5.4
  median_home_value: 177000
  gini_index: 0.4636
  vacancy_rate: 7.93
  race_white: 222619
  race_black: 19375
  race_asian: 5909
  race_native: 369
  hispanic: 12851
  bachelors_plus: 78225
districts:
  - to: "us/states/pa/districts/16"
    rel: in-district
    area_weight: 0.5183
  - to: "us/states/pa/districts/senate/49"
    rel: in-district
    area_weight: 0.4678
  - to: "us/states/pa/districts/senate/21"
    rel: in-district
    area_weight: 0.0503
  - to: "us/states/pa/districts/house/4"
    rel: in-district
    area_weight: 0.3246
  - to: "us/states/pa/districts/house/6"
    rel: in-district
    area_weight: 0.0753
  - to: "us/states/pa/districts/house/2"
    rel: in-district
    area_weight: 0.0661
  - to: "us/states/pa/districts/house/3"
    rel: in-district
    area_weight: 0.0398
  - to: "us/states/pa/districts/house/1"
    rel: in-district
    area_weight: 0.0123
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Erie County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 269052 |
| Under 18 | 55689 |
| 18–64 | 160284 |
| 65+ | 53079 |
| Median household income | 63354 |
| Poverty rate | 14.97 |
| Homeownership rate | 68.07 |
| Unemployment rate | 5.4 |
| Median home value | 177000 |
| Gini index | 0.4636 |
| Vacancy rate | 7.93 |
| White | 222619 |
| Black | 19375 |
| Asian | 5909 |
| Native | 369 |
| Hispanic/Latino | 12851 |
| Bachelor's or higher | 78225 |

## Districts

- [PA-16](/us/states/pa/districts/16.md) — 52% (congressional)
- [PA Senate District 49](/us/states/pa/districts/senate/49.md) — 47% (state senate)
- [PA Senate District 21](/us/states/pa/districts/senate/21.md) — 5% (state senate)
- [PA House District 4](/us/states/pa/districts/house/4.md) — 32% (state house)
- [PA House District 6](/us/states/pa/districts/house/6.md) — 8% (state house)
- [PA House District 2](/us/states/pa/districts/house/2.md) — 7% (state house)
- [PA House District 3](/us/states/pa/districts/house/3.md) — 4% (state house)
- [PA House District 1](/us/states/pa/districts/house/1.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
