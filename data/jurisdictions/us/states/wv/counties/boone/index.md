---
type: Jurisdiction
title: "Boone County, WV"
classification: county
fips: "54005"
state: "WV"
demographics:
  population: 21026
  population_under_18: 4317
  population_18_64: 12053
  population_65_plus: 4656
  median_household_income: 57093
  poverty_rate: 16.24
  homeownership_rate: 81.32
  unemployment_rate: 8.89
  median_home_value: 93100
  gini_index: 0.4246
  vacancy_rate: 21.9
  race_white: 20470
  race_black: 86
  race_asian: 36
  race_native: 5
  hispanic: 143
  bachelors_plus: 2338
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/7"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/house/32"
    rel: in-district
    area_weight: 0.9208
  - to: "us/states/wv/districts/house/31"
    rel: in-district
    area_weight: 0.0784
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Boone County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21026 |
| Under 18 | 4317 |
| 18–64 | 12053 |
| 65+ | 4656 |
| Median household income | 57093 |
| Poverty rate | 16.24 |
| Homeownership rate | 81.32 |
| Unemployment rate | 8.89 |
| Median home value | 93100 |
| Gini index | 0.4246 |
| Vacancy rate | 21.9 |
| White | 20470 |
| Black | 86 |
| Asian | 36 |
| Native | 5 |
| Hispanic/Latino | 143 |
| Bachelor's or higher | 2338 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 7](/us/states/wv/districts/senate/7.md) — 100% (state senate)
- [WV House District 32](/us/states/wv/districts/house/32.md) — 92% (state house)
- [WV House District 31](/us/states/wv/districts/house/31.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
