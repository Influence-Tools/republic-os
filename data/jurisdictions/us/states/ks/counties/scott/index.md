---
type: Jurisdiction
title: "Scott County, KS"
classification: county
fips: "20171"
state: "KS"
demographics:
  population: 5027
  population_under_18: 1232
  population_18_64: 2788
  population_65_plus: 1007
  median_household_income: 68839
  poverty_rate: 6.46
  homeownership_rate: 67.19
  unemployment_rate: 2.73
  median_home_value: 160000
  gini_index: 0.4006
  vacancy_rate: 1.93
  race_white: 4029
  race_black: 0
  race_asian: 0
  race_native: 62
  hispanic: 1096
  bachelors_plus: 1284
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/118"
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

# Scott County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5027 |
| Under 18 | 1232 |
| 18–64 | 2788 |
| 65+ | 1007 |
| Median household income | 68839 |
| Poverty rate | 6.46 |
| Homeownership rate | 67.19 |
| Unemployment rate | 2.73 |
| Median home value | 160000 |
| Gini index | 0.4006 |
| Vacancy rate | 1.93 |
| White | 4029 |
| Black | 0 |
| Asian | 0 |
| Native | 62 |
| Hispanic/Latino | 1096 |
| Bachelor's or higher | 1284 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
