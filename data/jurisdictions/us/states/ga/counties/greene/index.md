---
type: Jurisdiction
title: "Greene County, GA"
classification: county
fips: "13133"
state: "GA"
demographics:
  population: 20109
  population_under_18: 3460
  population_18_64: 10438
  population_65_plus: 6211
  median_household_income: 86272
  poverty_rate: 9.8
  homeownership_rate: 77.95
  unemployment_rate: 3.43
  median_home_value: 394800
  gini_index: 0.5628
  vacancy_rate: 24.3
  race_white: 11931
  race_black: 5983
  race_asian: 250
  race_native: 114
  hispanic: 1442
  bachelors_plus: 7969
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/124"
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

# Greene County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20109 |
| Under 18 | 3460 |
| 18–64 | 10438 |
| 65+ | 6211 |
| Median household income | 86272 |
| Poverty rate | 9.8 |
| Homeownership rate | 77.95 |
| Unemployment rate | 3.43 |
| Median home value | 394800 |
| Gini index | 0.5628 |
| Vacancy rate | 24.3 |
| White | 11931 |
| Black | 5983 |
| Asian | 250 |
| Native | 114 |
| Hispanic/Latino | 1442 |
| Bachelor's or higher | 7969 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 124](/us/states/ga/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
