---
type: Jurisdiction
title: "Nye County, NV"
classification: county
fips: "32023"
state: "NV"
demographics:
  population: 54344
  population_under_18: 9016
  population_18_64: 28537
  population_65_plus: 16791
  median_household_income: 60714
  poverty_rate: 14.14
  homeownership_rate: 77.79
  unemployment_rate: 8.07
  median_home_value: 290900
  gini_index: 0.4464
  vacancy_rate: 12.31
  race_white: 39769
  race_black: 1565
  race_asian: 1037
  race_native: 547
  hispanic: 9305
  bachelors_plus: 7344
districts:
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 0.7409
  - to: "us/states/nv/districts/senate/17"
    rel: in-district
    area_weight: 0.259
  - to: "us/states/nv/districts/house/33"
    rel: in-district
    area_weight: 0.7307
  - to: "us/states/nv/districts/house/38"
    rel: in-district
    area_weight: 0.259
  - to: "us/states/nv/districts/house/36"
    rel: in-district
    area_weight: 0.0102
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Nye County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54344 |
| Under 18 | 9016 |
| 18–64 | 28537 |
| 65+ | 16791 |
| Median household income | 60714 |
| Poverty rate | 14.14 |
| Homeownership rate | 77.79 |
| Unemployment rate | 8.07 |
| Median home value | 290900 |
| Gini index | 0.4464 |
| Vacancy rate | 12.31 |
| White | 39769 |
| Black | 1565 |
| Asian | 1037 |
| Native | 547 |
| Hispanic/Latino | 9305 |
| Bachelor's or higher | 7344 |

## Districts

- [NV-04](/us/states/nv/districts/04.md) — 100% (congressional)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 74% (state senate)
- [NV Senate District 17](/us/states/nv/districts/senate/17.md) — 26% (state senate)
- [NV House District 33](/us/states/nv/districts/house/33.md) — 73% (state house)
- [NV House District 38](/us/states/nv/districts/house/38.md) — 26% (state house)
- [NV House District 36](/us/states/nv/districts/house/36.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
