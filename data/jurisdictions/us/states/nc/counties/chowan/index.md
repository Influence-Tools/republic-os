---
type: Jurisdiction
title: "Chowan County, NC"
classification: county
fips: "37041"
state: "NC"
demographics:
  population: 13836
  population_under_18: 2652
  population_18_64: 7578
  population_65_plus: 3606
  median_household_income: 53864
  poverty_rate: 19.09
  homeownership_rate: 70.52
  unemployment_rate: 4.11
  median_home_value: 235800
  gini_index: 0.469
  vacancy_rate: 14.69
  race_white: 8353
  race_black: 4522
  race_asian: 9
  race_native: 0
  hispanic: 554
  bachelors_plus: 3602
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.7689
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.7568
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.757
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Chowan County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13836 |
| Under 18 | 2652 |
| 18–64 | 7578 |
| 65+ | 3606 |
| Median household income | 53864 |
| Poverty rate | 19.09 |
| Homeownership rate | 70.52 |
| Unemployment rate | 4.11 |
| Median home value | 235800 |
| Gini index | 0.469 |
| Vacancy rate | 14.69 |
| White | 8353 |
| Black | 4522 |
| Asian | 9 |
| Native | 0 |
| Hispanic/Latino | 554 |
| Bachelor's or higher | 3602 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 77% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 76% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 76% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
