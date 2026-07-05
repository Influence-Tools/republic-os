---
type: Jurisdiction
title: "Somerset County, NJ"
classification: county
fips: "34035"
state: "NJ"
demographics:
  population: 349846
  population_under_18: 74044
  population_18_64: 216265
  population_65_plus: 59537
  median_household_income: 140374
  poverty_rate: 5.37
  homeownership_rate: 74.3
  unemployment_rate: 4.74
  median_home_value: 552100
  gini_index: 0.4598
  vacancy_rate: 2.12
  race_white: 180538
  race_black: 33390
  race_asian: 68731
  race_native: 1478
  hispanic: 61585
  bachelors_plus: 209292
districts:
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.5909
  - to: "us/states/nj/districts/12"
    rel: in-district
    area_weight: 0.4087
  - to: "us/states/nj/districts/senate/16"
    rel: in-district
    area_weight: 0.3578
  - to: "us/states/nj/districts/senate/21"
    rel: in-district
    area_weight: 0.2562
  - to: "us/states/nj/districts/senate/23"
    rel: in-district
    area_weight: 0.2208
  - to: "us/states/nj/districts/senate/17"
    rel: in-district
    area_weight: 0.1559
  - to: "us/states/nj/districts/senate/22"
    rel: in-district
    area_weight: 0.0093
  - to: "us/states/nj/districts/house/16"
    rel: in-district
    area_weight: 0.3578
  - to: "us/states/nj/districts/house/21"
    rel: in-district
    area_weight: 0.2562
  - to: "us/states/nj/districts/house/23"
    rel: in-district
    area_weight: 0.2208
  - to: "us/states/nj/districts/house/17"
    rel: in-district
    area_weight: 0.1559
  - to: "us/states/nj/districts/house/22"
    rel: in-district
    area_weight: 0.0093
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Somerset County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 349846 |
| Under 18 | 74044 |
| 18–64 | 216265 |
| 65+ | 59537 |
| Median household income | 140374 |
| Poverty rate | 5.37 |
| Homeownership rate | 74.3 |
| Unemployment rate | 4.74 |
| Median home value | 552100 |
| Gini index | 0.4598 |
| Vacancy rate | 2.12 |
| White | 180538 |
| Black | 33390 |
| Asian | 68731 |
| Native | 1478 |
| Hispanic/Latino | 61585 |
| Bachelor's or higher | 209292 |

## Districts

- [NJ-07](/us/states/nj/districts/07.md) — 59% (congressional)
- [NJ-12](/us/states/nj/districts/12.md) — 41% (congressional)
- [NJ Senate District 16](/us/states/nj/districts/senate/16.md) — 36% (state senate)
- [NJ Senate District 21](/us/states/nj/districts/senate/21.md) — 26% (state senate)
- [NJ Senate District 23](/us/states/nj/districts/senate/23.md) — 22% (state senate)
- [NJ Senate District 17](/us/states/nj/districts/senate/17.md) — 16% (state senate)
- [NJ Senate District 22](/us/states/nj/districts/senate/22.md) — 1% (state senate)
- [NJ House District 16](/us/states/nj/districts/house/16.md) — 36% (state house)
- [NJ House District 21](/us/states/nj/districts/house/21.md) — 26% (state house)
- [NJ House District 23](/us/states/nj/districts/house/23.md) — 22% (state house)
- [NJ House District 17](/us/states/nj/districts/house/17.md) — 16% (state house)
- [NJ House District 22](/us/states/nj/districts/house/22.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
