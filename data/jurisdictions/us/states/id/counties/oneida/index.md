---
type: Jurisdiction
title: "Oneida County, ID"
classification: county
fips: "16071"
state: "ID"
demographics:
  population: 4768
  population_under_18: 1289
  population_18_64: 2530
  population_65_plus: 949
  median_household_income: 74954
  poverty_rate: 10.81
  homeownership_rate: 88.29
  unemployment_rate: 1.45
  median_home_value: 272000
  gini_index: 0.4255
  vacancy_rate: 8.57
  race_white: 4474
  race_black: 19
  race_asian: 0
  race_native: 29
  hispanic: 212
  bachelors_plus: 1101
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/id/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Oneida County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4768 |
| Under 18 | 1289 |
| 18–64 | 2530 |
| 65+ | 949 |
| Median household income | 74954 |
| Poverty rate | 10.81 |
| Homeownership rate | 88.29 |
| Unemployment rate | 1.45 |
| Median home value | 272000 |
| Gini index | 0.4255 |
| Vacancy rate | 8.57 |
| White | 4474 |
| Black | 19 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 212 |
| Bachelor's or higher | 1101 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 27](/us/states/id/districts/senate/27.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
