---
type: Jurisdiction
title: "San Miguel County, CO"
classification: county
fips: "08113"
state: "CO"
demographics:
  population: 7968
  population_under_18: 1442
  population_18_64: 2672
  population_65_plus: 3854
  median_household_income: 79024
  poverty_rate: 9.26
  homeownership_rate: 62.97
  unemployment_rate: 2.69
  median_home_value: 720700
  gini_index: 0.5685
  vacancy_rate: 30.83
  race_white: 6767
  race_black: 83
  race_asian: 51
  race_native: 10
  hispanic: 931
  bachelors_plus: 5218
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# San Miguel County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7968 |
| Under 18 | 1442 |
| 18–64 | 2672 |
| 65+ | 3854 |
| Median household income | 79024 |
| Poverty rate | 9.26 |
| Homeownership rate | 62.97 |
| Unemployment rate | 2.69 |
| Median home value | 720700 |
| Gini index | 0.5685 |
| Vacancy rate | 30.83 |
| White | 6767 |
| Black | 83 |
| Asian | 51 |
| Native | 10 |
| Hispanic/Latino | 931 |
| Bachelor's or higher | 5218 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
