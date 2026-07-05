---
type: Jurisdiction
title: "Chase County, KS"
classification: county
fips: "20017"
state: "KS"
demographics:
  population: 2561
  population_under_18: 523
  population_18_64: 1392
  population_65_plus: 646
  median_household_income: 56484
  poverty_rate: 8.35
  homeownership_rate: 73.32
  unemployment_rate: 0.94
  median_home_value: 109700
  gini_index: 0.472
  vacancy_rate: 17.36
  race_white: 2276
  race_black: 27
  race_asian: 14
  race_native: 4
  hispanic: 216
  bachelors_plus: 711
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/13"
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

# Chase County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2561 |
| Under 18 | 523 |
| 18–64 | 1392 |
| 65+ | 646 |
| Median household income | 56484 |
| Poverty rate | 8.35 |
| Homeownership rate | 73.32 |
| Unemployment rate | 0.94 |
| Median home value | 109700 |
| Gini index | 0.472 |
| Vacancy rate | 17.36 |
| White | 2276 |
| Black | 27 |
| Asian | 14 |
| Native | 4 |
| Hispanic/Latino | 216 |
| Bachelor's or higher | 711 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 14](/us/states/ks/districts/senate/14.md) — 100% (state senate)
- [KS House District 13](/us/states/ks/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
