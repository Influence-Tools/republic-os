---
type: Jurisdiction
title: "Pulaski County, GA"
classification: county
fips: "13235"
state: "GA"
demographics:
  population: 9939
  population_under_18: 1735
  population_18_64: 5896
  population_65_plus: 2308
  median_household_income: 50406
  poverty_rate: 16.54
  homeownership_rate: 70.77
  unemployment_rate: 3.17
  median_home_value: 157600
  gini_index: 0.4812
  vacancy_rate: 21.99
  race_white: 6116
  race_black: 3067
  race_asian: 84
  race_native: 3
  hispanic: 565
  bachelors_plus: 1495
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/148"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Pulaski County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9939 |
| Under 18 | 1735 |
| 18–64 | 5896 |
| 65+ | 2308 |
| Median household income | 50406 |
| Poverty rate | 16.54 |
| Homeownership rate | 70.77 |
| Unemployment rate | 3.17 |
| Median home value | 157600 |
| Gini index | 0.4812 |
| Vacancy rate | 21.99 |
| White | 6116 |
| Black | 3067 |
| Asian | 84 |
| Native | 3 |
| Hispanic/Latino | 565 |
| Bachelor's or higher | 1495 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 148](/us/states/ga/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
