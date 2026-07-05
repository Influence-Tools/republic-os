---
type: Jurisdiction
title: "Colquitt County, GA"
classification: county
fips: "13071"
state: "GA"
demographics:
  population: 46224
  population_under_18: 11856
  population_18_64: 26920
  population_65_plus: 7448
  median_household_income: 49341
  poverty_rate: 22.87
  homeownership_rate: 63.73
  unemployment_rate: 4.27
  median_home_value: 121400
  gini_index: 0.4533
  vacancy_rate: 13.39
  race_white: 25636
  race_black: 10546
  race_asian: 421
  race_native: 662
  hispanic: 9617
  bachelors_plus: 6930
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/172"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Colquitt County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46224 |
| Under 18 | 11856 |
| 18–64 | 26920 |
| 65+ | 7448 |
| Median household income | 49341 |
| Poverty rate | 22.87 |
| Homeownership rate | 63.73 |
| Unemployment rate | 4.27 |
| Median home value | 121400 |
| Gini index | 0.4533 |
| Vacancy rate | 13.39 |
| White | 25636 |
| Black | 10546 |
| Asian | 421 |
| Native | 662 |
| Hispanic/Latino | 9617 |
| Bachelor's or higher | 6930 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 172](/us/states/ga/districts/house/172.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
