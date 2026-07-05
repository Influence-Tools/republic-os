---
type: Jurisdiction
title: "McLeod County, MN"
classification: county
fips: "27085"
state: "MN"
demographics:
  population: 36798
  population_under_18: 8064
  population_18_64: 21341
  population_65_plus: 7393
  median_household_income: 80084
  poverty_rate: 8.67
  homeownership_rate: 77.43
  unemployment_rate: 3.33
  median_home_value: 246100
  gini_index: 0.4264
  vacancy_rate: 4.74
  race_white: 32972
  race_black: 224
  race_asian: 232
  race_native: 80
  hispanic: 2796
  bachelors_plus: 6842
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/17a"
    rel: in-district
    area_weight: 0.7896
  - to: "us/states/mn/districts/house/17b"
    rel: in-district
    area_weight: 0.2103
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# McLeod County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36798 |
| Under 18 | 8064 |
| 18–64 | 21341 |
| 65+ | 7393 |
| Median household income | 80084 |
| Poverty rate | 8.67 |
| Homeownership rate | 77.43 |
| Unemployment rate | 3.33 |
| Median home value | 246100 |
| Gini index | 0.4264 |
| Vacancy rate | 4.74 |
| White | 32972 |
| Black | 224 |
| Asian | 232 |
| Native | 80 |
| Hispanic/Latino | 2796 |
| Bachelor's or higher | 6842 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 17](/us/states/mn/districts/senate/17.md) — 100% (state senate)
- [MN House District 17A](/us/states/mn/districts/house/17a.md) — 79% (state house)
- [MN House District 17B](/us/states/mn/districts/house/17b.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
