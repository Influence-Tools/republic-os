---
type: Jurisdiction
title: "Norton County, KS"
classification: county
fips: "20137"
state: "KS"
demographics:
  population: 5359
  population_under_18: 1077
  population_18_64: 3195
  population_65_plus: 1087
  median_household_income: 54050
  poverty_rate: 7.2
  homeownership_rate: 76.2
  unemployment_rate: 1.68
  median_home_value: 101500
  gini_index: 0.3789
  vacancy_rate: 18.37
  race_white: 4778
  race_black: 167
  race_asian: 7
  race_native: 59
  hispanic: 315
  bachelors_plus: 1107
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/110"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Norton County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5359 |
| Under 18 | 1077 |
| 18–64 | 3195 |
| 65+ | 1087 |
| Median household income | 54050 |
| Poverty rate | 7.2 |
| Homeownership rate | 76.2 |
| Unemployment rate | 1.68 |
| Median home value | 101500 |
| Gini index | 0.3789 |
| Vacancy rate | 18.37 |
| White | 4778 |
| Black | 167 |
| Asian | 7 |
| Native | 59 |
| Hispanic/Latino | 315 |
| Bachelor's or higher | 1107 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 110](/us/states/ks/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
