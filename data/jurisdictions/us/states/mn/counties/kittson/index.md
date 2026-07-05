---
type: Jurisdiction
title: "Kittson County, MN"
classification: county
fips: "27069"
state: "MN"
demographics:
  population: 4084
  population_under_18: 881
  population_18_64: 2131
  population_65_plus: 1072
  median_household_income: 76100
  poverty_rate: 9.14
  homeownership_rate: 82.86
  unemployment_rate: 5.04
  median_home_value: 134800
  gini_index: 0.4147
  vacancy_rate: 20.38
  race_white: 3807
  race_black: 9
  race_asian: 15
  race_native: 11
  hispanic: 105
  bachelors_plus: 1016
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mn/districts/house/1a"
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

# Kittson County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4084 |
| Under 18 | 881 |
| 18–64 | 2131 |
| 65+ | 1072 |
| Median household income | 76100 |
| Poverty rate | 9.14 |
| Homeownership rate | 82.86 |
| Unemployment rate | 5.04 |
| Median home value | 134800 |
| Gini index | 0.4147 |
| Vacancy rate | 20.38 |
| White | 3807 |
| Black | 9 |
| Asian | 15 |
| Native | 11 |
| Hispanic/Latino | 105 |
| Bachelor's or higher | 1016 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1A](/us/states/mn/districts/house/1a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
