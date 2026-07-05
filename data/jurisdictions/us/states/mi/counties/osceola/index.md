---
type: Jurisdiction
title: "Osceola County, MI"
classification: county
fips: "26133"
state: "MI"
demographics:
  population: 23227
  population_under_18: 5173
  population_18_64: 12935
  population_65_plus: 5119
  median_household_income: 58267
  poverty_rate: 15.84
  homeownership_rate: 83.7
  unemployment_rate: 6.39
  median_home_value: 155400
  gini_index: 0.4302
  vacancy_rate: 25.97
  race_white: 21448
  race_black: 265
  race_asian: 97
  race_native: 65
  hispanic: 494
  bachelors_plus: 3632
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/100"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Osceola County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23227 |
| Under 18 | 5173 |
| 18–64 | 12935 |
| 65+ | 5119 |
| Median household income | 58267 |
| Poverty rate | 15.84 |
| Homeownership rate | 83.7 |
| Unemployment rate | 6.39 |
| Median home value | 155400 |
| Gini index | 0.4302 |
| Vacancy rate | 25.97 |
| White | 21448 |
| Black | 265 |
| Asian | 97 |
| Native | 65 |
| Hispanic/Latino | 494 |
| Bachelor's or higher | 3632 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 100% (state senate)
- [MI House District 100](/us/states/mi/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
