---
type: Jurisdiction
title: "Saginaw County, MI"
classification: county
fips: "26145"
state: "MI"
demographics:
  population: 188665
  population_under_18: 40264
  population_18_64: 109972
  population_65_plus: 38429
  median_household_income: 60622
  poverty_rate: 18.21
  homeownership_rate: 74.1
  unemployment_rate: 6.4
  median_home_value: 152800
  gini_index: 0.4684
  vacancy_rate: 9.57
  race_white: 133402
  race_black: 35003
  race_asian: 2225
  race_native: 533
  hispanic: 17381
  bachelors_plus: 43489
districts:
  - to: "us/states/mi/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/26"
    rel: in-district
    area_weight: 0.5652
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.2564
  - to: "us/states/mi/districts/senate/35"
    rel: in-district
    area_weight: 0.1783
  - to: "us/states/mi/districts/house/93"
    rel: in-district
    area_weight: 0.4838
  - to: "us/states/mi/districts/house/97"
    rel: in-district
    area_weight: 0.3113
  - to: "us/states/mi/districts/house/71"
    rel: in-district
    area_weight: 0.1323
  - to: "us/states/mi/districts/house/94"
    rel: in-district
    area_weight: 0.0725
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Saginaw County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 188665 |
| Under 18 | 40264 |
| 18–64 | 109972 |
| 65+ | 38429 |
| Median household income | 60622 |
| Poverty rate | 18.21 |
| Homeownership rate | 74.1 |
| Unemployment rate | 6.4 |
| Median home value | 152800 |
| Gini index | 0.4684 |
| Vacancy rate | 9.57 |
| White | 133402 |
| Black | 35003 |
| Asian | 2225 |
| Native | 533 |
| Hispanic/Latino | 17381 |
| Bachelor's or higher | 43489 |

## Districts

- [MI-08](/us/states/mi/districts/08.md) — 100% (congressional)
- [MI Senate District 26](/us/states/mi/districts/senate/26.md) — 57% (state senate)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 26% (state senate)
- [MI Senate District 35](/us/states/mi/districts/senate/35.md) — 18% (state senate)
- [MI House District 93](/us/states/mi/districts/house/93.md) — 48% (state house)
- [MI House District 97](/us/states/mi/districts/house/97.md) — 31% (state house)
- [MI House District 71](/us/states/mi/districts/house/71.md) — 13% (state house)
- [MI House District 94](/us/states/mi/districts/house/94.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
