---
type: Jurisdiction
title: "Dutchess County, NY"
classification: county
fips: "36027"
state: "NY"
demographics:
  population: 298220
  population_under_18: 54816
  population_18_64: 186352
  population_65_plus: 57052
  median_household_income: 99478
  poverty_rate: 8.43
  homeownership_rate: 69.19
  unemployment_rate: 5.24
  median_home_value: 400600
  gini_index: 0.4659
  vacancy_rate: 5.6
  race_white: 205306
  race_black: 29357
  race_asian: 10300
  race_native: 1824
  hispanic: 46023
  bachelors_plus: 129718
districts:
  - to: "us/states/ny/districts/18"
    rel: in-district
    area_weight: 0.8628
  - to: "us/states/ny/districts/17"
    rel: in-district
    area_weight: 0.1369
  - to: "us/states/ny/districts/senate/41"
    rel: in-district
    area_weight: 0.6214
  - to: "us/states/ny/districts/senate/39"
    rel: in-district
    area_weight: 0.3785
  - to: "us/states/ny/districts/house/105"
    rel: in-district
    area_weight: 0.4471
  - to: "us/states/ny/districts/house/106"
    rel: in-district
    area_weight: 0.441
  - to: "us/states/ny/districts/house/103"
    rel: in-district
    area_weight: 0.097
  - to: "us/states/ny/districts/house/104"
    rel: in-district
    area_weight: 0.0148
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Dutchess County, NY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 298220 |
| Under 18 | 54816 |
| 18–64 | 186352 |
| 65+ | 57052 |
| Median household income | 99478 |
| Poverty rate | 8.43 |
| Homeownership rate | 69.19 |
| Unemployment rate | 5.24 |
| Median home value | 400600 |
| Gini index | 0.4659 |
| Vacancy rate | 5.6 |
| White | 205306 |
| Black | 29357 |
| Asian | 10300 |
| Native | 1824 |
| Hispanic/Latino | 46023 |
| Bachelor's or higher | 129718 |

## Districts

- [NY-18](/us/states/ny/districts/18.md) — 86% (congressional)
- [NY-17](/us/states/ny/districts/17.md) — 14% (congressional)
- [NY Senate District 41](/us/states/ny/districts/senate/41.md) — 62% (state senate)
- [NY Senate District 39](/us/states/ny/districts/senate/39.md) — 38% (state senate)
- [NY House District 105](/us/states/ny/districts/house/105.md) — 45% (state house)
- [NY House District 106](/us/states/ny/districts/house/106.md) — 44% (state house)
- [NY House District 103](/us/states/ny/districts/house/103.md) — 10% (state house)
- [NY House District 104](/us/states/ny/districts/house/104.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
