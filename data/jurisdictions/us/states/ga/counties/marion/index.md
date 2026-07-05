---
type: Jurisdiction
title: "Marion County, GA"
classification: county
fips: "13197"
state: "GA"
demographics:
  population: 7509
  population_under_18: 1519
  population_18_64: 4353
  population_65_plus: 1637
  median_household_income: 51667
  poverty_rate: 20.92
  homeownership_rate: 78.86
  unemployment_rate: 4.85
  median_home_value: 154100
  gini_index: 0.4748
  vacancy_rate: 16.31
  race_white: 4377
  race_black: 2048
  race_asian: 175
  race_native: 89
  hispanic: 603
  bachelors_plus: 1362
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Marion County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7509 |
| Under 18 | 1519 |
| 18–64 | 4353 |
| 65+ | 1637 |
| Median household income | 51667 |
| Poverty rate | 20.92 |
| Homeownership rate | 78.86 |
| Unemployment rate | 4.85 |
| Median home value | 154100 |
| Gini index | 0.4748 |
| Vacancy rate | 16.31 |
| White | 4377 |
| Black | 2048 |
| Asian | 175 |
| Native | 89 |
| Hispanic/Latino | 603 |
| Bachelor's or higher | 1362 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 100% (state senate)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
