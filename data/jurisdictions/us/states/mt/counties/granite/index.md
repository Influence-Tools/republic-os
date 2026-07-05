---
type: Jurisdiction
title: "Granite County, MT"
classification: county
fips: "30039"
state: "MT"
demographics:
  population: 3462
  population_under_18: 509
  population_18_64: 1871
  population_65_plus: 1082
  median_household_income: 59265
  poverty_rate: 10.17
  homeownership_rate: 77.87
  unemployment_rate: 3.72
  median_home_value: 352700
  gini_index: 0.4614
  vacancy_rate: 41.81
  race_white: 3134
  race_black: 9
  race_asian: 32
  race_native: 63
  hispanic: 91
  bachelors_plus: 1079
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/76"
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

# Granite County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3462 |
| Under 18 | 509 |
| 18–64 | 1871 |
| 65+ | 1082 |
| Median household income | 59265 |
| Poverty rate | 10.17 |
| Homeownership rate | 77.87 |
| Unemployment rate | 3.72 |
| Median home value | 352700 |
| Gini index | 0.4614 |
| Vacancy rate | 41.81 |
| White | 3134 |
| Black | 9 |
| Asian | 32 |
| Native | 63 |
| Hispanic/Latino | 91 |
| Bachelor's or higher | 1079 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 38](/us/states/mt/districts/senate/38.md) — 100% (state senate)
- [MT House District 76](/us/states/mt/districts/house/76.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
