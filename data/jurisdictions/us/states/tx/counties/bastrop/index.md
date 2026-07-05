---
type: Jurisdiction
title: "Bastrop County, TX"
classification: county
fips: "48021"
state: "TX"
demographics:
  population: 106582
  population_under_18: 27681
  population_18_64: 62499
  population_65_plus: 16402
  median_household_income: 86226
  poverty_rate: 10.18
  homeownership_rate: 76.45
  unemployment_rate: 4.28
  median_home_value: 314800
  gini_index: 0.4132
  vacancy_rate: 7.15
  race_white: 57769
  race_black: 6155
  race_asian: 856
  race_native: 1279
  hispanic: 48002
  bachelors_plus: 23649
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.5146
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.4853
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/17"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bastrop County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106582 |
| Under 18 | 27681 |
| 18–64 | 62499 |
| 65+ | 16402 |
| Median household income | 86226 |
| Poverty rate | 10.18 |
| Homeownership rate | 76.45 |
| Unemployment rate | 4.28 |
| Median home value | 314800 |
| Gini index | 0.4132 |
| Vacancy rate | 7.15 |
| White | 57769 |
| Black | 6155 |
| Asian | 856 |
| Native | 1279 |
| Hispanic/Latino | 48002 |
| Bachelor's or higher | 23649 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 51% (congressional)
- [TX-27](/us/states/tx/districts/27.md) — 49% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 17](/us/states/tx/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
