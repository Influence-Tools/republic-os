---
type: Jurisdiction
title: "Putnam County, NY"
classification: county
fips: "36079"
state: "NY"
demographics:
  population: 98107
  population_under_18: 19033
  population_18_64: 60164
  population_65_plus: 18910
  median_household_income: 126257
  poverty_rate: 7.11
  homeownership_rate: 83.78
  unemployment_rate: 4.43
  median_home_value: 471300
  gini_index: 0.4254
  vacancy_rate: 7.56
  race_white: 73359
  race_black: 2960
  race_asian: 2263
  race_native: 181
  hispanic: 19656
  bachelors_plus: 47081
districts:
  - to: "us/states/ny/districts/17"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ny/districts/senate/40"
    rel: in-district
    area_weight: 0.6171
  - to: "us/states/ny/districts/senate/39"
    rel: in-district
    area_weight: 0.3828
  - to: "us/states/ny/districts/house/94"
    rel: in-district
    area_weight: 0.7905
  - to: "us/states/ny/districts/house/95"
    rel: in-district
    area_weight: 0.2094
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Putnam County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98107 |
| Under 18 | 19033 |
| 18–64 | 60164 |
| 65+ | 18910 |
| Median household income | 126257 |
| Poverty rate | 7.11 |
| Homeownership rate | 83.78 |
| Unemployment rate | 4.43 |
| Median home value | 471300 |
| Gini index | 0.4254 |
| Vacancy rate | 7.56 |
| White | 73359 |
| Black | 2960 |
| Asian | 2263 |
| Native | 181 |
| Hispanic/Latino | 19656 |
| Bachelor's or higher | 47081 |

## Districts

- [NY-17](/us/states/ny/districts/17.md) — 100% (congressional)
- [NY Senate District 40](/us/states/ny/districts/senate/40.md) — 62% (state senate)
- [NY Senate District 39](/us/states/ny/districts/senate/39.md) — 38% (state senate)
- [NY House District 94](/us/states/ny/districts/house/94.md) — 79% (state house)
- [NY House District 95](/us/states/ny/districts/house/95.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
