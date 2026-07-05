---
type: Jurisdiction
title: "Pendleton County, WV"
classification: county
fips: "54071"
state: "WV"
demographics:
  population: 6043
  population_under_18: 1136
  population_18_64: 3105
  population_65_plus: 1802
  median_household_income: 64931
  poverty_rate: 16.55
  homeownership_rate: 84.93
  unemployment_rate: 6.34
  median_home_value: 183800
  gini_index: 0.4008
  vacancy_rate: 36.62
  race_white: 5707
  race_black: 117
  race_asian: 13
  race_native: 9
  hispanic: 134
  bachelors_plus: 1096
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9968
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/67"
    rel: in-district
    area_weight: 0.5132
  - to: "us/states/wv/districts/house/86"
    rel: in-district
    area_weight: 0.4864
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Pendleton County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6043 |
| Under 18 | 1136 |
| 18–64 | 3105 |
| 65+ | 1802 |
| Median household income | 64931 |
| Poverty rate | 16.55 |
| Homeownership rate | 84.93 |
| Unemployment rate | 6.34 |
| Median home value | 183800 |
| Gini index | 0.4008 |
| Vacancy rate | 36.62 |
| White | 5707 |
| Black | 117 |
| Asian | 13 |
| Native | 9 |
| Hispanic/Latino | 134 |
| Bachelor's or higher | 1096 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 67](/us/states/wv/districts/house/67.md) — 51% (state house)
- [WV House District 86](/us/states/wv/districts/house/86.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
