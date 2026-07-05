---
type: Jurisdiction
title: "Stearns County, MN"
classification: county
fips: "27145"
state: "MN"
demographics:
  population: 160865
  population_under_18: 38011
  population_18_64: 96983
  population_65_plus: 25871
  median_household_income: 77066
  poverty_rate: 12.89
  homeownership_rate: 67.85
  unemployment_rate: 4.11
  median_home_value: 273400
  gini_index: 0.4376
  vacancy_rate: 7.84
  race_white: 131456
  race_black: 14649
  race_asian: 3136
  race_native: 188
  hispanic: 7700
  bachelors_plus: 38462
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.8107
  - to: "us/states/mn/districts/06"
    rel: in-district
    area_weight: 0.1893
  - to: "us/states/mn/districts/senate/13"
    rel: in-district
    area_weight: 0.5135
  - to: "us/states/mn/districts/senate/12"
    rel: in-district
    area_weight: 0.43
  - to: "us/states/mn/districts/senate/14"
    rel: in-district
    area_weight: 0.0563
  - to: "us/states/mn/districts/house/13a"
    rel: in-district
    area_weight: 0.4053
  - to: "us/states/mn/districts/house/12a"
    rel: in-district
    area_weight: 0.313
  - to: "us/states/mn/districts/house/12b"
    rel: in-district
    area_weight: 0.117
  - to: "us/states/mn/districts/house/13b"
    rel: in-district
    area_weight: 0.1082
  - to: "us/states/mn/districts/house/14a"
    rel: in-district
    area_weight: 0.0491
  - to: "us/states/mn/districts/house/14b"
    rel: in-district
    area_weight: 0.0072
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Stearns County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160865 |
| Under 18 | 38011 |
| 18–64 | 96983 |
| 65+ | 25871 |
| Median household income | 77066 |
| Poverty rate | 12.89 |
| Homeownership rate | 67.85 |
| Unemployment rate | 4.11 |
| Median home value | 273400 |
| Gini index | 0.4376 |
| Vacancy rate | 7.84 |
| White | 131456 |
| Black | 14649 |
| Asian | 3136 |
| Native | 188 |
| Hispanic/Latino | 7700 |
| Bachelor's or higher | 38462 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 81% (congressional)
- [MN-06](/us/states/mn/districts/06.md) — 19% (congressional)
- [MN Senate District 13](/us/states/mn/districts/senate/13.md) — 51% (state senate)
- [MN Senate District 12](/us/states/mn/districts/senate/12.md) — 43% (state senate)
- [MN Senate District 14](/us/states/mn/districts/senate/14.md) — 6% (state senate)
- [MN House District 13A](/us/states/mn/districts/house/13a.md) — 41% (state house)
- [MN House District 12A](/us/states/mn/districts/house/12a.md) — 31% (state house)
- [MN House District 12B](/us/states/mn/districts/house/12b.md) — 12% (state house)
- [MN House District 13B](/us/states/mn/districts/house/13b.md) — 11% (state house)
- [MN House District 14A](/us/states/mn/districts/house/14a.md) — 5% (state house)
- [MN House District 14B](/us/states/mn/districts/house/14b.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
