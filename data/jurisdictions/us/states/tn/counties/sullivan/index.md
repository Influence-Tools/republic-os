---
type: Jurisdiction
title: "Sullivan County, TN"
classification: county
fips: "47163"
state: "TN"
demographics:
  population: 160624
  population_under_18: 30610
  population_18_64: 94293
  population_65_plus: 35721
  median_household_income: 58807
  poverty_rate: 15.43
  homeownership_rate: 72.14
  unemployment_rate: 5.43
  median_home_value: 213300
  gini_index: 0.4674
  vacancy_rate: 9.72
  race_white: 148461
  race_black: 3307
  race_asian: 1204
  race_native: 178
  hispanic: 4217
  bachelors_plus: 42268
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/senate/4"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/house/1"
    rel: in-district
    area_weight: 0.3598
  - to: "us/states/tn/districts/house/3"
    rel: in-district
    area_weight: 0.3566
  - to: "us/states/tn/districts/house/2"
    rel: in-district
    area_weight: 0.283
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Sullivan County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160624 |
| Under 18 | 30610 |
| 18–64 | 94293 |
| 65+ | 35721 |
| Median household income | 58807 |
| Poverty rate | 15.43 |
| Homeownership rate | 72.14 |
| Unemployment rate | 5.43 |
| Median home value | 213300 |
| Gini index | 0.4674 |
| Vacancy rate | 9.72 |
| White | 148461 |
| Black | 3307 |
| Asian | 1204 |
| Native | 178 |
| Hispanic/Latino | 4217 |
| Bachelor's or higher | 42268 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 4](/us/states/tn/districts/senate/4.md) — 100% (state senate)
- [TN House District 1](/us/states/tn/districts/house/1.md) — 36% (state house)
- [TN House District 3](/us/states/tn/districts/house/3.md) — 36% (state house)
- [TN House District 2](/us/states/tn/districts/house/2.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
