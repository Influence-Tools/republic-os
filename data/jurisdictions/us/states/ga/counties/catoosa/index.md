---
type: Jurisdiction
title: "Catoosa County, GA"
classification: county
fips: "13047"
state: "GA"
demographics:
  population: 68634
  population_under_18: 15052
  population_18_64: 40776
  population_65_plus: 12806
  median_household_income: 74639
  poverty_rate: 9.85
  homeownership_rate: 74.25
  unemployment_rate: 4.26
  median_home_value: 240900
  gini_index: 0.4265
  vacancy_rate: 6.7
  race_white: 60605
  race_black: 946
  race_asian: 1045
  race_native: 209
  hispanic: 2778
  bachelors_plus: 16161
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/53"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/3"
    rel: in-district
    area_weight: 0.7479
  - to: "us/states/ga/districts/house/2"
    rel: in-district
    area_weight: 0.2518
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Catoosa County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68634 |
| Under 18 | 15052 |
| 18–64 | 40776 |
| 65+ | 12806 |
| Median household income | 74639 |
| Poverty rate | 9.85 |
| Homeownership rate | 74.25 |
| Unemployment rate | 4.26 |
| Median home value | 240900 |
| Gini index | 0.4265 |
| Vacancy rate | 6.7 |
| White | 60605 |
| Black | 946 |
| Asian | 1045 |
| Native | 209 |
| Hispanic/Latino | 2778 |
| Bachelor's or higher | 16161 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 53](/us/states/ga/districts/senate/53.md) — 100% (state senate)
- [GA House District 3](/us/states/ga/districts/house/3.md) — 75% (state house)
- [GA House District 2](/us/states/ga/districts/house/2.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
