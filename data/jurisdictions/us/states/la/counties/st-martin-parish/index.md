---
type: Jurisdiction
title: "St. Martin Parish, LA"
classification: county
fips: "22099"
state: "LA"
demographics:
  population: 51353
  population_under_18: 12336
  population_18_64: 30183
  population_65_plus: 8834
  median_household_income: 55960
  poverty_rate: 15.26
  homeownership_rate: 77.73
  unemployment_rate: 4.0
  median_home_value: 164200
  gini_index: 0.4651
  vacancy_rate: 17.83
  race_white: 32564
  race_black: 14690
  race_asian: 390
  race_native: 93
  hispanic: 1873
  bachelors_plus: 7397
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.9961
  - to: "us/states/la/districts/senate/22"
    rel: in-district
    area_weight: 0.6519
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.2598
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.0513
  - to: "us/states/la/districts/senate/24"
    rel: in-district
    area_weight: 0.0369
  - to: "us/states/la/districts/house/46"
    rel: in-district
    area_weight: 0.4673
  - to: "us/states/la/districts/house/50"
    rel: in-district
    area_weight: 0.2597
  - to: "us/states/la/districts/house/96"
    rel: in-district
    area_weight: 0.2342
  - to: "us/states/la/districts/house/48"
    rel: in-district
    area_weight: 0.0386
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Martin Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51353 |
| Under 18 | 12336 |
| 18–64 | 30183 |
| 65+ | 8834 |
| Median household income | 55960 |
| Poverty rate | 15.26 |
| Homeownership rate | 77.73 |
| Unemployment rate | 4.0 |
| Median home value | 164200 |
| Gini index | 0.4651 |
| Vacancy rate | 17.83 |
| White | 32564 |
| Black | 14690 |
| Asian | 390 |
| Native | 93 |
| Hispanic/Latino | 1873 |
| Bachelor's or higher | 7397 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 100% (congressional)
- [LA Senate District 22](/us/states/la/districts/senate/22.md) — 65% (state senate)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 26% (state senate)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 5% (state senate)
- [LA Senate District 24](/us/states/la/districts/senate/24.md) — 4% (state senate)
- [LA House District 46](/us/states/la/districts/house/46.md) — 47% (state house)
- [LA House District 50](/us/states/la/districts/house/50.md) — 26% (state house)
- [LA House District 96](/us/states/la/districts/house/96.md) — 23% (state house)
- [LA House District 48](/us/states/la/districts/house/48.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
