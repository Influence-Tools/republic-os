---
type: Jurisdiction
title: "Yalobusha County, MS"
classification: county
fips: "28161"
state: "MS"
demographics:
  population: 12419
  population_under_18: 2716
  population_18_64: 6979
  population_65_plus: 2724
  median_household_income: 49151
  poverty_rate: 21.51
  homeownership_rate: 69.32
  unemployment_rate: 5.86
  median_home_value: 122300
  gini_index: 0.4536
  vacancy_rate: 23.19
  race_white: 7150
  race_black: 4598
  race_asian: 19
  race_native: 44
  hispanic: 216
  bachelors_plus: 2005
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/34"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Yalobusha County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12419 |
| Under 18 | 2716 |
| 18–64 | 6979 |
| 65+ | 2724 |
| Median household income | 49151 |
| Poverty rate | 21.51 |
| Homeownership rate | 69.32 |
| Unemployment rate | 5.86 |
| Median home value | 122300 |
| Gini index | 0.4536 |
| Vacancy rate | 23.19 |
| White | 7150 |
| Black | 4598 |
| Asian | 19 |
| Native | 44 |
| Hispanic/Latino | 216 |
| Bachelor's or higher | 2005 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 8](/us/states/ms/districts/senate/8.md) — 100% (state senate)
- [MS House District 34](/us/states/ms/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
