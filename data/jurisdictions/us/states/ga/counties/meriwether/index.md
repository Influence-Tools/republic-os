---
type: Jurisdiction
title: "Meriwether County, GA"
classification: county
fips: "13199"
state: "GA"
demographics:
  population: 20929
  population_under_18: 4387
  population_18_64: 12069
  population_65_plus: 4473
  median_household_income: 57340
  poverty_rate: 18.93
  homeownership_rate: 73.02
  unemployment_rate: 6.59
  median_home_value: 168800
  gini_index: 0.4358
  vacancy_rate: 14.55
  race_white: 11892
  race_black: 8190
  race_asian: 142
  race_native: 17
  hispanic: 176
  bachelors_plus: 3135
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/136"
    rel: in-district
    area_weight: 0.7943
  - to: "us/states/ga/districts/house/137"
    rel: in-district
    area_weight: 0.2055
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Meriwether County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20929 |
| Under 18 | 4387 |
| 18–64 | 12069 |
| 65+ | 4473 |
| Median household income | 57340 |
| Poverty rate | 18.93 |
| Homeownership rate | 73.02 |
| Unemployment rate | 6.59 |
| Median home value | 168800 |
| Gini index | 0.4358 |
| Vacancy rate | 14.55 |
| White | 11892 |
| Black | 8190 |
| Asian | 142 |
| Native | 17 |
| Hispanic/Latino | 176 |
| Bachelor's or higher | 3135 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 29](/us/states/ga/districts/senate/29.md) — 100% (state senate)
- [GA House District 136](/us/states/ga/districts/house/136.md) — 79% (state house)
- [GA House District 137](/us/states/ga/districts/house/137.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
