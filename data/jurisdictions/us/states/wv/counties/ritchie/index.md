---
type: Jurisdiction
title: "Ritchie County, WV"
classification: county
fips: "54085"
state: "WV"
demographics:
  population: 8286
  population_under_18: 1646
  population_18_64: 4735
  population_65_plus: 1905
  median_household_income: 50582
  poverty_rate: 21.56
  homeownership_rate: 84.21
  unemployment_rate: 2.36
  median_home_value: 115900
  gini_index: 0.4416
  vacancy_rate: 18.85
  race_white: 8051
  race_black: 9
  race_asian: 111
  race_native: 0
  hispanic: 59
  bachelors_plus: 1054
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/wv/districts/senate/3"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/9"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Ritchie County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8286 |
| Under 18 | 1646 |
| 18–64 | 4735 |
| 65+ | 1905 |
| Median household income | 50582 |
| Poverty rate | 21.56 |
| Homeownership rate | 84.21 |
| Unemployment rate | 2.36 |
| Median home value | 115900 |
| Gini index | 0.4416 |
| Vacancy rate | 18.85 |
| White | 8051 |
| Black | 9 |
| Asian | 111 |
| Native | 0 |
| Hispanic/Latino | 59 |
| Bachelor's or higher | 1054 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 3](/us/states/wv/districts/senate/3.md) — 100% (state senate)
- [WV House District 9](/us/states/wv/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
