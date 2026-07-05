---
type: Jurisdiction
title: "Richmond County, GA"
classification: county
fips: "13245"
state: "GA"
demographics:
  population: 206069
  population_under_18: 47209
  population_18_64: 127290
  population_65_plus: 31570
  median_household_income: 55637
  poverty_rate: 20.03
  homeownership_rate: 51.22
  unemployment_rate: 8.53
  median_home_value: 178500
  gini_index: 0.4862
  vacancy_rate: 17.66
  race_white: 67215
  race_black: 115929
  race_asian: 3433
  race_native: 227
  hispanic: 11922
  bachelors_plus: 47053
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9951
  - to: "us/states/ga/districts/senate/22"
    rel: in-district
    area_weight: 0.7014
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.298
  - to: "us/states/ga/districts/house/130"
    rel: in-district
    area_weight: 0.3948
  - to: "us/states/ga/districts/house/132"
    rel: in-district
    area_weight: 0.3204
  - to: "us/states/ga/districts/house/126"
    rel: in-district
    area_weight: 0.1718
  - to: "us/states/ga/districts/house/129"
    rel: in-district
    area_weight: 0.0844
  - to: "us/states/ga/districts/house/127"
    rel: in-district
    area_weight: 0.028
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Richmond County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 206069 |
| Under 18 | 47209 |
| 18–64 | 127290 |
| 65+ | 31570 |
| Median household income | 55637 |
| Poverty rate | 20.03 |
| Homeownership rate | 51.22 |
| Unemployment rate | 8.53 |
| Median home value | 178500 |
| Gini index | 0.4862 |
| Vacancy rate | 17.66 |
| White | 67215 |
| Black | 115929 |
| Asian | 3433 |
| Native | 227 |
| Hispanic/Latino | 11922 |
| Bachelor's or higher | 47053 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 22](/us/states/ga/districts/senate/22.md) — 70% (state senate)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 30% (state senate)
- [GA House District 130](/us/states/ga/districts/house/130.md) — 39% (state house)
- [GA House District 132](/us/states/ga/districts/house/132.md) — 32% (state house)
- [GA House District 126](/us/states/ga/districts/house/126.md) — 17% (state house)
- [GA House District 129](/us/states/ga/districts/house/129.md) — 8% (state house)
- [GA House District 127](/us/states/ga/districts/house/127.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
