---
type: Jurisdiction
title: "Kandiyohi County, MN"
classification: county
fips: "27067"
state: "MN"
demographics:
  population: 44079
  population_under_18: 10807
  population_18_64: 24159
  population_65_plus: 9113
  median_household_income: 76592
  poverty_rate: 9.11
  homeownership_rate: 72.51
  unemployment_rate: 3.63
  median_home_value: 243200
  gini_index: 0.4153
  vacancy_rate: 13.44
  race_white: 34580
  race_black: 2287
  race_asian: 594
  race_native: 227
  hispanic: 6484
  bachelors_plus: 10631
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/16b"
    rel: in-district
    area_weight: 0.8326
  - to: "us/states/mn/districts/house/16a"
    rel: in-district
    area_weight: 0.1672
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Kandiyohi County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44079 |
| Under 18 | 10807 |
| 18–64 | 24159 |
| 65+ | 9113 |
| Median household income | 76592 |
| Poverty rate | 9.11 |
| Homeownership rate | 72.51 |
| Unemployment rate | 3.63 |
| Median home value | 243200 |
| Gini index | 0.4153 |
| Vacancy rate | 13.44 |
| White | 34580 |
| Black | 2287 |
| Asian | 594 |
| Native | 227 |
| Hispanic/Latino | 6484 |
| Bachelor's or higher | 10631 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 16](/us/states/mn/districts/senate/16.md) — 100% (state senate)
- [MN House District 16B](/us/states/mn/districts/house/16b.md) — 83% (state house)
- [MN House District 16A](/us/states/mn/districts/house/16a.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
