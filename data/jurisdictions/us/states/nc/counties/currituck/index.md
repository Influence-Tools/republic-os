---
type: Jurisdiction
title: "Currituck County, NC"
classification: county
fips: "37053"
state: "NC"
demographics:
  population: 30601
  population_under_18: 6704
  population_18_64: 18408
  population_65_plus: 5489
  median_household_income: 93511
  poverty_rate: 7.5
  homeownership_rate: 87.27
  unemployment_rate: 2.98
  median_home_value: 378800
  gini_index: 0.4196
  vacancy_rate: 30.65
  race_white: 25917
  race_black: 1541
  race_asian: 280
  race_native: 54
  hispanic: 1587
  bachelors_plus: 8959
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.5641
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.5473
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.5472
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Currituck County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30601 |
| Under 18 | 6704 |
| 18–64 | 18408 |
| 65+ | 5489 |
| Median household income | 93511 |
| Poverty rate | 7.5 |
| Homeownership rate | 87.27 |
| Unemployment rate | 2.98 |
| Median home value | 378800 |
| Gini index | 0.4196 |
| Vacancy rate | 30.65 |
| White | 25917 |
| Black | 1541 |
| Asian | 280 |
| Native | 54 |
| Hispanic/Latino | 1587 |
| Bachelor's or higher | 8959 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 56% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 55% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 55% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
