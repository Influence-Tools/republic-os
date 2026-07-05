---
type: Jurisdiction
title: "Loudon County, TN"
classification: county
fips: "47105"
state: "TN"
demographics:
  population: 58580
  population_under_18: 11121
  population_18_64: 31336
  population_65_plus: 16123
  median_household_income: 84185
  poverty_rate: 12.61
  homeownership_rate: 80.28
  unemployment_rate: 2.78
  median_home_value: 348000
  gini_index: 0.435
  vacancy_rate: 7.63
  race_white: 51108
  race_black: 743
  race_asian: 526
  race_native: 59
  hispanic: 6095
  bachelors_plus: 17829
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.9809
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.0191
  - to: "us/states/tn/districts/senate/5"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/house/21"
    rel: in-district
    area_weight: 0.8046
  - to: "us/states/tn/districts/house/32"
    rel: in-district
    area_weight: 0.1953
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Loudon County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58580 |
| Under 18 | 11121 |
| 18–64 | 31336 |
| 65+ | 16123 |
| Median household income | 84185 |
| Poverty rate | 12.61 |
| Homeownership rate | 80.28 |
| Unemployment rate | 2.78 |
| Median home value | 348000 |
| Gini index | 0.435 |
| Vacancy rate | 7.63 |
| White | 51108 |
| Black | 743 |
| Asian | 526 |
| Native | 59 |
| Hispanic/Latino | 6095 |
| Bachelor's or higher | 17829 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 98% (congressional)
- [TN-03](/us/states/tn/districts/03.md) — 2% (congressional)
- [TN Senate District 5](/us/states/tn/districts/senate/5.md) — 100% (state senate)
- [TN House District 21](/us/states/tn/districts/house/21.md) — 80% (state house)
- [TN House District 32](/us/states/tn/districts/house/32.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
