---
type: Jurisdiction
title: "Pulaski County, IL"
classification: county
fips: "17153"
state: "IL"
demographics:
  population: 5015
  population_under_18: 1032
  population_18_64: 2811
  population_65_plus: 1172
  median_household_income: 42463
  poverty_rate: 24.98
  homeownership_rate: 68.25
  unemployment_rate: 4.28
  median_home_value: 85100
  gini_index: 0.4395
  vacancy_rate: 31.95
  race_white: 3106
  race_black: 1694
  race_asian: 8
  race_native: 0
  hispanic: 52
  bachelors_plus: 610
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/il/districts/house/118"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Pulaski County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5015 |
| Under 18 | 1032 |
| 18–64 | 2811 |
| 65+ | 1172 |
| Median household income | 42463 |
| Poverty rate | 24.98 |
| Homeownership rate | 68.25 |
| Unemployment rate | 4.28 |
| Median home value | 85100 |
| Gini index | 0.4395 |
| Vacancy rate | 31.95 |
| White | 3106 |
| Black | 1694 |
| Asian | 8 |
| Native | 0 |
| Hispanic/Latino | 52 |
| Bachelor's or higher | 610 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 118](/us/states/il/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
