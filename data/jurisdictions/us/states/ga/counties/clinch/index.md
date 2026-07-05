---
type: Jurisdiction
title: "Clinch County, GA"
classification: county
fips: "13065"
state: "GA"
demographics:
  population: 6759
  population_under_18: 1676
  population_18_64: 3877
  population_65_plus: 1206
  median_household_income: 45847
  poverty_rate: 26.09
  homeownership_rate: 70.84
  unemployment_rate: 2.14
  median_home_value: 84400
  gini_index: 0.5117
  vacancy_rate: 20.05
  race_white: 4376
  race_black: 1734
  race_asian: 20
  race_native: 125
  hispanic: 448
  bachelors_plus: 580
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Clinch County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6759 |
| Under 18 | 1676 |
| 18–64 | 3877 |
| 65+ | 1206 |
| Median household income | 45847 |
| Poverty rate | 26.09 |
| Homeownership rate | 70.84 |
| Unemployment rate | 2.14 |
| Median home value | 84400 |
| Gini index | 0.5117 |
| Vacancy rate | 20.05 |
| White | 4376 |
| Black | 1734 |
| Asian | 20 |
| Native | 125 |
| Hispanic/Latino | 448 |
| Bachelor's or higher | 580 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
