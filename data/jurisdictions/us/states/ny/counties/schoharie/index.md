---
type: Jurisdiction
title: "Schoharie County, NY"
classification: county
fips: "36095"
state: "NY"
demographics:
  population: 30049
  population_under_18: 5182
  population_18_64: 17686
  population_65_plus: 7181
  median_household_income: 70133
  poverty_rate: 11.73
  homeownership_rate: 76.39
  unemployment_rate: 4.99
  median_home_value: 192500
  gini_index: 0.4436
  vacancy_rate: 22.35
  race_white: 26923
  race_black: 418
  race_asian: 268
  race_native: 35
  hispanic: 1209
  bachelors_plus: 8387
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/102"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Schoharie County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30049 |
| Under 18 | 5182 |
| 18–64 | 17686 |
| 65+ | 7181 |
| Median household income | 70133 |
| Poverty rate | 11.73 |
| Homeownership rate | 76.39 |
| Unemployment rate | 4.99 |
| Median home value | 192500 |
| Gini index | 0.4436 |
| Vacancy rate | 22.35 |
| White | 26923 |
| Black | 418 |
| Asian | 268 |
| Native | 35 |
| Hispanic/Latino | 1209 |
| Bachelor's or higher | 8387 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 100% (state senate)
- [NY House District 102](/us/states/ny/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
