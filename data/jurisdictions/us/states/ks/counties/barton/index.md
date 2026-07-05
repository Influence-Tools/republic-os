---
type: Jurisdiction
title: "Barton County, KS"
classification: county
fips: "20009"
state: "KS"
demographics:
  population: 25097
  population_under_18: 6044
  population_18_64: 13844
  population_65_plus: 5209
  median_household_income: 58851
  poverty_rate: 15.4
  homeownership_rate: 65.16
  unemployment_rate: 3.89
  median_home_value: 126400
  gini_index: 0.4443
  vacancy_rate: 16.18
  race_white: 20421
  race_black: 159
  race_asian: 50
  race_native: 203
  hispanic: 4183
  bachelors_plus: 4720
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/112"
    rel: in-district
    area_weight: 0.8471
  - to: "us/states/ks/districts/house/113"
    rel: in-district
    area_weight: 0.1529
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Barton County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25097 |
| Under 18 | 6044 |
| 18–64 | 13844 |
| 65+ | 5209 |
| Median household income | 58851 |
| Poverty rate | 15.4 |
| Homeownership rate | 65.16 |
| Unemployment rate | 3.89 |
| Median home value | 126400 |
| Gini index | 0.4443 |
| Vacancy rate | 16.18 |
| White | 20421 |
| Black | 159 |
| Asian | 50 |
| Native | 203 |
| Hispanic/Latino | 4183 |
| Bachelor's or higher | 4720 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 112](/us/states/ks/districts/house/112.md) — 85% (state house)
- [KS House District 113](/us/states/ks/districts/house/113.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
