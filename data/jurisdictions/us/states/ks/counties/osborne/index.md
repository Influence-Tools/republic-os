---
type: Jurisdiction
title: "Osborne County, KS"
classification: county
fips: "20141"
state: "KS"
demographics:
  population: 3452
  population_under_18: 762
  population_18_64: 1766
  population_65_plus: 924
  median_household_income: 63011
  poverty_rate: 8.44
  homeownership_rate: 77.2
  unemployment_rate: 1.64
  median_home_value: 86400
  gini_index: 0.4104
  vacancy_rate: 22.26
  race_white: 3186
  race_black: 12
  race_asian: 17
  race_native: 8
  hispanic: 103
  bachelors_plus: 758
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/109"
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

# Osborne County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3452 |
| Under 18 | 762 |
| 18–64 | 1766 |
| 65+ | 924 |
| Median household income | 63011 |
| Poverty rate | 8.44 |
| Homeownership rate | 77.2 |
| Unemployment rate | 1.64 |
| Median home value | 86400 |
| Gini index | 0.4104 |
| Vacancy rate | 22.26 |
| White | 3186 |
| Black | 12 |
| Asian | 17 |
| Native | 8 |
| Hispanic/Latino | 103 |
| Bachelor's or higher | 758 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 109](/us/states/ks/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
