---
type: Jurisdiction
title: "Clark County, KS"
classification: county
fips: "20025"
state: "KS"
demographics:
  population: 1974
  population_under_18: 500
  population_18_64: 1023
  population_65_plus: 451
  median_household_income: 63043
  poverty_rate: 9.87
  homeownership_rate: 73.6
  unemployment_rate: 2.79
  median_home_value: 87600
  gini_index: 0.4219
  vacancy_rate: 24.16
  race_white: 1732
  race_black: 0
  race_asian: 7
  race_native: 18
  hispanic: 106
  bachelors_plus: 519
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/115"
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

# Clark County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1974 |
| Under 18 | 500 |
| 18–64 | 1023 |
| 65+ | 451 |
| Median household income | 63043 |
| Poverty rate | 9.87 |
| Homeownership rate | 73.6 |
| Unemployment rate | 2.79 |
| Median home value | 87600 |
| Gini index | 0.4219 |
| Vacancy rate | 24.16 |
| White | 1732 |
| Black | 0 |
| Asian | 7 |
| Native | 18 |
| Hispanic/Latino | 106 |
| Bachelor's or higher | 519 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 115](/us/states/ks/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
