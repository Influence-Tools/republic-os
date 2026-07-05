---
type: Jurisdiction
title: "Washington County, KS"
classification: county
fips: "20201"
state: "KS"
demographics:
  population: 5533
  population_under_18: 1340
  population_18_64: 2886
  population_65_plus: 1307
  median_household_income: 65482
  poverty_rate: 9.28
  homeownership_rate: 78.47
  unemployment_rate: 1.09
  median_home_value: 117100
  gini_index: 0.4336
  vacancy_rate: 12.56
  race_white: 5064
  race_black: 8
  race_asian: 22
  race_native: 22
  hispanic: 269
  bachelors_plus: 1281
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/106"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Washington County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5533 |
| Under 18 | 1340 |
| 18–64 | 2886 |
| 65+ | 1307 |
| Median household income | 65482 |
| Poverty rate | 9.28 |
| Homeownership rate | 78.47 |
| Unemployment rate | 1.09 |
| Median home value | 117100 |
| Gini index | 0.4336 |
| Vacancy rate | 12.56 |
| White | 5064 |
| Black | 8 |
| Asian | 22 |
| Native | 22 |
| Hispanic/Latino | 269 |
| Bachelor's or higher | 1281 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 106](/us/states/ks/districts/house/106.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
