---
type: Jurisdiction
title: "Dade County, MO"
classification: county
fips: "29057"
state: "MO"
demographics:
  population: 7641
  population_under_18: 1589
  population_18_64: 4169
  population_65_plus: 1883
  median_household_income: 53750
  poverty_rate: 12.57
  homeownership_rate: 77.04
  unemployment_rate: 3.24
  median_home_value: 170600
  gini_index: 0.4384
  vacancy_rate: 19.0
  race_white: 7077
  race_black: 32
  race_asian: 10
  race_native: 31
  hispanic: 175
  bachelors_plus: 1122
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/20"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/house/127"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Dade County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7641 |
| Under 18 | 1589 |
| 18–64 | 4169 |
| 65+ | 1883 |
| Median household income | 53750 |
| Poverty rate | 12.57 |
| Homeownership rate | 77.04 |
| Unemployment rate | 3.24 |
| Median home value | 170600 |
| Gini index | 0.4384 |
| Vacancy rate | 19.0 |
| White | 7077 |
| Black | 32 |
| Asian | 10 |
| Native | 31 |
| Hispanic/Latino | 175 |
| Bachelor's or higher | 1122 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 20](/us/states/mo/districts/senate/20.md) — 100% (state senate)
- [MO House District 127](/us/states/mo/districts/house/127.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
