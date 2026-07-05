---
type: Jurisdiction
title: "Meeker County, MN"
classification: county
fips: "27093"
state: "MN"
demographics:
  population: 23468
  population_under_18: 5522
  population_18_64: 13012
  population_65_plus: 4934
  median_household_income: 75446
  poverty_rate: 9.07
  homeownership_rate: 79.26
  unemployment_rate: 3.18
  median_home_value: 249000
  gini_index: 0.4109
  vacancy_rate: 12.93
  race_white: 21849
  race_black: 72
  race_asian: 69
  race_native: 105
  hispanic: 1042
  bachelors_plus: 4222
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/16"
    rel: in-district
    area_weight: 0.6375
  - to: "us/states/mn/districts/senate/17"
    rel: in-district
    area_weight: 0.2785
  - to: "us/states/mn/districts/senate/29"
    rel: in-district
    area_weight: 0.0839
  - to: "us/states/mn/districts/house/16a"
    rel: in-district
    area_weight: 0.6375
  - to: "us/states/mn/districts/house/17a"
    rel: in-district
    area_weight: 0.2785
  - to: "us/states/mn/districts/house/29a"
    rel: in-district
    area_weight: 0.0839
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Meeker County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23468 |
| Under 18 | 5522 |
| 18–64 | 13012 |
| 65+ | 4934 |
| Median household income | 75446 |
| Poverty rate | 9.07 |
| Homeownership rate | 79.26 |
| Unemployment rate | 3.18 |
| Median home value | 249000 |
| Gini index | 0.4109 |
| Vacancy rate | 12.93 |
| White | 21849 |
| Black | 72 |
| Asian | 69 |
| Native | 105 |
| Hispanic/Latino | 1042 |
| Bachelor's or higher | 4222 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 16](/us/states/mn/districts/senate/16.md) — 64% (state senate)
- [MN Senate District 17](/us/states/mn/districts/senate/17.md) — 28% (state senate)
- [MN Senate District 29](/us/states/mn/districts/senate/29.md) — 8% (state senate)
- [MN House District 16A](/us/states/mn/districts/house/16a.md) — 64% (state house)
- [MN House District 17A](/us/states/mn/districts/house/17a.md) — 28% (state house)
- [MN House District 29A](/us/states/mn/districts/house/29a.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
