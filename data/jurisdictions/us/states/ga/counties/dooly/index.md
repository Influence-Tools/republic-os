---
type: Jurisdiction
title: "Dooly County, GA"
classification: county
fips: "13093"
state: "GA"
demographics:
  population: 10984
  population_under_18: 1710
  population_18_64: 6830
  population_65_plus: 2444
  median_household_income: 60987
  poverty_rate: 15.73
  homeownership_rate: 64.7
  unemployment_rate: 3.57
  median_home_value: 107400
  gini_index: 0.437
  vacancy_rate: 15.63
  race_white: 4548
  race_black: 5179
  race_asian: 0
  race_native: 102
  hispanic: 915
  bachelors_plus: 1699
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/150"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Dooly County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10984 |
| Under 18 | 1710 |
| 18–64 | 6830 |
| 65+ | 2444 |
| Median household income | 60987 |
| Poverty rate | 15.73 |
| Homeownership rate | 64.7 |
| Unemployment rate | 3.57 |
| Median home value | 107400 |
| Gini index | 0.437 |
| Vacancy rate | 15.63 |
| White | 4548 |
| Black | 5179 |
| Asian | 0 |
| Native | 102 |
| Hispanic/Latino | 915 |
| Bachelor's or higher | 1699 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 150](/us/states/ga/districts/house/150.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
