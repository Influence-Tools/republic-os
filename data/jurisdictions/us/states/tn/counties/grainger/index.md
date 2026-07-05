---
type: Jurisdiction
title: "Grainger County, TN"
classification: county
fips: "47057"
state: "TN"
demographics:
  population: 24266
  population_under_18: 4567
  population_18_64: 14237
  population_65_plus: 5462
  median_household_income: 50538
  poverty_rate: 17.07
  homeownership_rate: 77.12
  unemployment_rate: 4.68
  median_home_value: 189200
  gini_index: 0.4759
  vacancy_rate: 18.38
  race_white: 23185
  race_black: 324
  race_asian: 43
  race_native: 218
  hispanic: 877
  bachelors_plus: 4127
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.9885
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.0115
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/10"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Grainger County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24266 |
| Under 18 | 4567 |
| 18–64 | 14237 |
| 65+ | 5462 |
| Median household income | 50538 |
| Poverty rate | 17.07 |
| Homeownership rate | 77.12 |
| Unemployment rate | 4.68 |
| Median home value | 189200 |
| Gini index | 0.4759 |
| Vacancy rate | 18.38 |
| White | 23185 |
| Black | 324 |
| Asian | 43 |
| Native | 218 |
| Hispanic/Latino | 877 |
| Bachelor's or higher | 4127 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 99% (congressional)
- [TN-01](/us/states/tn/districts/01.md) — 1% (congressional)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 100% (state senate)
- [TN House District 10](/us/states/tn/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
