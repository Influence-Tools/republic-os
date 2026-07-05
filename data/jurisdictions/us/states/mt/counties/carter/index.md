---
type: Jurisdiction
title: "Carter County, MT"
classification: county
fips: "30011"
state: "MT"
demographics:
  population: 1308
  population_under_18: 231
  population_18_64: 670
  population_65_plus: 407
  median_household_income: 54167
  poverty_rate: 15.4
  homeownership_rate: 62.17
  unemployment_rate: 2.84
  median_home_value: 199200
  gini_index: 0.4057
  vacancy_rate: 27.62
  race_white: 1167
  race_black: 2
  race_asian: 0
  race_native: 2
  hispanic: 32
  bachelors_plus: 256
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Carter County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1308 |
| Under 18 | 231 |
| 18–64 | 670 |
| 65+ | 407 |
| Median household income | 54167 |
| Poverty rate | 15.4 |
| Homeownership rate | 62.17 |
| Unemployment rate | 2.84 |
| Median home value | 199200 |
| Gini index | 0.4057 |
| Vacancy rate | 27.62 |
| White | 1167 |
| Black | 2 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 32 |
| Bachelor's or higher | 256 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
