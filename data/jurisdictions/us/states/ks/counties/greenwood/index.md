---
type: Jurisdiction
title: "Greenwood County, KS"
classification: county
fips: "20073"
state: "KS"
demographics:
  population: 5919
  population_under_18: 1271
  population_18_64: 3088
  population_65_plus: 1560
  median_household_income: 60042
  poverty_rate: 13.89
  homeownership_rate: 80.46
  unemployment_rate: 3.38
  median_home_value: 88700
  gini_index: 0.4969
  vacancy_rate: 27.28
  race_white: 5466
  race_black: 44
  race_asian: 0
  race_native: 126
  hispanic: 234
  bachelors_plus: 1234
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ks/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
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

# Greenwood County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5919 |
| Under 18 | 1271 |
| 18–64 | 3088 |
| 65+ | 1560 |
| Median household income | 60042 |
| Poverty rate | 13.89 |
| Homeownership rate | 80.46 |
| Unemployment rate | 3.38 |
| Median home value | 88700 |
| Gini index | 0.4969 |
| Vacancy rate | 27.28 |
| White | 5466 |
| Black | 44 |
| Asian | 0 |
| Native | 126 |
| Hispanic/Latino | 234 |
| Bachelor's or higher | 1234 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 14](/us/states/ks/districts/senate/14.md) — 100% (state senate)
- [KS House District 13](/us/states/ks/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
