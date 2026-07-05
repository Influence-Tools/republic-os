---
type: Jurisdiction
title: "Rice County, KS"
classification: county
fips: "20159"
state: "KS"
demographics:
  population: 9350
  population_under_18: 2190
  population_18_64: 5383
  population_65_plus: 1777
  median_household_income: 63925
  poverty_rate: 7.74
  homeownership_rate: 77.41
  unemployment_rate: 4.38
  median_home_value: 104600
  gini_index: 0.428
  vacancy_rate: 15.28
  race_white: 7379
  race_black: 169
  race_asian: 3
  race_native: 70
  hispanic: 1305
  bachelors_plus: 2124
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/113"
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

# Rice County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9350 |
| Under 18 | 2190 |
| 18–64 | 5383 |
| 65+ | 1777 |
| Median household income | 63925 |
| Poverty rate | 7.74 |
| Homeownership rate | 77.41 |
| Unemployment rate | 4.38 |
| Median home value | 104600 |
| Gini index | 0.428 |
| Vacancy rate | 15.28 |
| White | 7379 |
| Black | 169 |
| Asian | 3 |
| Native | 70 |
| Hispanic/Latino | 1305 |
| Bachelor's or higher | 2124 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 113](/us/states/ks/districts/house/113.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
