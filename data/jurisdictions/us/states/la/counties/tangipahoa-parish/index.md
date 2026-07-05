---
type: Jurisdiction
title: "Tangipahoa Parish, LA"
classification: county
fips: "22105"
state: "LA"
demographics:
  population: 136738
  population_under_18: 33579
  population_18_64: 82125
  population_65_plus: 21034
  median_household_income: 56760
  poverty_rate: 19.18
  homeownership_rate: 70.27
  unemployment_rate: 5.96
  median_home_value: 212900
  gini_index: 0.4831
  vacancy_rate: 13.34
  race_white: 83696
  race_black: 40109
  race_asian: 1083
  race_native: 114
  hispanic: 7924
  bachelors_plus: 24596
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.6838
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.3154
  - to: "us/states/la/districts/senate/12"
    rel: in-district
    area_weight: 0.5795
  - to: "us/states/la/districts/senate/37"
    rel: in-district
    area_weight: 0.3824
  - to: "us/states/la/districts/house/73"
    rel: in-district
    area_weight: 0.3991
  - to: "us/states/la/districts/house/86"
    rel: in-district
    area_weight: 0.2911
  - to: "us/states/la/districts/house/72"
    rel: in-district
    area_weight: 0.2905
  - to: "us/states/la/districts/house/95"
    rel: in-district
    area_weight: 0.0189
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Tangipahoa Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 136738 |
| Under 18 | 33579 |
| 18–64 | 82125 |
| 65+ | 21034 |
| Median household income | 56760 |
| Poverty rate | 19.18 |
| Homeownership rate | 70.27 |
| Unemployment rate | 5.96 |
| Median home value | 212900 |
| Gini index | 0.4831 |
| Vacancy rate | 13.34 |
| White | 83696 |
| Black | 40109 |
| Asian | 1083 |
| Native | 114 |
| Hispanic/Latino | 7924 |
| Bachelor's or higher | 24596 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 68% (congressional)
- [LA-01](/us/states/la/districts/01.md) — 32% (congressional)
- [LA Senate District 12](/us/states/la/districts/senate/12.md) — 58% (state senate)
- [LA Senate District 37](/us/states/la/districts/senate/37.md) — 38% (state senate)
- [LA House District 73](/us/states/la/districts/house/73.md) — 40% (state house)
- [LA House District 86](/us/states/la/districts/house/86.md) — 29% (state house)
- [LA House District 72](/us/states/la/districts/house/72.md) — 29% (state house)
- [LA House District 95](/us/states/la/districts/house/95.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
