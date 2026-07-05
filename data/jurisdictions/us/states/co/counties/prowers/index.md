---
type: Jurisdiction
title: "Prowers County, CO"
classification: county
fips: "08099"
state: "CO"
demographics:
  population: 11910
  population_under_18: 3107
  population_18_64: 6562
  population_65_plus: 2241
  median_household_income: 53508
  poverty_rate: 18.16
  homeownership_rate: 67.1
  unemployment_rate: 4.14
  median_home_value: 160600
  gini_index: 0.5159
  vacancy_rate: 13.62
  race_white: 7725
  race_black: 124
  race_asian: 36
  race_native: 175
  hispanic: 4829
  bachelors_plus: 2109
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Prowers County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11910 |
| Under 18 | 3107 |
| 18–64 | 6562 |
| 65+ | 2241 |
| Median household income | 53508 |
| Poverty rate | 18.16 |
| Homeownership rate | 67.1 |
| Unemployment rate | 4.14 |
| Median home value | 160600 |
| Gini index | 0.5159 |
| Vacancy rate | 13.62 |
| White | 7725 |
| Black | 124 |
| Asian | 36 |
| Native | 175 |
| Hispanic/Latino | 4829 |
| Bachelor's or higher | 2109 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
