---
type: Jurisdiction
title: "Clay County, TN"
classification: county
fips: "47027"
state: "TN"
demographics:
  population: 7670
  population_under_18: 1613
  population_18_64: 1928
  population_65_plus: 4129
  median_household_income: 39972
  poverty_rate: 24.2
  homeownership_rate: 74.38
  unemployment_rate: 10.05
  median_home_value: 136400
  gini_index: 0.4369
  vacancy_rate: 12.96
  race_white: 7214
  race_black: 256
  race_asian: 41
  race_native: 20
  hispanic: 18
  bachelors_plus: 1005
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/tn/districts/house/38"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Clay County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7670 |
| Under 18 | 1613 |
| 18–64 | 1928 |
| 65+ | 4129 |
| Median household income | 39972 |
| Poverty rate | 24.2 |
| Homeownership rate | 74.38 |
| Unemployment rate | 10.05 |
| Median home value | 136400 |
| Gini index | 0.4369 |
| Vacancy rate | 12.96 |
| White | 7214 |
| Black | 256 |
| Asian | 41 |
| Native | 20 |
| Hispanic/Latino | 18 |
| Bachelor's or higher | 1005 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 38](/us/states/tn/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
