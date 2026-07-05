---
type: Jurisdiction
title: "Johnson County, GA"
classification: county
fips: "13167"
state: "GA"
demographics:
  population: 9190
  population_under_18: 1633
  population_18_64: 5690
  population_65_plus: 1867
  median_household_income: 51028
  poverty_rate: 24.24
  homeownership_rate: 75.94
  unemployment_rate: 7.44
  median_home_value: 94900
  gini_index: 0.4736
  vacancy_rate: 9.63
  race_white: 5714
  race_black: 3027
  race_asian: 0
  race_native: 26
  hispanic: 162
  bachelors_plus: 880
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/155"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Johnson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9190 |
| Under 18 | 1633 |
| 18–64 | 5690 |
| 65+ | 1867 |
| Median household income | 51028 |
| Poverty rate | 24.24 |
| Homeownership rate | 75.94 |
| Unemployment rate | 7.44 |
| Median home value | 94900 |
| Gini index | 0.4736 |
| Vacancy rate | 9.63 |
| White | 5714 |
| Black | 3027 |
| Asian | 0 |
| Native | 26 |
| Hispanic/Latino | 162 |
| Bachelor's or higher | 880 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 100% (state senate)
- [GA House District 155](/us/states/ga/districts/house/155.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
