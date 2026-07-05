---
type: Jurisdiction
title: "Isabella County, MI"
classification: county
fips: "26073"
state: "MI"
demographics:
  population: 64565
  population_under_18: 11471
  population_18_64: 44072
  population_65_plus: 9022
  median_household_income: 55237
  poverty_rate: 21.9
  homeownership_rate: 61.84
  unemployment_rate: 6.39
  median_home_value: 170400
  gini_index: 0.4612
  vacancy_rate: 13.07
  race_white: 54561
  race_black: 1616
  race_asian: 1091
  race_native: 1934
  hispanic: 3281
  bachelors_plus: 16367
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/92"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Isabella County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64565 |
| Under 18 | 11471 |
| 18–64 | 44072 |
| 65+ | 9022 |
| Median household income | 55237 |
| Poverty rate | 21.9 |
| Homeownership rate | 61.84 |
| Unemployment rate | 6.39 |
| Median home value | 170400 |
| Gini index | 0.4612 |
| Vacancy rate | 13.07 |
| White | 54561 |
| Black | 1616 |
| Asian | 1091 |
| Native | 1934 |
| Hispanic/Latino | 3281 |
| Bachelor's or higher | 16367 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 100% (state senate)
- [MI House District 92](/us/states/mi/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
