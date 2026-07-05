---
type: Jurisdiction
title: "Perquimans County, NC"
classification: county
fips: "37143"
state: "NC"
demographics:
  population: 13244
  population_under_18: 2441
  population_18_64: 6969
  population_65_plus: 3834
  median_household_income: 67917
  poverty_rate: 9.83
  homeownership_rate: 76.54
  unemployment_rate: 3.56
  median_home_value: 231700
  gini_index: 0.3976
  vacancy_rate: 19.42
  race_white: 9332
  race_black: 2820
  race_asian: 55
  race_native: 7
  hispanic: 424
  bachelors_plus: 3063
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.7771
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.7658
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.7657
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Perquimans County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13244 |
| Under 18 | 2441 |
| 18–64 | 6969 |
| 65+ | 3834 |
| Median household income | 67917 |
| Poverty rate | 9.83 |
| Homeownership rate | 76.54 |
| Unemployment rate | 3.56 |
| Median home value | 231700 |
| Gini index | 0.3976 |
| Vacancy rate | 19.42 |
| White | 9332 |
| Black | 2820 |
| Asian | 55 |
| Native | 7 |
| Hispanic/Latino | 424 |
| Bachelor's or higher | 3063 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 78% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 77% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 77% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
