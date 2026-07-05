---
type: Jurisdiction
title: "Daggett County, UT"
classification: county
fips: "49009"
state: "UT"
demographics:
  population: 783
  population_under_18: 165
  population_18_64: 453
  population_65_plus: 165
  median_household_income: 66000
  poverty_rate: 9.02
  homeownership_rate: 82.29
  unemployment_rate: 6.65
  median_home_value: 282300
  gini_index: 0.4099
  vacancy_rate: 75.24
  race_white: 711
  race_black: 0
  race_asian: 0
  race_native: 29
  hispanic: 22
  bachelors_plus: 141
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ut/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ut/districts/house/68"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Daggett County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 783 |
| Under 18 | 165 |
| 18–64 | 453 |
| 65+ | 165 |
| Median household income | 66000 |
| Poverty rate | 9.02 |
| Homeownership rate | 82.29 |
| Unemployment rate | 6.65 |
| Median home value | 282300 |
| Gini index | 0.4099 |
| Vacancy rate | 75.24 |
| White | 711 |
| Black | 0 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 22 |
| Bachelor's or higher | 141 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 100% (congressional)
- [UT Senate District 20](/us/states/ut/districts/senate/20.md) — 100% (state senate)
- [UT House District 68](/us/states/ut/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
