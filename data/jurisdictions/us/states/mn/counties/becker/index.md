---
type: Jurisdiction
title: "Becker County, MN"
classification: county
fips: "27005"
state: "MN"
demographics:
  population: 35343
  population_under_18: 8231
  population_18_64: 19061
  population_65_plus: 8051
  median_household_income: 71388
  poverty_rate: 12.9
  homeownership_rate: 77.19
  unemployment_rate: 4.34
  median_home_value: 291000
  gini_index: 0.4797
  vacancy_rate: 27.97
  race_white: 30134
  race_black: 345
  race_asian: 179
  race_native: 1684
  hispanic: 702
  bachelors_plus: 9073
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.6472
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.3528
  - to: "us/states/mn/districts/senate/5"
    rel: in-district
    area_weight: 0.4231
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.3029
  - to: "us/states/mn/districts/senate/4"
    rel: in-district
    area_weight: 0.2739
  - to: "us/states/mn/districts/house/5a"
    rel: in-district
    area_weight: 0.4231
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.3029
  - to: "us/states/mn/districts/house/4b"
    rel: in-district
    area_weight: 0.2739
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Becker County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35343 |
| Under 18 | 8231 |
| 18–64 | 19061 |
| 65+ | 8051 |
| Median household income | 71388 |
| Poverty rate | 12.9 |
| Homeownership rate | 77.19 |
| Unemployment rate | 4.34 |
| Median home value | 291000 |
| Gini index | 0.4797 |
| Vacancy rate | 27.97 |
| White | 30134 |
| Black | 345 |
| Asian | 179 |
| Native | 1684 |
| Hispanic/Latino | 702 |
| Bachelor's or higher | 9073 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 65% (congressional)
- [MN-08](/us/states/mn/districts/08.md) — 35% (congressional)
- [MN Senate District 5](/us/states/mn/districts/senate/5.md) — 42% (state senate)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 30% (state senate)
- [MN Senate District 4](/us/states/mn/districts/senate/4.md) — 27% (state senate)
- [MN House District 5A](/us/states/mn/districts/house/5a.md) — 42% (state house)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 30% (state house)
- [MN House District 4B](/us/states/mn/districts/house/4b.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
