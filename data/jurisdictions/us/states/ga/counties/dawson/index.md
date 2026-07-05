---
type: Jurisdiction
title: "Dawson County, GA"
classification: county
fips: "13085"
state: "GA"
demographics:
  population: 30242
  population_under_18: 6177
  population_18_64: 18165
  population_65_plus: 5900
  median_household_income: 92991
  poverty_rate: 8.54
  homeownership_rate: 78.66
  unemployment_rate: 3.52
  median_home_value: 406700
  gini_index: 0.4141
  vacancy_rate: 10.92
  race_white: 26074
  race_black: 588
  race_asian: 382
  race_native: 9
  hispanic: 2208
  bachelors_plus: 10818
districts:
  - to: "us/states/ga/districts/07"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/9"
    rel: in-district
    area_weight: 0.7233
  - to: "us/states/ga/districts/house/7"
    rel: in-district
    area_weight: 0.2765
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Dawson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30242 |
| Under 18 | 6177 |
| 18–64 | 18165 |
| 65+ | 5900 |
| Median household income | 92991 |
| Poverty rate | 8.54 |
| Homeownership rate | 78.66 |
| Unemployment rate | 3.52 |
| Median home value | 406700 |
| Gini index | 0.4141 |
| Vacancy rate | 10.92 |
| White | 26074 |
| Black | 588 |
| Asian | 382 |
| Native | 9 |
| Hispanic/Latino | 2208 |
| Bachelor's or higher | 10818 |

## Districts

- [GA-07](/us/states/ga/districts/07.md) — 100% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 9](/us/states/ga/districts/house/9.md) — 72% (state house)
- [GA House District 7](/us/states/ga/districts/house/7.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
