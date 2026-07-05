---
type: Jurisdiction
title: "Oktibbeha County, MS"
classification: county
fips: "28105"
state: "MS"
demographics:
  population: 51771
  population_under_18: 9058
  population_18_64: 36390
  population_65_plus: 6323
  median_household_income: 46695
  poverty_rate: 25.53
  homeownership_rate: 47.98
  unemployment_rate: 5.78
  median_home_value: 237700
  gini_index: 0.5303
  vacancy_rate: 14.75
  race_white: 28654
  race_black: 18365
  race_asian: 1652
  race_native: 101
  hispanic: 1253
  bachelors_plus: 18458
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.7484
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.2516
  - to: "us/states/ms/districts/senate/15"
    rel: in-district
    area_weight: 0.5124
  - to: "us/states/ms/districts/senate/16"
    rel: in-district
    area_weight: 0.4048
  - to: "us/states/ms/districts/senate/17"
    rel: in-district
    area_weight: 0.0828
  - to: "us/states/ms/districts/house/38"
    rel: in-district
    area_weight: 0.4949
  - to: "us/states/ms/districts/house/35"
    rel: in-district
    area_weight: 0.2453
  - to: "us/states/ms/districts/house/43"
    rel: in-district
    area_weight: 0.1713
  - to: "us/states/ms/districts/house/36"
    rel: in-district
    area_weight: 0.0872
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Oktibbeha County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51771 |
| Under 18 | 9058 |
| 18–64 | 36390 |
| 65+ | 6323 |
| Median household income | 46695 |
| Poverty rate | 25.53 |
| Homeownership rate | 47.98 |
| Unemployment rate | 5.78 |
| Median home value | 237700 |
| Gini index | 0.5303 |
| Vacancy rate | 14.75 |
| White | 28654 |
| Black | 18365 |
| Asian | 1652 |
| Native | 101 |
| Hispanic/Latino | 1253 |
| Bachelor's or higher | 18458 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 75% (congressional)
- [MS-01](/us/states/ms/districts/01.md) — 25% (congressional)
- [MS Senate District 15](/us/states/ms/districts/senate/15.md) — 51% (state senate)
- [MS Senate District 16](/us/states/ms/districts/senate/16.md) — 40% (state senate)
- [MS Senate District 17](/us/states/ms/districts/senate/17.md) — 8% (state senate)
- [MS House District 38](/us/states/ms/districts/house/38.md) — 49% (state house)
- [MS House District 35](/us/states/ms/districts/house/35.md) — 25% (state house)
- [MS House District 43](/us/states/ms/districts/house/43.md) — 17% (state house)
- [MS House District 36](/us/states/ms/districts/house/36.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
