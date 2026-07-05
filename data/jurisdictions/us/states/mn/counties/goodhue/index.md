---
type: Jurisdiction
title: "Goodhue County, MN"
classification: county
fips: "27049"
state: "MN"
demographics:
  population: 47943
  population_under_18: 10514
  population_18_64: 27557
  population_65_plus: 9872
  median_household_income: 84171
  poverty_rate: 9.28
  homeownership_rate: 78.82
  unemployment_rate: 3.57
  median_home_value: 285100
  gini_index: 0.4345
  vacancy_rate: 6.8
  race_white: 42969
  race_black: 752
  race_asian: 329
  race_native: 451
  hispanic: 1964
  bachelors_plus: 12427
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/mn/districts/senate/20"
    rel: in-district
    area_weight: 0.7321
  - to: "us/states/mn/districts/senate/19"
    rel: in-district
    area_weight: 0.1913
  - to: "us/states/mn/districts/senate/58"
    rel: in-district
    area_weight: 0.0765
  - to: "us/states/mn/districts/house/20a"
    rel: in-district
    area_weight: 0.5505
  - to: "us/states/mn/districts/house/19a"
    rel: in-district
    area_weight: 0.1913
  - to: "us/states/mn/districts/house/20b"
    rel: in-district
    area_weight: 0.1816
  - to: "us/states/mn/districts/house/58b"
    rel: in-district
    area_weight: 0.0765
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Goodhue County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47943 |
| Under 18 | 10514 |
| 18–64 | 27557 |
| 65+ | 9872 |
| Median household income | 84171 |
| Poverty rate | 9.28 |
| Homeownership rate | 78.82 |
| Unemployment rate | 3.57 |
| Median home value | 285100 |
| Gini index | 0.4345 |
| Vacancy rate | 6.8 |
| White | 42969 |
| Black | 752 |
| Asian | 329 |
| Native | 451 |
| Hispanic/Latino | 1964 |
| Bachelor's or higher | 12427 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 20](/us/states/mn/districts/senate/20.md) — 73% (state senate)
- [MN Senate District 19](/us/states/mn/districts/senate/19.md) — 19% (state senate)
- [MN Senate District 58](/us/states/mn/districts/senate/58.md) — 8% (state senate)
- [MN House District 20A](/us/states/mn/districts/house/20a.md) — 55% (state house)
- [MN House District 19A](/us/states/mn/districts/house/19a.md) — 19% (state house)
- [MN House District 20B](/us/states/mn/districts/house/20b.md) — 18% (state house)
- [MN House District 58B](/us/states/mn/districts/house/58b.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
