---
type: Jurisdiction
title: "Liberty County, GA"
classification: county
fips: "13179"
state: "GA"
demographics:
  population: 67397
  population_under_18: 18733
  population_18_64: 41836
  population_65_plus: 6828
  median_household_income: 60456
  poverty_rate: 15.32
  homeownership_rate: 50.86
  unemployment_rate: 7.94
  median_home_value: 201500
  gini_index: 0.4114
  vacancy_rate: 13.29
  race_white: 25712
  race_black: 28503
  race_asian: 1175
  race_native: 345
  hispanic: 8535
  bachelors_plus: 10564
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.8988
  - to: "us/states/ga/districts/senate/1"
    rel: in-district
    area_weight: 0.8981
  - to: "us/states/ga/districts/house/168"
    rel: in-district
    area_weight: 0.5982
  - to: "us/states/ga/districts/house/167"
    rel: in-district
    area_weight: 0.2996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Liberty County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67397 |
| Under 18 | 18733 |
| 18–64 | 41836 |
| 65+ | 6828 |
| Median household income | 60456 |
| Poverty rate | 15.32 |
| Homeownership rate | 50.86 |
| Unemployment rate | 7.94 |
| Median home value | 201500 |
| Gini index | 0.4114 |
| Vacancy rate | 13.29 |
| White | 25712 |
| Black | 28503 |
| Asian | 1175 |
| Native | 345 |
| Hispanic/Latino | 8535 |
| Bachelor's or higher | 10564 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 90% (congressional)
- [GA Senate District 1](/us/states/ga/districts/senate/1.md) — 90% (state senate)
- [GA House District 168](/us/states/ga/districts/house/168.md) — 60% (state house)
- [GA House District 167](/us/states/ga/districts/house/167.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
