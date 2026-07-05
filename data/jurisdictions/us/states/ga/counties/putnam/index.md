---
type: Jurisdiction
title: "Putnam County, GA"
classification: county
fips: "13237"
state: "GA"
demographics:
  population: 22855
  population_under_18: 4436
  population_18_64: 12740
  population_65_plus: 5679
  median_household_income: 72096
  poverty_rate: 17.65
  homeownership_rate: 80.92
  unemployment_rate: 3.72
  median_home_value: 249300
  gini_index: 0.5282
  vacancy_rate: 22.73
  race_white: 14988
  race_black: 5029
  race_asian: 498
  race_native: 45
  hispanic: 1648
  bachelors_plus: 6950
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/ga/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/144"
    rel: in-district
    area_weight: 0.6283
  - to: "us/states/ga/districts/house/124"
    rel: in-district
    area_weight: 0.3713
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Putnam County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22855 |
| Under 18 | 4436 |
| 18–64 | 12740 |
| 65+ | 5679 |
| Median household income | 72096 |
| Poverty rate | 17.65 |
| Homeownership rate | 80.92 |
| Unemployment rate | 3.72 |
| Median home value | 249300 |
| Gini index | 0.5282 |
| Vacancy rate | 22.73 |
| White | 14988 |
| Black | 5029 |
| Asian | 498 |
| Native | 45 |
| Hispanic/Latino | 1648 |
| Bachelor's or higher | 6950 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 25](/us/states/ga/districts/senate/25.md) — 100% (state senate)
- [GA House District 144](/us/states/ga/districts/house/144.md) — 63% (state house)
- [GA House District 124](/us/states/ga/districts/house/124.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
