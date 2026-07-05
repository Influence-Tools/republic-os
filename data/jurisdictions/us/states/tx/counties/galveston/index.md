---
type: Jurisdiction
title: "Galveston County, TX"
classification: county
fips: "48167"
state: "TX"
demographics:
  population: 358990
  population_under_18: 84684
  population_18_64: 217702
  population_65_plus: 56604
  median_household_income: 86105
  poverty_rate: 11.71
  homeownership_rate: 67.64
  unemployment_rate: 5.7
  median_home_value: 314600
  gini_index: 0.4597
  vacancy_rate: 13.1
  race_white: 216591
  race_black: 44109
  race_asian: 12211
  race_native: 1950
  hispanic: 94669
  bachelors_plus: 113517
districts:
  - to: "us/states/tx/districts/14"
    rel: in-district
    area_weight: 0.4878
  - to: "us/states/tx/districts/senate/11"
    rel: in-district
    area_weight: 0.4037
  - to: "us/states/tx/districts/senate/4"
    rel: in-district
    area_weight: 0.0673
  - to: "us/states/tx/districts/house/24"
    rel: in-district
    area_weight: 0.2398
  - to: "us/states/tx/districts/house/23"
    rel: in-district
    area_weight: 0.2309
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Galveston County, TX

County jurisdiction — 8 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 358990 |
| Under 18 | 84684 |
| 18–64 | 217702 |
| 65+ | 56604 |
| Median household income | 86105 |
| Poverty rate | 11.71 |
| Homeownership rate | 67.64 |
| Unemployment rate | 5.7 |
| Median home value | 314600 |
| Gini index | 0.4597 |
| Vacancy rate | 13.1 |
| White | 216591 |
| Black | 44109 |
| Asian | 12211 |
| Native | 1950 |
| Hispanic/Latino | 94669 |
| Bachelor's or higher | 113517 |

## Districts

- [TX-14](/us/states/tx/districts/14.md) — 49% (congressional)
- [TX Senate District 11](/us/states/tx/districts/senate/11.md) — 40% (state senate)
- [TX Senate District 4](/us/states/tx/districts/senate/4.md) — 7% (state senate)
- [TX House District 24](/us/states/tx/districts/house/24.md) — 24% (state house)
- [TX House District 23](/us/states/tx/districts/house/23.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
