---
type: Jurisdiction
title: "Glynn County, GA"
classification: county
fips: "13127"
state: "GA"
demographics:
  population: 85447
  population_under_18: 17784
  population_18_64: 48265
  population_65_plus: 19398
  median_household_income: 69799
  poverty_rate: 16.06
  homeownership_rate: 66.67
  unemployment_rate: 3.73
  median_home_value: 301300
  gini_index: 0.5018
  vacancy_rate: 18.29
  race_white: 54821
  race_black: 20747
  race_asian: 1106
  race_native: 266
  hispanic: 6637
  bachelors_plus: 27600
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.8
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.7955
  - to: "us/states/ga/districts/house/167"
    rel: in-district
    area_weight: 0.4128
  - to: "us/states/ga/districts/house/179"
    rel: in-district
    area_weight: 0.2553
  - to: "us/states/ga/districts/house/180"
    rel: in-district
    area_weight: 0.1274
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Glynn County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 85447 |
| Under 18 | 17784 |
| 18–64 | 48265 |
| 65+ | 19398 |
| Median household income | 69799 |
| Poverty rate | 16.06 |
| Homeownership rate | 66.67 |
| Unemployment rate | 3.73 |
| Median home value | 301300 |
| Gini index | 0.5018 |
| Vacancy rate | 18.29 |
| White | 54821 |
| Black | 20747 |
| Asian | 1106 |
| Native | 266 |
| Hispanic/Latino | 6637 |
| Bachelor's or higher | 27600 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 80% (congressional)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 80% (state senate)
- [GA House District 167](/us/states/ga/districts/house/167.md) — 41% (state house)
- [GA House District 179](/us/states/ga/districts/house/179.md) — 26% (state house)
- [GA House District 180](/us/states/ga/districts/house/180.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
