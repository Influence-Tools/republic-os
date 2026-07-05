---
type: Jurisdiction
title: "Tulare County, CA"
classification: county
fips: "06107"
state: "CA"
demographics:
  population: 478693
  population_under_18: 142421
  population_18_64: 279171
  population_65_plus: 57101
  median_household_income: 71300
  poverty_rate: 17.89
  homeownership_rate: 58.45
  unemployment_rate: 9.31
  median_home_value: 330100
  gini_index: 0.4361
  vacancy_rate: 7.14
  race_white: 177316
  race_black: 7451
  race_asian: 17582
  race_native: 7616
  hispanic: 318976
  bachelors_plus: 64642
districts:
  - to: "us/states/ca/districts/20"
    rel: in-district
    area_weight: 0.7056
  - to: "us/states/ca/districts/22"
    rel: in-district
    area_weight: 0.2024
  - to: "us/states/ca/districts/21"
    rel: in-district
    area_weight: 0.0908
  - to: "us/states/ca/districts/senate/12"
    rel: in-district
    area_weight: 0.7477
  - to: "us/states/ca/districts/senate/16"
    rel: in-district
    area_weight: 0.2522
  - to: "us/states/ca/districts/house/32"
    rel: in-district
    area_weight: 0.7422
  - to: "us/states/ca/districts/house/33"
    rel: in-district
    area_weight: 0.2578
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Tulare County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 478693 |
| Under 18 | 142421 |
| 18–64 | 279171 |
| 65+ | 57101 |
| Median household income | 71300 |
| Poverty rate | 17.89 |
| Homeownership rate | 58.45 |
| Unemployment rate | 9.31 |
| Median home value | 330100 |
| Gini index | 0.4361 |
| Vacancy rate | 7.14 |
| White | 177316 |
| Black | 7451 |
| Asian | 17582 |
| Native | 7616 |
| Hispanic/Latino | 318976 |
| Bachelor's or higher | 64642 |

## Districts

- [CA-20](/us/states/ca/districts/20.md) — 71% (congressional)
- [CA-22](/us/states/ca/districts/22.md) — 20% (congressional)
- [CA-21](/us/states/ca/districts/21.md) — 9% (congressional)
- [CA Senate District 12](/us/states/ca/districts/senate/12.md) — 75% (state senate)
- [CA Senate District 16](/us/states/ca/districts/senate/16.md) — 25% (state senate)
- [CA House District 32](/us/states/ca/districts/house/32.md) — 74% (state house)
- [CA House District 33](/us/states/ca/districts/house/33.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
