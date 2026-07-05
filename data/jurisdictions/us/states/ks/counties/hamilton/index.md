---
type: Jurisdiction
title: "Hamilton County, KS"
classification: county
fips: "20075"
state: "KS"
demographics:
  population: 2471
  population_under_18: 836
  population_18_64: 1344
  population_65_plus: 291
  median_household_income: 70250
  poverty_rate: 7.03
  homeownership_rate: 77.15
  unemployment_rate: 3.06
  median_home_value: 115800
  gini_index: 0.4067
  vacancy_rate: 25.35
  race_white: 1548
  race_black: 1
  race_asian: 0
  race_native: 0
  hispanic: 1088
  bachelors_plus: 348
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/124"
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

# Hamilton County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2471 |
| Under 18 | 836 |
| 18–64 | 1344 |
| 65+ | 291 |
| Median household income | 70250 |
| Poverty rate | 7.03 |
| Homeownership rate | 77.15 |
| Unemployment rate | 3.06 |
| Median home value | 115800 |
| Gini index | 0.4067 |
| Vacancy rate | 25.35 |
| White | 1548 |
| Black | 1 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 1088 |
| Bachelor's or higher | 348 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
