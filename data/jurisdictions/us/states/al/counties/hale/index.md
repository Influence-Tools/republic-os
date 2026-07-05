---
type: Jurisdiction
title: "Hale County, AL"
classification: county
fips: "01065"
state: "AL"
demographics:
  population: 14829
  population_under_18: 3584
  population_18_64: 8280
  population_65_plus: 2965
  median_household_income: 39250
  poverty_rate: 24.58
  homeownership_rate: 74.39
  unemployment_rate: 6.0
  median_home_value: 127600
  gini_index: 0.5106
  vacancy_rate: 25.7
  race_white: 5645
  race_black: 8105
  race_asian: 15
  race_native: 60
  hispanic: 195
  bachelors_plus: 2400
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/72"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Hale County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14829 |
| Under 18 | 3584 |
| 18–64 | 8280 |
| 65+ | 2965 |
| Median household income | 39250 |
| Poverty rate | 24.58 |
| Homeownership rate | 74.39 |
| Unemployment rate | 6.0 |
| Median home value | 127600 |
| Gini index | 0.5106 |
| Vacancy rate | 25.7 |
| White | 5645 |
| Black | 8105 |
| Asian | 15 |
| Native | 60 |
| Hispanic/Latino | 195 |
| Bachelor's or higher | 2400 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 100% (state senate)
- [AL House District 72](/us/states/al/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
