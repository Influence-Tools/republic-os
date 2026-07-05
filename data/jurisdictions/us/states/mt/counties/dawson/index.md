---
type: Jurisdiction
title: "Dawson County, MT"
classification: county
fips: "30021"
state: "MT"
demographics:
  population: 8827
  population_under_18: 1885
  population_18_64: 5074
  population_65_plus: 1868
  median_household_income: 71334
  poverty_rate: 8.71
  homeownership_rate: 71.89
  unemployment_rate: 2.66
  median_home_value: 185300
  gini_index: 0.4073
  vacancy_rate: 17.48
  race_white: 8188
  race_black: 23
  race_asian: 29
  race_native: 119
  hispanic: 319
  bachelors_plus: 1789
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/house/33"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Dawson County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8827 |
| Under 18 | 1885 |
| 18–64 | 5074 |
| 65+ | 1868 |
| Median household income | 71334 |
| Poverty rate | 8.71 |
| Homeownership rate | 71.89 |
| Unemployment rate | 2.66 |
| Median home value | 185300 |
| Gini index | 0.4073 |
| Vacancy rate | 17.48 |
| White | 8188 |
| Black | 23 |
| Asian | 29 |
| Native | 119 |
| Hispanic/Latino | 319 |
| Bachelor's or higher | 1789 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 33](/us/states/mt/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
