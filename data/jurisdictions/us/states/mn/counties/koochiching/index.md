---
type: Jurisdiction
title: "Koochiching County, MN"
classification: county
fips: "27071"
state: "MN"
demographics:
  population: 11833
  population_under_18: 2068
  population_18_64: 6385
  population_65_plus: 3380
  median_household_income: 66940
  poverty_rate: 10.87
  homeownership_rate: 80.43
  unemployment_rate: 4.82
  median_home_value: 156600
  gini_index: 0.4336
  vacancy_rate: 20.93
  race_white: 10618
  race_black: 35
  race_asian: 81
  race_native: 246
  hispanic: 182
  bachelors_plus: 2482
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/mn/districts/senate/3"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mn/districts/house/3a"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Koochiching County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11833 |
| Under 18 | 2068 |
| 18–64 | 6385 |
| 65+ | 3380 |
| Median household income | 66940 |
| Poverty rate | 10.87 |
| Homeownership rate | 80.43 |
| Unemployment rate | 4.82 |
| Median home value | 156600 |
| Gini index | 0.4336 |
| Vacancy rate | 20.93 |
| White | 10618 |
| Black | 35 |
| Asian | 81 |
| Native | 246 |
| Hispanic/Latino | 182 |
| Bachelor's or higher | 2482 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 3](/us/states/mn/districts/senate/3.md) — 100% (state senate)
- [MN House District 3A](/us/states/mn/districts/house/3a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
