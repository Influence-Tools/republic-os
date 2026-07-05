---
type: Jurisdiction
title: "Allegan County, MI"
classification: county
fips: "26005"
state: "MI"
demographics:
  population: 121456
  population_under_18: 28212
  population_18_64: 70866
  population_65_plus: 22378
  median_household_income: 83283
  poverty_rate: 8.37
  homeownership_rate: 87.37
  unemployment_rate: 2.96
  median_home_value: 267100
  gini_index: 0.4151
  vacancy_rate: 13.52
  race_white: 105919
  race_black: 1483
  race_asian: 838
  race_native: 539
  hispanic: 9856
  bachelors_plus: 30453
districts:
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.4596
  - to: "us/states/mi/districts/senate/20"
    rel: in-district
    area_weight: 0.29
  - to: "us/states/mi/districts/senate/18"
    rel: in-district
    area_weight: 0.1375
  - to: "us/states/mi/districts/senate/31"
    rel: in-district
    area_weight: 0.0318
  - to: "us/states/mi/districts/house/43"
    rel: in-district
    area_weight: 0.2714
  - to: "us/states/mi/districts/house/39"
    rel: in-district
    area_weight: 0.0713
  - to: "us/states/mi/districts/house/38"
    rel: in-district
    area_weight: 0.054
  - to: "us/states/mi/districts/house/42"
    rel: in-district
    area_weight: 0.0269
  - to: "us/states/mi/districts/house/79"
    rel: in-district
    area_weight: 0.0195
  - to: "us/states/mi/districts/house/86"
    rel: in-district
    area_weight: 0.0163
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Allegan County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 121456 |
| Under 18 | 28212 |
| 18–64 | 70866 |
| 65+ | 22378 |
| Median household income | 83283 |
| Poverty rate | 8.37 |
| Homeownership rate | 87.37 |
| Unemployment rate | 2.96 |
| Median home value | 267100 |
| Gini index | 0.4151 |
| Vacancy rate | 13.52 |
| White | 105919 |
| Black | 1483 |
| Asian | 838 |
| Native | 539 |
| Hispanic/Latino | 9856 |
| Bachelor's or higher | 30453 |

## Districts

- [MI-04](/us/states/mi/districts/04.md) — 46% (congressional)
- [MI Senate District 20](/us/states/mi/districts/senate/20.md) — 29% (state senate)
- [MI Senate District 18](/us/states/mi/districts/senate/18.md) — 14% (state senate)
- [MI Senate District 31](/us/states/mi/districts/senate/31.md) — 3% (state senate)
- [MI House District 43](/us/states/mi/districts/house/43.md) — 27% (state house)
- [MI House District 39](/us/states/mi/districts/house/39.md) — 7% (state house)
- [MI House District 38](/us/states/mi/districts/house/38.md) — 5% (state house)
- [MI House District 42](/us/states/mi/districts/house/42.md) — 3% (state house)
- [MI House District 79](/us/states/mi/districts/house/79.md) — 2% (state house)
- [MI House District 86](/us/states/mi/districts/house/86.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
