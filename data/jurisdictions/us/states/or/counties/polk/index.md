---
type: Jurisdiction
title: "Polk County, OR"
classification: county
fips: "41053"
state: "OR"
demographics:
  population: 89662
  population_under_18: 19385
  population_18_64: 53215
  population_65_plus: 17062
  median_household_income: 85118
  poverty_rate: 12.66
  homeownership_rate: 64.7
  unemployment_rate: 5.65
  median_home_value: 454700
  gini_index: 0.441
  vacancy_rate: 5.39
  race_white: 69670
  race_black: 791
  race_asian: 1703
  race_native: 1460
  hispanic: 13990
  bachelors_plus: 25926
districts:
  - to: "us/states/or/districts/06"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/or/districts/senate/12"
    rel: in-district
    area_weight: 0.9649
  - to: "us/states/or/districts/senate/10"
    rel: in-district
    area_weight: 0.0348
  - to: "us/states/or/districts/house/23"
    rel: in-district
    area_weight: 0.8233
  - to: "us/states/or/districts/house/24"
    rel: in-district
    area_weight: 0.1416
  - to: "us/states/or/districts/house/20"
    rel: in-district
    area_weight: 0.0348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Polk County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 89662 |
| Under 18 | 19385 |
| 18–64 | 53215 |
| 65+ | 17062 |
| Median household income | 85118 |
| Poverty rate | 12.66 |
| Homeownership rate | 64.7 |
| Unemployment rate | 5.65 |
| Median home value | 454700 |
| Gini index | 0.441 |
| Vacancy rate | 5.39 |
| White | 69670 |
| Black | 791 |
| Asian | 1703 |
| Native | 1460 |
| Hispanic/Latino | 13990 |
| Bachelor's or higher | 25926 |

## Districts

- [OR-06](/us/states/or/districts/06.md) — 100% (congressional)
- [OR Senate District 12](/us/states/or/districts/senate/12.md) — 96% (state senate)
- [OR Senate District 10](/us/states/or/districts/senate/10.md) — 3% (state senate)
- [OR House District 23](/us/states/or/districts/house/23.md) — 82% (state house)
- [OR House District 24](/us/states/or/districts/house/24.md) — 14% (state house)
- [OR House District 20](/us/states/or/districts/house/20.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
