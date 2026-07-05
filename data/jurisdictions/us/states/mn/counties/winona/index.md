---
type: Jurisdiction
title: "Winona County, MN"
classification: county
fips: "27169"
state: "MN"
demographics:
  population: 49779
  population_under_18: 8769
  population_18_64: 31685
  population_65_plus: 9325
  median_household_income: 70744
  poverty_rate: 14.8
  homeownership_rate: 69.49
  unemployment_rate: 2.29
  median_home_value: 235400
  gini_index: 0.4507
  vacancy_rate: 7.33
  race_white: 44707
  race_black: 958
  race_asian: 1089
  race_native: 202
  hispanic: 1930
  bachelors_plus: 13651
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/26"
    rel: in-district
    area_weight: 0.6655
  - to: "us/states/mn/districts/senate/20"
    rel: in-district
    area_weight: 0.3343
  - to: "us/states/mn/districts/house/26a"
    rel: in-district
    area_weight: 0.6655
  - to: "us/states/mn/districts/house/20b"
    rel: in-district
    area_weight: 0.3343
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Winona County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49779 |
| Under 18 | 8769 |
| 18–64 | 31685 |
| 65+ | 9325 |
| Median household income | 70744 |
| Poverty rate | 14.8 |
| Homeownership rate | 69.49 |
| Unemployment rate | 2.29 |
| Median home value | 235400 |
| Gini index | 0.4507 |
| Vacancy rate | 7.33 |
| White | 44707 |
| Black | 958 |
| Asian | 1089 |
| Native | 202 |
| Hispanic/Latino | 1930 |
| Bachelor's or higher | 13651 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 26](/us/states/mn/districts/senate/26.md) — 67% (state senate)
- [MN Senate District 20](/us/states/mn/districts/senate/20.md) — 33% (state senate)
- [MN House District 26A](/us/states/mn/districts/house/26a.md) — 67% (state house)
- [MN House District 20B](/us/states/mn/districts/house/20b.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
