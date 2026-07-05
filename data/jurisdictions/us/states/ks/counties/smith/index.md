---
type: Jurisdiction
title: "Smith County, KS"
classification: county
fips: "20183"
state: "KS"
demographics:
  population: 3552
  population_under_18: 712
  population_18_64: 1800
  population_65_plus: 1040
  median_household_income: 59135
  poverty_rate: 7.27
  homeownership_rate: 84.79
  unemployment_rate: 0.62
  median_home_value: 94100
  gini_index: 0.4248
  vacancy_rate: 22.04
  race_white: 3347
  race_black: 8
  race_asian: 8
  race_native: 12
  hispanic: 94
  bachelors_plus: 849
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
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

# Smith County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3552 |
| Under 18 | 712 |
| 18–64 | 1800 |
| 65+ | 1040 |
| Median household income | 59135 |
| Poverty rate | 7.27 |
| Homeownership rate | 84.79 |
| Unemployment rate | 0.62 |
| Median home value | 94100 |
| Gini index | 0.4248 |
| Vacancy rate | 22.04 |
| White | 3347 |
| Black | 8 |
| Asian | 8 |
| Native | 12 |
| Hispanic/Latino | 94 |
| Bachelor's or higher | 849 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 109](/us/states/ks/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
