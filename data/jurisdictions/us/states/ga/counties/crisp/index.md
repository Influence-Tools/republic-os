---
type: Jurisdiction
title: "Crisp County, GA"
classification: county
fips: "13081"
state: "GA"
demographics:
  population: 19790
  population_under_18: 4673
  population_18_64: 11204
  population_65_plus: 3913
  median_household_income: 45105
  poverty_rate: 23.34
  homeownership_rate: 55.5
  unemployment_rate: 7.46
  median_home_value: 140200
  gini_index: 0.5022
  vacancy_rate: 20.19
  race_white: 9838
  race_black: 8954
  race_asian: 99
  race_native: 11
  hispanic: 715
  bachelors_plus: 2799
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/148"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Crisp County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19790 |
| Under 18 | 4673 |
| 18–64 | 11204 |
| 65+ | 3913 |
| Median household income | 45105 |
| Poverty rate | 23.34 |
| Homeownership rate | 55.5 |
| Unemployment rate | 7.46 |
| Median home value | 140200 |
| Gini index | 0.5022 |
| Vacancy rate | 20.19 |
| White | 9838 |
| Black | 8954 |
| Asian | 99 |
| Native | 11 |
| Hispanic/Latino | 715 |
| Bachelor's or higher | 2799 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 148](/us/states/ga/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
