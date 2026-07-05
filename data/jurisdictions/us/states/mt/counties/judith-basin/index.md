---
type: Jurisdiction
title: "Judith Basin County, MT"
classification: county
fips: "30045"
state: "MT"
demographics:
  population: 2071
  population_under_18: 466
  population_18_64: 1066
  population_65_plus: 539
  median_household_income: 59000
  poverty_rate: 13.31
  homeownership_rate: 72.66
  unemployment_rate: 0.09
  median_home_value: 238300
  gini_index: 0.4588
  vacancy_rate: 27.2
  race_white: 1868
  race_black: 0
  race_asian: 0
  race_native: 29
  hispanic: 159
  bachelors_plus: 561
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/78"
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

# Judith Basin County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2071 |
| Under 18 | 466 |
| 18–64 | 1066 |
| 65+ | 539 |
| Median household income | 59000 |
| Poverty rate | 13.31 |
| Homeownership rate | 72.66 |
| Unemployment rate | 0.09 |
| Median home value | 238300 |
| Gini index | 0.4588 |
| Vacancy rate | 27.2 |
| White | 1868 |
| Black | 0 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 159 |
| Bachelor's or higher | 561 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 100% (state senate)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
