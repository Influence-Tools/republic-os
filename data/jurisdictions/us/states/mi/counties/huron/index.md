---
type: Jurisdiction
title: "Huron County, MI"
classification: county
fips: "26063"
state: "MI"
demographics:
  population: 31113
  population_under_18: 5906
  population_18_64: 16742
  population_65_plus: 8465
  median_household_income: 58870
  poverty_rate: 12.62
  homeownership_rate: 81.82
  unemployment_rate: 4.14
  median_home_value: 154300
  gini_index: 0.4426
  vacancy_rate: 30.46
  race_white: 29230
  race_black: 108
  race_asian: 180
  race_native: 70
  hispanic: 886
  bachelors_plus: 5677
districts:
  - to: "us/states/mi/districts/09"
    rel: in-district
    area_weight: 0.3923
  - to: "us/states/mi/districts/senate/25"
    rel: in-district
    area_weight: 0.391
  - to: "us/states/mi/districts/house/98"
    rel: in-district
    area_weight: 0.391
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Huron County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31113 |
| Under 18 | 5906 |
| 18–64 | 16742 |
| 65+ | 8465 |
| Median household income | 58870 |
| Poverty rate | 12.62 |
| Homeownership rate | 81.82 |
| Unemployment rate | 4.14 |
| Median home value | 154300 |
| Gini index | 0.4426 |
| Vacancy rate | 30.46 |
| White | 29230 |
| Black | 108 |
| Asian | 180 |
| Native | 70 |
| Hispanic/Latino | 886 |
| Bachelor's or higher | 5677 |

## Districts

- [MI-09](/us/states/mi/districts/09.md) — 39% (congressional)
- [MI Senate District 25](/us/states/mi/districts/senate/25.md) — 39% (state senate)
- [MI House District 98](/us/states/mi/districts/house/98.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
