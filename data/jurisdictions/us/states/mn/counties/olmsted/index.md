---
type: Jurisdiction
title: "Olmsted County, MN"
classification: county
fips: "27109"
state: "MN"
demographics:
  population: 164498
  population_under_18: 39364
  population_18_64: 97737
  population_65_plus: 27397
  median_household_income: 95406
  poverty_rate: 7.5
  homeownership_rate: 70.57
  unemployment_rate: 3.56
  median_home_value: 331700
  gini_index: 0.4639
  vacancy_rate: 5.95
  race_white: 127008
  race_black: 12419
  race_asian: 10487
  race_native: 289
  hispanic: 9814
  bachelors_plus: 79324
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/20"
    rel: in-district
    area_weight: 0.5366
  - to: "us/states/mn/districts/senate/24"
    rel: in-district
    area_weight: 0.3035
  - to: "us/states/mn/districts/senate/25"
    rel: in-district
    area_weight: 0.1598
  - to: "us/states/mn/districts/house/20b"
    rel: in-district
    area_weight: 0.5366
  - to: "us/states/mn/districts/house/24a"
    rel: in-district
    area_weight: 0.2574
  - to: "us/states/mn/districts/house/25a"
    rel: in-district
    area_weight: 0.1416
  - to: "us/states/mn/districts/house/24b"
    rel: in-district
    area_weight: 0.0461
  - to: "us/states/mn/districts/house/25b"
    rel: in-district
    area_weight: 0.0182
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Olmsted County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 164498 |
| Under 18 | 39364 |
| 18–64 | 97737 |
| 65+ | 27397 |
| Median household income | 95406 |
| Poverty rate | 7.5 |
| Homeownership rate | 70.57 |
| Unemployment rate | 3.56 |
| Median home value | 331700 |
| Gini index | 0.4639 |
| Vacancy rate | 5.95 |
| White | 127008 |
| Black | 12419 |
| Asian | 10487 |
| Native | 289 |
| Hispanic/Latino | 9814 |
| Bachelor's or higher | 79324 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 20](/us/states/mn/districts/senate/20.md) — 54% (state senate)
- [MN Senate District 24](/us/states/mn/districts/senate/24.md) — 30% (state senate)
- [MN Senate District 25](/us/states/mn/districts/senate/25.md) — 16% (state senate)
- [MN House District 20B](/us/states/mn/districts/house/20b.md) — 54% (state house)
- [MN House District 24A](/us/states/mn/districts/house/24a.md) — 26% (state house)
- [MN House District 25A](/us/states/mn/districts/house/25a.md) — 14% (state house)
- [MN House District 24B](/us/states/mn/districts/house/24b.md) — 5% (state house)
- [MN House District 25B](/us/states/mn/districts/house/25b.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
