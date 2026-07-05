---
type: Jurisdiction
title: "Pleasants County, WV"
classification: county
fips: "54073"
state: "WV"
demographics:
  population: 7521
  population_under_18: 1469
  population_18_64: 4623
  population_65_plus: 1429
  median_household_income: 60932
  poverty_rate: 11.59
  homeownership_rate: 81.44
  unemployment_rate: 8.55
  median_home_value: 151000
  gini_index: 0.5507
  vacancy_rate: 14.06
  race_white: 7149
  race_black: 31
  race_asian: 0
  race_native: 22
  hispanic: 158
  bachelors_plus: 1127
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/senate/3"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/9"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Pleasants County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7521 |
| Under 18 | 1469 |
| 18–64 | 4623 |
| 65+ | 1429 |
| Median household income | 60932 |
| Poverty rate | 11.59 |
| Homeownership rate | 81.44 |
| Unemployment rate | 8.55 |
| Median home value | 151000 |
| Gini index | 0.5507 |
| Vacancy rate | 14.06 |
| White | 7149 |
| Black | 31 |
| Asian | 0 |
| Native | 22 |
| Hispanic/Latino | 158 |
| Bachelor's or higher | 1127 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 3](/us/states/wv/districts/senate/3.md) — 100% (state senate)
- [WV House District 9](/us/states/wv/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
