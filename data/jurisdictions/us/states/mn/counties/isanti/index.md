---
type: Jurisdiction
title: "Isanti County, MN"
classification: county
fips: "27059"
state: "MN"
demographics:
  population: 42596
  population_under_18: 9901
  population_18_64: 25363
  population_65_plus: 7332
  median_household_income: 87440
  poverty_rate: 7.45
  homeownership_rate: 83.7
  unemployment_rate: 4.11
  median_home_value: 306200
  gini_index: 0.3856
  vacancy_rate: 5.65
  race_white: 39012
  race_black: 372
  race_asian: 822
  race_native: 179
  hispanic: 1102
  bachelors_plus: 7736
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mn/districts/senate/28"
    rel: in-district
    area_weight: 0.6844
  - to: "us/states/mn/districts/senate/27"
    rel: in-district
    area_weight: 0.166
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.0803
  - to: "us/states/mn/districts/senate/31"
    rel: in-district
    area_weight: 0.0693
  - to: "us/states/mn/districts/house/28a"
    rel: in-district
    area_weight: 0.6844
  - to: "us/states/mn/districts/house/27b"
    rel: in-district
    area_weight: 0.166
  - to: "us/states/mn/districts/house/10b"
    rel: in-district
    area_weight: 0.0803
  - to: "us/states/mn/districts/house/31b"
    rel: in-district
    area_weight: 0.0693
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Isanti County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42596 |
| Under 18 | 9901 |
| 18–64 | 25363 |
| 65+ | 7332 |
| Median household income | 87440 |
| Poverty rate | 7.45 |
| Homeownership rate | 83.7 |
| Unemployment rate | 4.11 |
| Median home value | 306200 |
| Gini index | 0.3856 |
| Vacancy rate | 5.65 |
| White | 39012 |
| Black | 372 |
| Asian | 822 |
| Native | 179 |
| Hispanic/Latino | 1102 |
| Bachelor's or higher | 7736 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 28](/us/states/mn/districts/senate/28.md) — 68% (state senate)
- [MN Senate District 27](/us/states/mn/districts/senate/27.md) — 17% (state senate)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 8% (state senate)
- [MN Senate District 31](/us/states/mn/districts/senate/31.md) — 7% (state senate)
- [MN House District 28A](/us/states/mn/districts/house/28a.md) — 68% (state house)
- [MN House District 27B](/us/states/mn/districts/house/27b.md) — 17% (state house)
- [MN House District 10B](/us/states/mn/districts/house/10b.md) — 8% (state house)
- [MN House District 31B](/us/states/mn/districts/house/31b.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
