---
type: Jurisdiction
title: "Clatsop County, OR"
classification: county
fips: "41007"
state: "OR"
demographics:
  population: 41363
  population_under_18: 7389
  population_18_64: 23603
  population_65_plus: 10371
  median_household_income: 71822
  poverty_rate: 12.32
  homeownership_rate: 63.25
  unemployment_rate: 4.71
  median_home_value: 468300
  gini_index: 0.4636
  vacancy_rate: 23.13
  race_white: 34355
  race_black: 421
  race_asian: 526
  race_native: 306
  hispanic: 4156
  bachelors_plus: 12423
districts:
  - to: "us/states/or/districts/01"
    rel: in-district
    area_weight: 0.7863
  - to: "us/states/or/districts/senate/16"
    rel: in-district
    area_weight: 0.787
  - to: "us/states/or/districts/house/32"
    rel: in-district
    area_weight: 0.7868
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Clatsop County, OR

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41363 |
| Under 18 | 7389 |
| 18–64 | 23603 |
| 65+ | 10371 |
| Median household income | 71822 |
| Poverty rate | 12.32 |
| Homeownership rate | 63.25 |
| Unemployment rate | 4.71 |
| Median home value | 468300 |
| Gini index | 0.4636 |
| Vacancy rate | 23.13 |
| White | 34355 |
| Black | 421 |
| Asian | 526 |
| Native | 306 |
| Hispanic/Latino | 4156 |
| Bachelor's or higher | 12423 |

## Districts

- [OR-01](/us/states/or/districts/01.md) — 79% (congressional)
- [OR Senate District 16](/us/states/or/districts/senate/16.md) — 79% (state senate)
- [OR House District 32](/us/states/or/districts/house/32.md) — 79% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
