---
type: Jurisdiction
title: "Clay County, KS"
classification: county
fips: "20027"
state: "KS"
demographics:
  population: 8048
  population_under_18: 1853
  population_18_64: 4249
  population_65_plus: 1946
  median_household_income: 66176
  poverty_rate: 13.35
  homeownership_rate: 78.0
  unemployment_rate: 1.03
  median_home_value: 155900
  gini_index: 0.4309
  vacancy_rate: 10.7
  race_white: 7410
  race_black: 193
  race_asian: 45
  race_native: 38
  hispanic: 284
  bachelors_plus: 1882
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/64"
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

# Clay County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8048 |
| Under 18 | 1853 |
| 18–64 | 4249 |
| 65+ | 1946 |
| Median household income | 66176 |
| Poverty rate | 13.35 |
| Homeownership rate | 78.0 |
| Unemployment rate | 1.03 |
| Median home value | 155900 |
| Gini index | 0.4309 |
| Vacancy rate | 10.7 |
| White | 7410 |
| Black | 193 |
| Asian | 45 |
| Native | 38 |
| Hispanic/Latino | 284 |
| Bachelor's or higher | 1882 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 64](/us/states/ks/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
