---
type: Jurisdiction
title: "Phillips County, KS"
classification: county
fips: "20147"
state: "KS"
demographics:
  population: 4813
  population_under_18: 1083
  population_18_64: 2500
  population_65_plus: 1230
  median_household_income: 62123
  poverty_rate: 15.36
  homeownership_rate: 78.0
  unemployment_rate: 3.22
  median_home_value: 96500
  gini_index: 0.4162
  vacancy_rate: 18.53
  race_white: 4453
  race_black: 36
  race_asian: 22
  race_native: 36
  hispanic: 165
  bachelors_plus: 1028
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.5997
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.4002
  - to: "us/states/ks/districts/house/110"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Phillips County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4813 |
| Under 18 | 1083 |
| 18–64 | 2500 |
| 65+ | 1230 |
| Median household income | 62123 |
| Poverty rate | 15.36 |
| Homeownership rate | 78.0 |
| Unemployment rate | 3.22 |
| Median home value | 96500 |
| Gini index | 0.4162 |
| Vacancy rate | 18.53 |
| White | 4453 |
| Black | 36 |
| Asian | 22 |
| Native | 36 |
| Hispanic/Latino | 165 |
| Bachelor's or higher | 1028 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 60% (state senate)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 40% (state senate)
- [KS House District 110](/us/states/ks/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
