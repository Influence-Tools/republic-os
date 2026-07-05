---
type: Jurisdiction
title: "Redwood County, MN"
classification: county
fips: "27127"
state: "MN"
demographics:
  population: 15350
  population_under_18: 3784
  population_18_64: 8145
  population_65_plus: 3421
  median_household_income: 67866
  poverty_rate: 13.27
  homeownership_rate: 78.39
  unemployment_rate: 2.56
  median_home_value: 158200
  gini_index: 0.4411
  vacancy_rate: 11.49
  race_white: 13284
  race_black: 98
  race_asian: 407
  race_native: 593
  hispanic: 641
  bachelors_plus: 2919
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/15b"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Redwood County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15350 |
| Under 18 | 3784 |
| 18–64 | 8145 |
| 65+ | 3421 |
| Median household income | 67866 |
| Poverty rate | 13.27 |
| Homeownership rate | 78.39 |
| Unemployment rate | 2.56 |
| Median home value | 158200 |
| Gini index | 0.4411 |
| Vacancy rate | 11.49 |
| White | 13284 |
| Black | 98 |
| Asian | 407 |
| Native | 593 |
| Hispanic/Latino | 641 |
| Bachelor's or higher | 2919 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 100% (state senate)
- [MN House District 15B](/us/states/mn/districts/house/15b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
