---
type: Jurisdiction
title: "Calhoun County, IL"
classification: county
fips: "17013"
state: "IL"
demographics:
  population: 4330
  population_under_18: 861
  population_18_64: 2368
  population_65_plus: 1101
  median_household_income: 93203
  poverty_rate: 6.31
  homeownership_rate: 88.7
  unemployment_rate: 3.24
  median_home_value: 190900
  gini_index: 0.3793
  vacancy_rate: 46.13
  race_white: 4086
  race_black: 64
  race_asian: 0
  race_native: 3
  hispanic: 36
  bachelors_plus: 781
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Calhoun County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4330 |
| Under 18 | 861 |
| 18–64 | 2368 |
| 65+ | 1101 |
| Median household income | 93203 |
| Poverty rate | 6.31 |
| Homeownership rate | 88.7 |
| Unemployment rate | 3.24 |
| Median home value | 190900 |
| Gini index | 0.3793 |
| Vacancy rate | 46.13 |
| White | 4086 |
| Black | 64 |
| Asian | 0 |
| Native | 3 |
| Hispanic/Latino | 36 |
| Bachelor's or higher | 781 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
