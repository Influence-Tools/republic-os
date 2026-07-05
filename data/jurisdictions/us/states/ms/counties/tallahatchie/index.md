---
type: Jurisdiction
title: "Tallahatchie County, MS"
classification: county
fips: "28135"
state: "MS"
demographics:
  population: 11764
  population_under_18: 2409
  population_18_64: 7220
  population_65_plus: 2135
  median_household_income: 37466
  poverty_rate: 24.62
  homeownership_rate: 64.51
  unemployment_rate: 10.18
  median_home_value: 82300
  gini_index: 0.4592
  vacancy_rate: 21.78
  race_white: 4314
  race_black: 7155
  race_asian: 4
  race_native: 30
  hispanic: 91
  bachelors_plus: 1313
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/24"
    rel: in-district
    area_weight: 0.8984
  - to: "us/states/ms/districts/senate/13"
    rel: in-district
    area_weight: 0.1013
  - to: "us/states/ms/districts/house/30"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Tallahatchie County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11764 |
| Under 18 | 2409 |
| 18–64 | 7220 |
| 65+ | 2135 |
| Median household income | 37466 |
| Poverty rate | 24.62 |
| Homeownership rate | 64.51 |
| Unemployment rate | 10.18 |
| Median home value | 82300 |
| Gini index | 0.4592 |
| Vacancy rate | 21.78 |
| White | 4314 |
| Black | 7155 |
| Asian | 4 |
| Native | 30 |
| Hispanic/Latino | 91 |
| Bachelor's or higher | 1313 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 24](/us/states/ms/districts/senate/24.md) — 90% (state senate)
- [MS Senate District 13](/us/states/ms/districts/senate/13.md) — 10% (state senate)
- [MS House District 30](/us/states/ms/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
