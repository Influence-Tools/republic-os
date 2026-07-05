---
type: Jurisdiction
title: "Hillsdale County, MI"
classification: county
fips: "26059"
state: "MI"
demographics:
  population: 45654
  population_under_18: 9826
  population_18_64: 26065
  population_65_plus: 9763
  median_household_income: 64242
  poverty_rate: 14.37
  homeownership_rate: 82.01
  unemployment_rate: 4.38
  median_home_value: 176100
  gini_index: 0.4307
  vacancy_rate: 16.99
  race_white: 42662
  race_black: 318
  race_asian: 117
  race_native: 31
  hispanic: 1283
  bachelors_plus: 9268
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/16"
    rel: in-district
    area_weight: 0.7034
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.2964
  - to: "us/states/mi/districts/house/35"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Hillsdale County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45654 |
| Under 18 | 9826 |
| 18–64 | 26065 |
| 65+ | 9763 |
| Median household income | 64242 |
| Poverty rate | 14.37 |
| Homeownership rate | 82.01 |
| Unemployment rate | 4.38 |
| Median home value | 176100 |
| Gini index | 0.4307 |
| Vacancy rate | 16.99 |
| White | 42662 |
| Black | 318 |
| Asian | 117 |
| Native | 31 |
| Hispanic/Latino | 1283 |
| Bachelor's or higher | 9268 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 16](/us/states/mi/districts/senate/16.md) — 70% (state senate)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 30% (state senate)
- [MI House District 35](/us/states/mi/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
