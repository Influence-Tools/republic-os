---
type: Jurisdiction
title: "Raleigh County, WV"
classification: county
fips: "54081"
state: "WV"
demographics:
  population: 73195
  population_under_18: 15392
  population_18_64: 41595
  population_65_plus: 16208
  median_household_income: 52150
  poverty_rate: 22.82
  homeownership_rate: 75.33
  unemployment_rate: 5.0
  median_home_value: 150900
  gini_index: 0.4896
  vacancy_rate: 16.18
  race_white: 63941
  race_black: 5015
  race_asian: 632
  race_native: 12
  hispanic: 1298
  bachelors_plus: 16052
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/9"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/43"
    rel: in-district
    area_weight: 0.4249
  - to: "us/states/wv/districts/house/42"
    rel: in-district
    area_weight: 0.2787
  - to: "us/states/wv/districts/house/45"
    rel: in-district
    area_weight: 0.1502
  - to: "us/states/wv/districts/house/41"
    rel: in-district
    area_weight: 0.129
  - to: "us/states/wv/districts/house/44"
    rel: in-district
    area_weight: 0.0168
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Raleigh County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 73195 |
| Under 18 | 15392 |
| 18–64 | 41595 |
| 65+ | 16208 |
| Median household income | 52150 |
| Poverty rate | 22.82 |
| Homeownership rate | 75.33 |
| Unemployment rate | 5.0 |
| Median home value | 150900 |
| Gini index | 0.4896 |
| Vacancy rate | 16.18 |
| White | 63941 |
| Black | 5015 |
| Asian | 632 |
| Native | 12 |
| Hispanic/Latino | 1298 |
| Bachelor's or higher | 16052 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 9](/us/states/wv/districts/senate/9.md) — 100% (state senate)
- [WV House District 43](/us/states/wv/districts/house/43.md) — 42% (state house)
- [WV House District 42](/us/states/wv/districts/house/42.md) — 28% (state house)
- [WV House District 45](/us/states/wv/districts/house/45.md) — 15% (state house)
- [WV House District 41](/us/states/wv/districts/house/41.md) — 13% (state house)
- [WV House District 44](/us/states/wv/districts/house/44.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
