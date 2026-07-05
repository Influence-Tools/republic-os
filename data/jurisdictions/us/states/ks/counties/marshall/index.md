---
type: Jurisdiction
title: "Marshall County, KS"
classification: county
fips: "20117"
state: "KS"
demographics:
  population: 9993
  population_under_18: 2420
  population_18_64: 5267
  population_65_plus: 2306
  median_household_income: 68419
  poverty_rate: 11.34
  homeownership_rate: 79.98
  unemployment_rate: 2.04
  median_home_value: 127700
  gini_index: 0.4324
  vacancy_rate: 12.1
  race_white: 9456
  race_black: 71
  race_asian: 33
  race_native: 31
  hispanic: 280
  bachelors_plus: 1817
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 0.7623
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.2373
  - to: "us/states/ks/districts/house/106"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Marshall County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9993 |
| Under 18 | 2420 |
| 18–64 | 5267 |
| 65+ | 2306 |
| Median household income | 68419 |
| Poverty rate | 11.34 |
| Homeownership rate | 79.98 |
| Unemployment rate | 2.04 |
| Median home value | 127700 |
| Gini index | 0.4324 |
| Vacancy rate | 12.1 |
| White | 9456 |
| Black | 71 |
| Asian | 33 |
| Native | 31 |
| Hispanic/Latino | 280 |
| Bachelor's or higher | 1817 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 76% (state senate)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 24% (state senate)
- [KS House District 106](/us/states/ks/districts/house/106.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
