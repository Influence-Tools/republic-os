---
type: Jurisdiction
title: "Sherburne County, MN"
classification: county
fips: "27141"
state: "MN"
demographics:
  population: 100560
  population_under_18: 25908
  population_18_64: 62252
  population_65_plus: 12400
  median_household_income: 105466
  poverty_rate: 5.09
  homeownership_rate: 83.25
  unemployment_rate: 2.99
  median_home_value: 361400
  gini_index: 0.3883
  vacancy_rate: 4.16
  race_white: 87245
  race_black: 4085
  race_asian: 1680
  race_native: 337
  hispanic: 3400
  bachelors_plus: 25602
districts:
  - to: "us/states/mn/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/27"
    rel: in-district
    area_weight: 0.8801
  - to: "us/states/mn/districts/senate/30"
    rel: in-district
    area_weight: 0.0969
  - to: "us/states/mn/districts/senate/14"
    rel: in-district
    area_weight: 0.0228
  - to: "us/states/mn/districts/house/27a"
    rel: in-district
    area_weight: 0.6403
  - to: "us/states/mn/districts/house/27b"
    rel: in-district
    area_weight: 0.2398
  - to: "us/states/mn/districts/house/30b"
    rel: in-district
    area_weight: 0.0969
  - to: "us/states/mn/districts/house/14b"
    rel: in-district
    area_weight: 0.0227
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Sherburne County, MN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100560 |
| Under 18 | 25908 |
| 18–64 | 62252 |
| 65+ | 12400 |
| Median household income | 105466 |
| Poverty rate | 5.09 |
| Homeownership rate | 83.25 |
| Unemployment rate | 2.99 |
| Median home value | 361400 |
| Gini index | 0.3883 |
| Vacancy rate | 4.16 |
| White | 87245 |
| Black | 4085 |
| Asian | 1680 |
| Native | 337 |
| Hispanic/Latino | 3400 |
| Bachelor's or higher | 25602 |

## Districts

- [MN-06](/us/states/mn/districts/06.md) — 100% (congressional)
- [MN Senate District 27](/us/states/mn/districts/senate/27.md) — 88% (state senate)
- [MN Senate District 30](/us/states/mn/districts/senate/30.md) — 10% (state senate)
- [MN Senate District 14](/us/states/mn/districts/senate/14.md) — 2% (state senate)
- [MN House District 27A](/us/states/mn/districts/house/27a.md) — 64% (state house)
- [MN House District 27B](/us/states/mn/districts/house/27b.md) — 24% (state house)
- [MN House District 30B](/us/states/mn/districts/house/30b.md) — 10% (state house)
- [MN House District 14B](/us/states/mn/districts/house/14b.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
