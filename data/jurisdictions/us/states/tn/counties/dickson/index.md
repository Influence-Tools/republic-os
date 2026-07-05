---
type: Jurisdiction
title: "Dickson County, TN"
classification: county
fips: "47043"
state: "TN"
demographics:
  population: 55983
  population_under_18: 13705
  population_18_64: 18188
  population_65_plus: 24090
  median_household_income: 75003
  poverty_rate: 10.86
  homeownership_rate: 80.27
  unemployment_rate: 3.37
  median_home_value: 306400
  gini_index: 0.4281
  vacancy_rate: 8.03
  race_white: 49567
  race_black: 2093
  race_asian: 83
  race_native: 101
  hispanic: 2835
  bachelors_plus: 11520
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/house/69"
    rel: in-district
    area_weight: 0.602
  - to: "us/states/tn/districts/house/78"
    rel: in-district
    area_weight: 0.3979
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Dickson County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55983 |
| Under 18 | 13705 |
| 18–64 | 18188 |
| 65+ | 24090 |
| Median household income | 75003 |
| Poverty rate | 10.86 |
| Homeownership rate | 80.27 |
| Unemployment rate | 3.37 |
| Median home value | 306400 |
| Gini index | 0.4281 |
| Vacancy rate | 8.03 |
| White | 49567 |
| Black | 2093 |
| Asian | 83 |
| Native | 101 |
| Hispanic/Latino | 2835 |
| Bachelor's or higher | 11520 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 23](/us/states/tn/districts/senate/23.md) — 100% (state senate)
- [TN House District 69](/us/states/tn/districts/house/69.md) — 60% (state house)
- [TN House District 78](/us/states/tn/districts/house/78.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
