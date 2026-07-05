---
type: Jurisdiction
title: "Santa Barbara County, CA"
classification: county
fips: "06083"
state: "CA"
demographics:
  population: 443701
  population_under_18: 99399
  population_18_64: 270592
  population_65_plus: 73710
  median_household_income: 98161
  poverty_rate: 14.74
  homeownership_rate: 52.37
  unemployment_rate: 6.42
  median_home_value: 790700
  gini_index: 0.4944
  vacancy_rate: 6.84
  race_white: 213134
  race_black: 7570
  race_asian: 23694
  race_native: 9181
  hispanic: 213992
  bachelors_plus: 143776
districts:
  - to: "us/states/ca/districts/24"
    rel: in-district
    area_weight: 0.7265
  - to: "us/states/ca/districts/senate/21"
    rel: in-district
    area_weight: 0.7271
  - to: "us/states/ca/districts/house/37"
    rel: in-district
    area_weight: 0.727
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Santa Barbara County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 443701 |
| Under 18 | 99399 |
| 18–64 | 270592 |
| 65+ | 73710 |
| Median household income | 98161 |
| Poverty rate | 14.74 |
| Homeownership rate | 52.37 |
| Unemployment rate | 6.42 |
| Median home value | 790700 |
| Gini index | 0.4944 |
| Vacancy rate | 6.84 |
| White | 213134 |
| Black | 7570 |
| Asian | 23694 |
| Native | 9181 |
| Hispanic/Latino | 213992 |
| Bachelor's or higher | 143776 |

## Districts

- [CA-24](/us/states/ca/districts/24.md) — 73% (congressional)
- [CA Senate District 21](/us/states/ca/districts/senate/21.md) — 73% (state senate)
- [CA House District 37](/us/states/ca/districts/house/37.md) — 73% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
