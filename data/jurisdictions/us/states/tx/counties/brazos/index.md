---
type: Jurisdiction
title: "Brazos County, TX"
classification: county
fips: "48041"
state: "TX"
demographics:
  population: 242311
  population_under_18: 48785
  population_18_64: 168814
  population_65_plus: 24712
  median_household_income: 58553
  poverty_rate: 24.27
  homeownership_rate: 46.84
  unemployment_rate: 4.72
  median_home_value: 296000
  gini_index: 0.5193
  vacancy_rate: 9.66
  race_white: 153237
  race_black: 25439
  race_asian: 14486
  race_native: 1533
  hispanic: 66411
  bachelors_plus: 80244
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/house/12"
    rel: in-district
    area_weight: 0.5978
  - to: "us/states/tx/districts/house/14"
    rel: in-district
    area_weight: 0.402
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Brazos County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 242311 |
| Under 18 | 48785 |
| 18–64 | 168814 |
| 65+ | 24712 |
| Median household income | 58553 |
| Poverty rate | 24.27 |
| Homeownership rate | 46.84 |
| Unemployment rate | 4.72 |
| Median home value | 296000 |
| Gini index | 0.5193 |
| Vacancy rate | 9.66 |
| White | 153237 |
| Black | 25439 |
| Asian | 14486 |
| Native | 1533 |
| Hispanic/Latino | 66411 |
| Bachelor's or higher | 80244 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 12](/us/states/tx/districts/house/12.md) — 60% (state house)
- [TX House District 14](/us/states/tx/districts/house/14.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
