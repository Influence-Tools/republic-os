---
type: Jurisdiction
title: "Pushmataha County, OK"
classification: county
fips: "40127"
state: "OK"
demographics:
  population: 10790
  population_under_18: 2314
  population_18_64: 6028
  population_65_plus: 2448
  median_household_income: 47940
  poverty_rate: 20.71
  homeownership_rate: 74.86
  unemployment_rate: 4.41
  median_home_value: 132300
  gini_index: 0.4813
  vacancy_rate: 22.37
  race_white: 7511
  race_black: 157
  race_asian: 40
  race_native: 1802
  hispanic: 467
  bachelors_plus: 1774
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/5"
    rel: in-district
    area_weight: 0.6504
  - to: "us/states/ok/districts/senate/6"
    rel: in-district
    area_weight: 0.3495
  - to: "us/states/ok/districts/house/19"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Pushmataha County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10790 |
| Under 18 | 2314 |
| 18–64 | 6028 |
| 65+ | 2448 |
| Median household income | 47940 |
| Poverty rate | 20.71 |
| Homeownership rate | 74.86 |
| Unemployment rate | 4.41 |
| Median home value | 132300 |
| Gini index | 0.4813 |
| Vacancy rate | 22.37 |
| White | 7511 |
| Black | 157 |
| Asian | 40 |
| Native | 1802 |
| Hispanic/Latino | 467 |
| Bachelor's or higher | 1774 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 5](/us/states/ok/districts/senate/5.md) — 65% (state senate)
- [OK Senate District 6](/us/states/ok/districts/senate/6.md) — 35% (state senate)
- [OK House District 19](/us/states/ok/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
