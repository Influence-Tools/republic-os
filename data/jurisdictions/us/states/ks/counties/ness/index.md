---
type: Jurisdiction
title: "Ness County, KS"
classification: county
fips: "20135"
state: "KS"
demographics:
  population: 2653
  population_under_18: 524
  population_18_64: 1465
  population_65_plus: 664
  median_household_income: 68616
  poverty_rate: 11.23
  homeownership_rate: 81.57
  unemployment_rate: 0.81
  median_home_value: 89700
  gini_index: 0.465
  vacancy_rate: 19.38
  race_white: 2144
  race_black: 0
  race_asian: 5
  race_native: 14
  hispanic: 395
  bachelors_plus: 545
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/118"
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

# Ness County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2653 |
| Under 18 | 524 |
| 18–64 | 1465 |
| 65+ | 664 |
| Median household income | 68616 |
| Poverty rate | 11.23 |
| Homeownership rate | 81.57 |
| Unemployment rate | 0.81 |
| Median home value | 89700 |
| Gini index | 0.465 |
| Vacancy rate | 19.38 |
| White | 2144 |
| Black | 0 |
| Asian | 5 |
| Native | 14 |
| Hispanic/Latino | 395 |
| Bachelor's or higher | 545 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
