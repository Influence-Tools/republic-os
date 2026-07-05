---
type: Jurisdiction
title: "Cook County, GA"
classification: county
fips: "13075"
state: "GA"
demographics:
  population: 17532
  population_under_18: 4458
  population_18_64: 10240
  population_65_plus: 2834
  median_household_income: 53651
  poverty_rate: 17.73
  homeownership_rate: 66.02
  unemployment_rate: 3.64
  median_home_value: 157500
  gini_index: 0.492
  vacancy_rate: 15.79
  race_white: 11194
  race_black: 4839
  race_asian: 72
  race_native: 63
  hispanic: 1335
  bachelors_plus: 2889
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/172"
    rel: in-district
    area_weight: 0.5628
  - to: "us/states/ga/districts/house/170"
    rel: in-district
    area_weight: 0.4369
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Cook County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17532 |
| Under 18 | 4458 |
| 18–64 | 10240 |
| 65+ | 2834 |
| Median household income | 53651 |
| Poverty rate | 17.73 |
| Homeownership rate | 66.02 |
| Unemployment rate | 3.64 |
| Median home value | 157500 |
| Gini index | 0.492 |
| Vacancy rate | 15.79 |
| White | 11194 |
| Black | 4839 |
| Asian | 72 |
| Native | 63 |
| Hispanic/Latino | 1335 |
| Bachelor's or higher | 2889 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 172](/us/states/ga/districts/house/172.md) — 56% (state house)
- [GA House District 170](/us/states/ga/districts/house/170.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
