---
type: Jurisdiction
title: "Elbert County, GA"
classification: county
fips: "13105"
state: "GA"
demographics:
  population: 19849
  population_under_18: 4380
  population_18_64: 11268
  population_65_plus: 4201
  median_household_income: 58450
  poverty_rate: 17.98
  homeownership_rate: 70.93
  unemployment_rate: 4.59
  median_home_value: 142000
  gini_index: 0.4251
  vacancy_rate: 11.14
  race_white: 12568
  race_black: 4430
  race_asian: 261
  race_native: 91
  hispanic: 1174
  bachelors_plus: 3162
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/123"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Elbert County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19849 |
| Under 18 | 4380 |
| 18–64 | 11268 |
| 65+ | 4201 |
| Median household income | 58450 |
| Poverty rate | 17.98 |
| Homeownership rate | 70.93 |
| Unemployment rate | 4.59 |
| Median home value | 142000 |
| Gini index | 0.4251 |
| Vacancy rate | 11.14 |
| White | 12568 |
| Black | 4430 |
| Asian | 261 |
| Native | 91 |
| Hispanic/Latino | 1174 |
| Bachelor's or higher | 3162 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 123](/us/states/ga/districts/house/123.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
