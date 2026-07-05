---
type: Jurisdiction
title: "Franklin County, MA"
classification: county
fips: "25011"
state: "MA"
demographics:
  population: 70944
  population_under_18: 11803
  population_18_64: 41681
  population_65_plus: 17460
  median_household_income: 74907
  poverty_rate: 12.12
  homeownership_rate: 70.14
  unemployment_rate: 5.38
  median_home_value: 329000
  gini_index: 0.4361
  vacancy_rate: 8.57
  race_white: 63125
  race_black: 956
  race_asian: 1439
  race_native: 82
  hispanic: 3839
  bachelors_plus: 32142
districts:
  - to: "us/states/ma/districts/02"
    rel: in-district
    area_weight: 0.8723
  - to: "us/states/ma/districts/01"
    rel: in-district
    area_weight: 0.1275
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Franklin County, MA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70944 |
| Under 18 | 11803 |
| 18–64 | 41681 |
| 65+ | 17460 |
| Median household income | 74907 |
| Poverty rate | 12.12 |
| Homeownership rate | 70.14 |
| Unemployment rate | 5.38 |
| Median home value | 329000 |
| Gini index | 0.4361 |
| Vacancy rate | 8.57 |
| White | 63125 |
| Black | 956 |
| Asian | 1439 |
| Native | 82 |
| Hispanic/Latino | 3839 |
| Bachelor's or higher | 32142 |

## Districts

- [MA-02](/us/states/ma/districts/02.md) — 87% (congressional)
- [MA-01](/us/states/ma/districts/01.md) — 13% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
