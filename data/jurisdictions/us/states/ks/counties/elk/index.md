---
type: Jurisdiction
title: "Elk County, KS"
classification: county
fips: "20049"
state: "KS"
demographics:
  population: 2453
  population_under_18: 567
  population_18_64: 1187
  population_65_plus: 699
  median_household_income: 64609
  poverty_rate: 10.37
  homeownership_rate: 78.78
  unemployment_rate: 2.03
  median_home_value: 68500
  gini_index: 0.3945
  vacancy_rate: 33.0
  race_white: 2167
  race_black: 2
  race_asian: 6
  race_native: 18
  hispanic: 110
  bachelors_plus: 477
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/12"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Elk County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2453 |
| Under 18 | 567 |
| 18–64 | 1187 |
| 65+ | 699 |
| Median household income | 64609 |
| Poverty rate | 10.37 |
| Homeownership rate | 78.78 |
| Unemployment rate | 2.03 |
| Median home value | 68500 |
| Gini index | 0.3945 |
| Vacancy rate | 33.0 |
| White | 2167 |
| Black | 2 |
| Asian | 6 |
| Native | 18 |
| Hispanic/Latino | 110 |
| Bachelor's or higher | 477 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 15](/us/states/ks/districts/senate/15.md) — 100% (state senate)
- [KS House District 12](/us/states/ks/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
