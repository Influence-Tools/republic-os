---
type: Jurisdiction
title: "Stevens County, KS"
classification: county
fips: "20189"
state: "KS"
demographics:
  population: 5162
  population_under_18: 1486
  population_18_64: 2756
  population_65_plus: 920
  median_household_income: 64178
  poverty_rate: 14.25
  homeownership_rate: 74.47
  unemployment_rate: 3.11
  median_home_value: 129300
  gini_index: 0.4122
  vacancy_rate: 16.64
  race_white: 3483
  race_black: 6
  race_asian: 12
  race_native: 1
  hispanic: 2018
  bachelors_plus: 863
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/124"
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

# Stevens County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5162 |
| Under 18 | 1486 |
| 18–64 | 2756 |
| 65+ | 920 |
| Median household income | 64178 |
| Poverty rate | 14.25 |
| Homeownership rate | 74.47 |
| Unemployment rate | 3.11 |
| Median home value | 129300 |
| Gini index | 0.4122 |
| Vacancy rate | 16.64 |
| White | 3483 |
| Black | 6 |
| Asian | 12 |
| Native | 1 |
| Hispanic/Latino | 2018 |
| Bachelor's or higher | 863 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
