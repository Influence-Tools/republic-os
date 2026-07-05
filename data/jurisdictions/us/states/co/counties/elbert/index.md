---
type: Jurisdiction
title: "Elbert County, CO"
classification: county
fips: "08039"
state: "CO"
demographics:
  population: 27874
  population_under_18: 5919
  population_18_64: 16709
  population_65_plus: 5246
  median_household_income: 132685
  poverty_rate: 5.28
  homeownership_rate: 95.03
  unemployment_rate: 3.39
  median_home_value: 709800
  gini_index: 0.4118
  vacancy_rate: 4.81
  race_white: 23624
  race_black: 215
  race_asian: 199
  race_native: 85
  hispanic: 2562
  bachelors_plus: 9470
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/56"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Elbert County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27874 |
| Under 18 | 5919 |
| 18–64 | 16709 |
| 65+ | 5246 |
| Median household income | 132685 |
| Poverty rate | 5.28 |
| Homeownership rate | 95.03 |
| Unemployment rate | 3.39 |
| Median home value | 709800 |
| Gini index | 0.4118 |
| Vacancy rate | 4.81 |
| White | 23624 |
| Black | 215 |
| Asian | 199 |
| Native | 85 |
| Hispanic/Latino | 2562 |
| Bachelor's or higher | 9470 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 56](/us/states/co/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
