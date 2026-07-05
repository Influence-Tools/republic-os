---
type: Jurisdiction
title: "Troup County, GA"
classification: county
fips: "13285"
state: "GA"
demographics:
  population: 70330
  population_under_18: 17223
  population_18_64: 41933
  population_65_plus: 11174
  median_household_income: 56776
  poverty_rate: 16.9
  homeownership_rate: 60.58
  unemployment_rate: 5.3
  median_home_value: 217200
  gini_index: 0.4921
  vacancy_rate: 9.69
  race_white: 38908
  race_black: 25321
  race_asian: 1638
  race_native: 51
  hispanic: 3315
  bachelors_plus: 16076
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/29"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/138"
    rel: in-district
    area_weight: 0.3967
  - to: "us/states/ga/districts/house/137"
    rel: in-district
    area_weight: 0.2529
  - to: "us/states/ga/districts/house/72"
    rel: in-district
    area_weight: 0.2434
  - to: "us/states/ga/districts/house/136"
    rel: in-district
    area_weight: 0.107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Troup County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70330 |
| Under 18 | 17223 |
| 18–64 | 41933 |
| 65+ | 11174 |
| Median household income | 56776 |
| Poverty rate | 16.9 |
| Homeownership rate | 60.58 |
| Unemployment rate | 5.3 |
| Median home value | 217200 |
| Gini index | 0.4921 |
| Vacancy rate | 9.69 |
| White | 38908 |
| Black | 25321 |
| Asian | 1638 |
| Native | 51 |
| Hispanic/Latino | 3315 |
| Bachelor's or higher | 16076 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 29](/us/states/ga/districts/senate/29.md) — 100% (state senate)
- [GA House District 138](/us/states/ga/districts/house/138.md) — 40% (state house)
- [GA House District 137](/us/states/ga/districts/house/137.md) — 25% (state house)
- [GA House District 72](/us/states/ga/districts/house/72.md) — 24% (state house)
- [GA House District 136](/us/states/ga/districts/house/136.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
