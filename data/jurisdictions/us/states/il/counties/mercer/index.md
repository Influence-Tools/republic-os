---
type: Jurisdiction
title: "Mercer County, IL"
classification: county
fips: "17131"
state: "IL"
demographics:
  population: 15495
  population_under_18: 3230
  population_18_64: 8876
  population_65_plus: 3389
  median_household_income: 74182
  poverty_rate: 8.92
  homeownership_rate: 83.76
  unemployment_rate: 3.15
  median_home_value: 146700
  gini_index: 0.4141
  vacancy_rate: 9.88
  race_white: 14589
  race_black: 93
  race_asian: 56
  race_native: 14
  hispanic: 534
  bachelors_plus: 3110
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.6178
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.3821
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.7473
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.2526
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.7473
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.2526
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Mercer County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15495 |
| Under 18 | 3230 |
| 18–64 | 8876 |
| 65+ | 3389 |
| Median household income | 74182 |
| Poverty rate | 8.92 |
| Homeownership rate | 83.76 |
| Unemployment rate | 3.15 |
| Median home value | 146700 |
| Gini index | 0.4141 |
| Vacancy rate | 9.88 |
| White | 14589 |
| Black | 93 |
| Asian | 56 |
| Native | 14 |
| Hispanic/Latino | 534 |
| Bachelor's or higher | 3110 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 62% (congressional)
- [IL-17](/us/states/il/districts/17.md) — 38% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 75% (state senate)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 25% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 75% (state house)
- [IL House District 71](/us/states/il/districts/house/71.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
