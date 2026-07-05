---
type: Jurisdiction
title: "Siskiyou County, CA"
classification: county
fips: "06093"
state: "CA"
demographics:
  population: 43466
  population_under_18: 8690
  population_18_64: 22675
  population_65_plus: 12101
  median_household_income: 59095
  poverty_rate: 16.38
  homeownership_rate: 69.2
  unemployment_rate: 7.89
  median_home_value: 309500
  gini_index: 0.4823
  vacancy_rate: 17.36
  race_white: 33672
  race_black: 592
  race_asian: 800
  race_native: 1417
  hispanic: 5860
  bachelors_plus: 10046
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Siskiyou County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43466 |
| Under 18 | 8690 |
| 18–64 | 22675 |
| 65+ | 12101 |
| Median household income | 59095 |
| Poverty rate | 16.38 |
| Homeownership rate | 69.2 |
| Unemployment rate | 7.89 |
| Median home value | 309500 |
| Gini index | 0.4823 |
| Vacancy rate | 17.36 |
| White | 33672 |
| Black | 592 |
| Asian | 800 |
| Native | 1417 |
| Hispanic/Latino | 5860 |
| Bachelor's or higher | 10046 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
