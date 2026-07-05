---
type: Jurisdiction
title: "Doddridge County, WV"
classification: county
fips: "54017"
state: "WV"
demographics:
  population: 7711
  population_under_18: 1136
  population_18_64: 4907
  population_65_plus: 1668
  median_household_income: 57401
  poverty_rate: 14.84
  homeownership_rate: 88.8
  unemployment_rate: 5.73
  median_home_value: 160800
  gini_index: 0.4771
  vacancy_rate: 21.05
  race_white: 7137
  race_black: 189
  race_asian: 35
  race_native: 12
  hispanic: 110
  bachelors_plus: 1051
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/house/8"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Doddridge County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7711 |
| Under 18 | 1136 |
| 18–64 | 4907 |
| 65+ | 1668 |
| Median household income | 57401 |
| Poverty rate | 14.84 |
| Homeownership rate | 88.8 |
| Unemployment rate | 5.73 |
| Median home value | 160800 |
| Gini index | 0.4771 |
| Vacancy rate | 21.05 |
| White | 7137 |
| Black | 189 |
| Asian | 35 |
| Native | 12 |
| Hispanic/Latino | 110 |
| Bachelor's or higher | 1051 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 100% (state senate)
- [WV House District 8](/us/states/wv/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
