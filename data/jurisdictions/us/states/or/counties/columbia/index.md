---
type: Jurisdiction
title: "Columbia County, OR"
classification: county
fips: "41009"
state: "OR"
demographics:
  population: 53493
  population_under_18: 10867
  population_18_64: 31872
  population_65_plus: 10754
  median_household_income: 87458
  poverty_rate: 8.87
  homeownership_rate: 76.15
  unemployment_rate: 4.11
  median_home_value: 421600
  gini_index: 0.3864
  vacancy_rate: 5.59
  race_white: 45709
  race_black: 332
  race_asian: 423
  race_native: 481
  hispanic: 3603
  bachelors_plus: 9946
districts:
  - to: "us/states/or/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/31"
    rel: in-district
    area_weight: 0.9271
  - to: "us/states/or/districts/house/32"
    rel: in-district
    area_weight: 0.0728
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Columbia County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53493 |
| Under 18 | 10867 |
| 18–64 | 31872 |
| 65+ | 10754 |
| Median household income | 87458 |
| Poverty rate | 8.87 |
| Homeownership rate | 76.15 |
| Unemployment rate | 4.11 |
| Median home value | 421600 |
| Gini index | 0.3864 |
| Vacancy rate | 5.59 |
| White | 45709 |
| Black | 332 |
| Asian | 423 |
| Native | 481 |
| Hispanic/Latino | 3603 |
| Bachelor's or higher | 9946 |

## Districts

- [OR-01](/us/states/or/districts/01.md) — 100% (congressional)
- [OR Senate District 16](/us/states/or/districts/senate/16.md) — 100% (state senate)
- [OR House District 31](/us/states/or/districts/house/31.md) — 93% (state house)
- [OR House District 32](/us/states/or/districts/house/32.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
