---
type: Jurisdiction
title: "Storey County, NV"
classification: county
fips: "32029"
state: "NV"
demographics:
  population: 4140
  population_under_18: 556
  population_18_64: 2208
  population_65_plus: 1376
  median_household_income: 93409
  poverty_rate: 7.06
  homeownership_rate: 96.09
  unemployment_rate: 6.47
  median_home_value: 426400
  gini_index: 0.3967
  vacancy_rate: 7.16
  race_white: 3331
  race_black: 91
  race_asian: 55
  race_native: 2
  hispanic: 530
  bachelors_plus: 1572
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/senate/16"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nv/districts/house/40"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Storey County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4140 |
| Under 18 | 556 |
| 18–64 | 2208 |
| 65+ | 1376 |
| Median household income | 93409 |
| Poverty rate | 7.06 |
| Homeownership rate | 96.09 |
| Unemployment rate | 6.47 |
| Median home value | 426400 |
| Gini index | 0.3967 |
| Vacancy rate | 7.16 |
| White | 3331 |
| Black | 91 |
| Asian | 55 |
| Native | 2 |
| Hispanic/Latino | 530 |
| Bachelor's or higher | 1572 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 16](/us/states/nv/districts/senate/16.md) — 100% (state senate)
- [NV House District 40](/us/states/nv/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
