---
type: Jurisdiction
title: "Tift County, GA"
classification: county
fips: "13277"
state: "GA"
demographics:
  population: 41438
  population_under_18: 10273
  population_18_64: 24566
  population_65_plus: 6599
  median_household_income: 53255
  poverty_rate: 20.8
  homeownership_rate: 61.04
  unemployment_rate: 2.82
  median_home_value: 165200
  gini_index: 0.487
  vacancy_rate: 11.89
  race_white: 23418
  race_black: 12316
  race_asian: 539
  race_native: 255
  hispanic: 5472
  bachelors_plus: 8647
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/170"
    rel: in-district
    area_weight: 0.5774
  - to: "us/states/ga/districts/house/169"
    rel: in-district
    area_weight: 0.4226
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Tift County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41438 |
| Under 18 | 10273 |
| 18–64 | 24566 |
| 65+ | 6599 |
| Median household income | 53255 |
| Poverty rate | 20.8 |
| Homeownership rate | 61.04 |
| Unemployment rate | 2.82 |
| Median home value | 165200 |
| Gini index | 0.487 |
| Vacancy rate | 11.89 |
| White | 23418 |
| Black | 12316 |
| Asian | 539 |
| Native | 255 |
| Hispanic/Latino | 5472 |
| Bachelor's or higher | 8647 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 170](/us/states/ga/districts/house/170.md) — 58% (state house)
- [GA House District 169](/us/states/ga/districts/house/169.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
