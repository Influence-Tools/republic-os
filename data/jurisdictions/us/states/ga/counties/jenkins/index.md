---
type: Jurisdiction
title: "Jenkins County, GA"
classification: county
fips: "13165"
state: "GA"
demographics:
  population: 8711
  population_under_18: 1496
  population_18_64: 5364
  population_65_plus: 1851
  median_household_income: 44389
  poverty_rate: 22.85
  homeownership_rate: 82.25
  unemployment_rate: 3.86
  median_home_value: 92900
  gini_index: 0.4667
  vacancy_rate: 26.69
  race_white: 4786
  race_black: 3234
  race_asian: 0
  race_native: 5
  hispanic: 802
  bachelors_plus: 1056
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/126"
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

# Jenkins County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8711 |
| Under 18 | 1496 |
| 18–64 | 5364 |
| 65+ | 1851 |
| Median household income | 44389 |
| Poverty rate | 22.85 |
| Homeownership rate | 82.25 |
| Unemployment rate | 3.86 |
| Median home value | 92900 |
| Gini index | 0.4667 |
| Vacancy rate | 26.69 |
| White | 4786 |
| Black | 3234 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 802 |
| Bachelor's or higher | 1056 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 126](/us/states/ga/districts/house/126.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
