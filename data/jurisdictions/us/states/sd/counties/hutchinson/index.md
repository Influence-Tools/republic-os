---
type: Jurisdiction
title: "Hutchinson County, SD"
classification: county
fips: "46067"
state: "SD"
demographics:
  population: 7404
  population_under_18: 1957
  population_18_64: 3834
  population_65_plus: 1613
  median_household_income: 73977
  poverty_rate: 12.16
  homeownership_rate: 77.27
  unemployment_rate: 1.65
  median_home_value: 163000
  gini_index: 0.4342
  vacancy_rate: 10.14
  race_white: 6747
  race_black: 8
  race_asian: 27
  race_native: 75
  hispanic: 200
  bachelors_plus: 1754
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/19"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Hutchinson County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7404 |
| Under 18 | 1957 |
| 18–64 | 3834 |
| 65+ | 1613 |
| Median household income | 73977 |
| Poverty rate | 12.16 |
| Homeownership rate | 77.27 |
| Unemployment rate | 1.65 |
| Median home value | 163000 |
| Gini index | 0.4342 |
| Vacancy rate | 10.14 |
| White | 6747 |
| Black | 8 |
| Asian | 27 |
| Native | 75 |
| Hispanic/Latino | 200 |
| Bachelor's or higher | 1754 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 19](/us/states/sd/districts/senate/19.md) — 100% (state senate)
- [SD House District 19](/us/states/sd/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
