---
type: Jurisdiction
title: "Butte County, ID"
classification: county
fips: "16023"
state: "ID"
demographics:
  population: 2684
  population_under_18: 660
  population_18_64: 1480
  population_65_plus: 544
  median_household_income: 53015
  poverty_rate: 19.25
  homeownership_rate: 77.54
  unemployment_rate: 4.37
  median_home_value: 217600
  gini_index: 0.4158
  vacancy_rate: 19.69
  race_white: 2457
  race_black: 0
  race_asian: 0
  race_native: 12
  hispanic: 173
  bachelors_plus: 427
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/30"
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

# Butte County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2684 |
| Under 18 | 660 |
| 18–64 | 1480 |
| 65+ | 544 |
| Median household income | 53015 |
| Poverty rate | 19.25 |
| Homeownership rate | 77.54 |
| Unemployment rate | 4.37 |
| Median home value | 217600 |
| Gini index | 0.4158 |
| Vacancy rate | 19.69 |
| White | 2457 |
| Black | 0 |
| Asian | 0 |
| Native | 12 |
| Hispanic/Latino | 173 |
| Bachelor's or higher | 427 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 30](/us/states/id/districts/senate/30.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
